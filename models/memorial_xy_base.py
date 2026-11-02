from qgis.core import QgsGeometry, QgsPointXY

from .memorial_base import MemorialBase
from .data_classes import GeneralInfoObject
from .full_parcel import FullParcel
from .basic_parcel import BasicParcel
from ..utils import string_format

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

            line_geom = QgsGeometry.fromPolylineXY([point_1, point_2])
            measure = line_geom.length()

            if point_1 == points[0]:

                descriptions.append((
                    f" partindo no ponto P0PP ({describe_coordinates(point_1)})"
                    f" até o ponto P01 ({describe_coordinates(point_2)})"
                    f" apresenta {string_format.float_to_string_2f(measure)} metro{string_format.check_plural(measure > 1)}"
                    f" de frente para a {self.main_parcel.street.description}"
                ))

            else:

                confrontations = [
                    parcel.name
                    for parcel in self.other_parcels
                    if parcel.confronts_with(line_geom)
                ]

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
                        f" até o ponto P0{str(index+1)} ({describe_coordinates(point_2)})"
                        f" apresenta {string_format.float_to_string_2f(measure)} metro{string_format.check_plural(measure > 1)}"
                        f"{confrontations_description}"
                    ))

        return "; ".join(descriptions)


def describe_coordinates(point: QgsPointXY) -> str:

    def format_coordinate(value: float) -> str:
        return string_format.float_to_string_2f(
            string_format.apply_thousands_separator(value)
        )

    northing = format_coordinate(point.y())
    easting = format_coordinate(point.x())

    return f"coordenadas N: {northing} e E: {easting}"