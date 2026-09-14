from qgis.core import (
     QgsProject, 
     QgsMapLayerType, 
     QgsWkbTypes, 
     Qgis, 
     QgsCategorizedSymbolRenderer,
     QgsRendererCategory,
     QgsLineSymbol,
     QgsVectorLayer,
     QgsGeometry,
     QgsFeature,
     QgsRectangle,
)

from .models.data_classes import FeatureContext
from .models.basic_parcel import BasicParcel
from .models.full_parcel import FullParcel
from .models.data_classes import GeneralInfoObject
from .models.complements import Street
from .models.segment import Segment
from .dialogs.general_info_dialog import GeneralInfoDialog
from .dialogs.basic_parcels_wizard import BasicParcelsWizard
from .dialogs.main_parcel_dialog import MainParcelDialog
from .dialogs.sides_definition_wizard import SidesDefinitionWizard
from .dialogs.street_confrontations_dialog import StreetConfrontationsDialog
from .utils.number_format import string_to_float



def process_general_info_dialog(general_info: GeneralInfoObject | None = None) -> GeneralInfoObject | None:

     general_info_dialog = GeneralInfoDialog()
     
     if general_info is not None:
          general_info_dialog.pre_set(general_info)
     
     accepted = general_info_dialog.exec_()
     if accepted:
          general_info = general_info_dialog.as_general_info_object()
          return general_info
     else:
          return None

def process_parcel_definition(iface, project: QgsProject) -> tuple[BasicParcel, list[BasicParcel]] | None:

     #TODO: Criar verificação de features selecionadas antes de continuar
     feature_list = filter_polygon_features(project)
     zoom_to_features(iface, feature_list)
     parcel_definition_wizard = BasicParcelsWizard(feature_list)

     accepted = parcel_definition_wizard.exec_()

     parcels: list[BasicParcel] = []
     if accepted:
          for result in parcel_definition_wizard.get_results():
               parcels.append(BasicParcel(
                    result["parcel_name"],
                    result["block"],
                    result["site_plan"],
                    result["site_plan_code"],
                    result["feature_context"]
               ))
          
          main_parcel_name = parcel_definition_wizard.get_main_parcel_name()
     else:
          return None

     main_parcel = next((parcel for parcel in parcels if parcel.name == main_parcel_name), None)
     if main_parcel is not None:
          parcels.remove(main_parcel)
     else:
          #TODO: implementar alternativa caso não selecionado??
          raise NotImplementedError
     result = (main_parcel, parcels)
     return result

def process_main_parcel_dialog(base_parcel: BasicParcel) -> FullParcel | None:

     main_parcel_dialog = MainParcelDialog(base_parcel)
     accepted = main_parcel_dialog.exec_()

     if accepted:
          result = main_parcel_dialog.get_result()
          main_parcel = FullParcel(
               base_parcel,
               result.district,
               result.street_side,
               Street(result.main_street_name, result.main_street_code) if result.main_street_name else None,
               result.number,
               result.shape,
               string_to_float(result.distance_to_corner),
               Street(result.cross_street_name, result.cross_street_code),
               result.property_identifier
          )
     else:
          return None

     return main_parcel

def process_sides_definition(iface, project: QgsProject, parcel: FullParcel) -> bool:

     layer_name = f"camada-de-segmentos-lote-{parcel.name}"
     found_layers: list[QgsVectorLayer] = project.mapLayersByName(layer_name)
     
     if found_layers:
          #TODO: Criar forma de verificar se usuário deseja reutilizar camada
          segments_layer = found_layers[0]

          segments = []

          for feature in segments_layer.getFeatures():
               segment = Segment(feature["name"], FeatureContext(segments_layer, feature))
               segments.append(segment)
     else:
          segments_layer = QgsVectorLayer(
               "LineString?crs=" + parcel.feature_context.layer.crs().authid() + "&field=id:integer&field=name:string(5)&field=side:string(10)", 
               layer_name,
               "memory"
          )
          project.addMapLayer(segments_layer)

          provider = segments_layer.dataProvider()
          geom = parcel.feature_context.feature.geometry()
          xy_points = geom.asMultiPolygon()[0][0]

          # ring_geom = QgsGeometry.fromPolygonXY([xy_points])
          # if ring_geom.isPolygonClockwise():
          #      xy_points = list(reversed(xy_points))
          segments = []

          for point_1, point_2 in zip(xy_points, xy_points[1:]):
               new_segment_geom = QgsGeometry.fromPolylineXY([point_1, point_2])
               feature = QgsFeature(segments_layer.fields())
               new_id = segments_layer.featureCount()+1
               new_name = "S"+str(new_id)
               feature.setAttributes([new_id, new_name, "undefined"])
               feature.setGeometry(new_segment_geom)
               provider.addFeature(feature)
               segment = Segment(new_name, FeatureContext(segments_layer, feature))
               segments.append(segment)
               
          segments_layer.setRenderer(create_sidebased_rederer())
          segments_layer.triggerRepaint()

     #Abre dialog para definir lados
     focus_feature(parcel.feature_context.feature, iface)
     sides_definition_widget = SidesDefinitionWizard(segments)
     accepted = sides_definition_widget.exec_()
     if accepted:
          #Passa lados para o main_parcel
          result = sides_definition_widget.get_result()
          parcel.define_sides(result.front, result.left, result.right, result.back)
          return True
     else:
          return False

def process_confrontation_definition(parcel: FullParcel) -> bool:

     sides = [
          parcel.front,
          parcel.left_side,
          parcel.right_side,
     ]
     if parcel.back is not None:
          sides.append(parcel.back)
     dialog = StreetConfrontationsDialog(sides)
     accepted = dialog.exec_()

     return accepted

def filter_polygon_features(project: QgsProject) -> list[FeatureContext]:
     result_list = []
     for layer in project.mapLayers().values():    
          if layer.type() == QgsMapLayerType.VectorLayer and layer.geometryType() == QgsWkbTypes.PolygonGeometry:
               for feature in layer.getSelectedFeatures():
                    if feature.geometry().type() == Qgis.GeometryType.Polygon:
                         result_list.append(FeatureContext(layer=layer, feature=feature))
     return result_list

def create_sidebased_rederer() -> QgsCategorizedSymbolRenderer:

     categories = []

     colors = {
     "front": "red",
     "right": "blue",
     "back": "orange",
     "left": "green",
     "undefined": "grey"
     }

     for side, color in colors.items():

          symbol = QgsLineSymbol.createSimple({
               "color": color,
               "width": "2.0"
          })

          categories.append(
               QgsRendererCategory(
                    side,
                    symbol,
                    side
               )
          )

     return QgsCategorizedSymbolRenderer("side", categories)

def capture_polygons(self, project):
     # capture the project's polygons
     polygon_layers = {
          layer 
          for layer in project.mapLayers().values() 
          if layer.type() == QgsMapLayerType.VectorLayer
          and layer.geometryType() == QgsWkbTypes.PolygonGeometry
          }
     print("capture the polygons in each layer and verifies multiPolygons")
     polygons = []
     multi_polygons = []
     for layer in polygon_layers:
          for feature in layer.getFeatures():
               geom = feature.geometry()
               if geom.type() == Qgis.GeometryType.Polygon:
                    print("Encontrado multiPolígono")
                    geom_collection = geom.asGeometryCollection()
                    if len(geom_collection) == 1:
                         print("Encontrado multiPolígono com 1 elemento")
                         polygons.append({
                                   "name": f"{layer.name()} {str(feature.id()) if layer.featureCount()>1 else ''}",
                                   "geom": geom_collection[0]
                                   })
                    elif len(geom_collection) > 1:
                         print("Encontrado multipoligono com mais de 1 elemento")
                         multi_polygons.append(geom)

     print("\nPolígonos únicos encontrados:")
     for polygon in polygons:
          print("Polígono:", polygon["name"], polygon["geom"].asWkt())
     if len(multi_polygons)>0:
          print("aviso! Encontrados Multipolígonos!")
     else:
          print("Nenhum MultiPolígono encontrado!")
     print("end of phase1")
     return polygons

def focus_feature(feature, iface):
     extent = feature.geometry().boundingBox()

     extent.scale(1.2)

     iface.mapCanvas().setExtent(extent)
     iface.mapCanvas().refresh()

def zoom_to_features(iface, feature_contexts: list[FeatureContext]):
     extent = QgsRectangle()

     for fc in feature_contexts:
          geometry = fc.feature.geometry()

          if not geometry.isEmpty():
               extent.combineExtentWith(geometry.boundingBox())

     if not extent.isEmpty():
          extent.scale(1.2)
          iface.mapCanvas().setExtent(extent)
          iface.mapCanvas().refresh()