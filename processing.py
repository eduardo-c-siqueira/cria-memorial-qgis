from dialogs.street_confrontations_dialog import StreetConfrontationsDialog
from qgis.core import (
     QgsProject, 
     QgsVectorLayer,
     QgsGeometry,
)
from .qgs_processing import (
     create_sidebased_rederer, 
     focus_feature, 
     new_vector_layer,
     segment_from_xypoints, 
     zoom_to_features, 
)

from .models.data_classes import FeatureContext
from .models.basic_parcel import BasicParcel
from .models.full_parcel import FullParcel
from .models.data_classes import GeneralInfoObject
from .models.street import Street
from .models.segment import Segment
from .models.user_settings import UserSettings
from .dialogs.general_info_dialog import GeneralInfoDialog
from .dialogs.basic_parcels_wizard import BasicParcelsWizard
from .dialogs.main_parcel_dialog import MainParcelDialog
from .dialogs.sides_definition_wizard import SidesDefinitionWizard
from .utils.number_format import string_to_float



def process_general_info_dialog(user_settings: UserSettings, general_info: GeneralInfoObject | None = None) -> GeneralInfoObject | None:

     general_info_dialog = GeneralInfoDialog(user_settings)
     
     accepted = general_info_dialog.exec_()
     if accepted:
          general_info = general_info_dialog.as_general_info_object()
          return general_info
     else:
          return None

def process_parcel_definition(iface, feature_list: list[FeatureContext]) -> tuple[BasicParcel, list[BasicParcel]] | None:

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

     parcels.remove(main_parcel)

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

          segments_layer = new_vector_layer(parcel.feature_context.layer, layer_name, [("id", "integer"), ("name", "string(5)"), ("side", "string(10)")])

          project.addMapLayer(segments_layer)

          geom = parcel.feature_context.feature.geometry()
          xy_points = geom.asMultiPolygon()[0][0]

          segments = []

          for point_1, point_2 in zip(xy_points, xy_points[1:]):

               new_id = segments_layer.featureCount()+1
               new_name = "S"+str(new_id)
               segment = segment_from_xypoints(segments_layer, (point_1, point_2), new_name)
               segment.feature_context.feature.setAttributes([new_id, new_name, "undefined"])
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

def get_parcel_confrontations(geometry: QgsGeometry, parcel_list: list[BasicParcel]) -> list[str]:

     confrontations = []

     for parcel in parcel_list:

          parcel_geom = parcel.feature_context.feature.geometry()
          intersection = geometry.intersection(parcel_geom)
          if not intersection.isEmpty() and intersection.length() > 0:
               confrontations.append(parcel.name)

     return confrontations
