from qgis.core import QgsPoint, QgsGeometry

from .memorial_base import MemorialBase
from .data_classes import FeatureContext, GeneralInfoObject
from .full_parcel import FullParcel
from .basic_parcel import BasicParcel
from .segment import Segment
from ..utils import string_format
import qgs_processing
import processing

class MemorialXYBase(MemorialBase):
# Classe abstrata para subespecialização (diferencia entre memorial padrão e memorial coordenadas)
    def __init__(self, general_info: GeneralInfoObject):
        super().__init__(general_info)
        self.main_parcel: FullParcel = None
        self.other_parcels: list[BasicParcel] = None


    def describe_all_segments(self) -> str:

        points = self.main_parcel.ordered_qgs_points
        descriptions = []

        for index, (point_1, point_2) in enumerate(zip(points, points[1:] + points[:1])):

            line_geom = QgsGeometry.fromPolyline([point_1, point_2])
            measure = line_geom.length()

            if point_1 == points[0]:

                descriptions.append((
                    f" partindo no ponto P0PP (coordenadas N: {point_1.y()} e E: {point_1.x()})"
                    f" até o ponto P01 (coordenadas N: {point_2.y()} e E: {point_2.x()})"
                    f" apresenta {string_format.float_to_string_2f(measure)} metro{string_format.check_plural(measure > 1)}"
                    f" de frente para a {self.main_parcel.street.description}."
                ))

            else:

                confrontations = processing.get_parcel_confrontations(line_geom, self.other_parcels)

                #TODO: eliminar caso a alternativa funcione
                # for parcel in self.other_parcels:

                #     parcel_geom = parcel.feature_context.feature.geometry()
                #     intersection = line_geom.intersection(parcel_geom)
                #     if not intersection.isEmpty() and intersection.length() > 0:
                #         confrontations.append(parcel.name)

                confrontations_description = f" e confronta com {", ".join(confrontations)}" if confrontations  else ""

                if point_2 == points[0]:

                    descriptions.append((
                        f" e do ponto P0{str(index)} até o ponto P0PP"
                        f" apresenta {string_format.float_to_string_2f(measure)} metro{string_format.check_plural(measure > 1)}"
                        f"{confrontations_description}"
                    ))
                    
                else:

                    descriptions.append((
                        f" do ponto P0{str(index)}"
                        f" até o ponto P0{str(index+1)} (coordenadas N: {point_2.y()} e E: {point_2.x()})"
                        f" apresenta {string_format.float_to_string_2f(measure)} metro{string_format.check_plural(measure > 1)}"
                        f"{confrontations_description}"
                    ))

        return "; ".join(descriptions)

    # def describe_front_with_coordinates(self, segment: Segment):

    #     #TODO: Perguntas:
    #     # - Frente será sempre 1 segmento apenas?
    #     return (
    #         f" partindo no ponto **nome_no_ponto_0 (coordenadas N: **n_coord_y e E: **e_coord_x)"
    #         f" até o ponto **nome_ponto_1 (coordenadas N: **n_coord_y e E: **e_coord_x)"
    #         f" apresenta {self.segments[0].describe_measure()} de frente para a {self.street.description}"
    #     )

    # def describe_side_with_coordinates(self, show_xy_2: bool = False, show_xy_1: bool = False):
    #     return f"do ponto **ponto_1 **coord_1_if até o ponto **ponto_2 **coord_2_if apresenta **medida_total? metros e **confrontações"
