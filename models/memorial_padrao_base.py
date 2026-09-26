from .memorial_base import MemorialBase
from .data_classes import GeneralInfoObject
from .full_parcel import FullParcel
from .basic_parcel import BasicParcel
from .segment import Segment
from .enums import SideEnum
from ..utils import string_format


class MemorialPadraoBase(MemorialBase):
# Classe abstrata para subespecialização (diferencia entre memorial padrão e memorial coordenadas)
    def __init__(self, general_info: GeneralInfoObject):
        super().__init__(general_info)
        self.main_parcel: FullParcel = None
        self.other_parcels: list[BasicParcel] = None

    #TODO: Consertar a forma de criar e descrever a rua com base na confrontação do segmento
    def describe_front(self, segments: list[Segment]):

        if len(segments) == 1:
            #TODO: colocar aqui a remoção da primeira street_confrontation
            return f" apresenta {segments[0].describe_measure()} de frente para a {self.main_parcel.street.description}{segments[0].list_confrontations()}"

        else:
            return f" apresenta {string_format.number_in_full(len(segments))} segmentos de frente para a {self.main_parcel.street.description}:{self.describe_segments_on_side(segments)}"

    def describe_side(self, side_position: SideEnum, segments: list[Segment]):

        if len(segments) == 1:
            return f"{side_position.begin_description()} apresenta {segments[0].describe_measure()}{segments[0].list_confrontations()}"

        else:
            return f"{side_position.begin_description()} apresenta {string_format.number_in_full(len(segments))} segmentos:{self.describe_segments_on_side(segments)}"

    #TODO: implementar forma de lidar com confrontações idênticas
    def describe_segments_on_side(self, segments: list[Segment]):

        description_list = [
            f" o {string_format.segment_ordinal(index)} segmento apresenta {segment.describe_measure()}{segment.list_confrontations()}" 
            for index, segment 
            in enumerate(segments)
        ]

        return ", ".join(description_list)