from qgis.core import (
     QgsVectorLayer,
     QgsPointXY,
     QgsGeometry,
     QgsFeature,
     QgsProject,
     QgsMapLayerType,
     Qgis,
     QgsWkbTypes,
     QgsLineSymbol,
     QgsRendererCategory,
     QgsCategorizedSymbolRenderer,
     QgsRectangle,
     QgsPoint
     )

from .models.segment import Segment
from .models.data_classes import FeatureContext

def new_vector_layer(reference_layer, new_layer_name, field_names_n_types: list[(str, str)], geometry_type: str):

     field_descriptions = []
     for pair in field_names_n_types:
          name, type = pair
          field_descriptions.append(f"&field={name}:{type}")

     return QgsVectorLayer(
                    f"{geometry_type}?crs={reference_layer.crs().authid()}{"".join(field_descriptions)}", 
                    new_layer_name,
                    "memory"
               )

def segment_from_xypoints(target_layer: QgsVectorLayer, xy_points: tuple[QgsPointXY, QgsPointXY], name: str) -> Segment:

     point_1, point_2 = xy_points

     new_segment_geom = QgsGeometry.fromPolylineXY([point_1, point_2])
     feature = QgsFeature(target_layer.fields())
     feature.setGeometry(new_segment_geom)
     target_layer.dataProvider().addFeature(feature)
     
     return Segment(name, FeatureContext(target_layer, feature))

#TODO: fazer renderer e definição de nome do ponto
def qgspoint_from_xypoint(target_layer: QgsVectorLayer, point: QgsPointXY) -> QgsPoint:

     new_point = QgsGeometry.fromPointXY(point)
     feature = QgsFeature(target_layer.fields())
     feature.setGeometry(new_point)
     target_layer.dataProvider().addFeature(feature)

     return new_point.get()

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


def capture_polygons(self, project: QgsProject):
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
