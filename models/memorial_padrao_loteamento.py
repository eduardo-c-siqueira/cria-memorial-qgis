from .memorial_padrao_base import MemorialPadraoBase
from .full_parcel import FullParcel
from .basic_parcel import BasicParcel
from .data_classes import CreateMemorialResult, GeneralInfoObject
from .enums import SideEnum

class MemorialPadraoLoteamento(MemorialPadraoBase):
    
    def __init__(self, general_info: GeneralInfoObject, main_parcel: FullParcel | None = None, other_parcels: list[BasicParcel] | None = None):
        super().__init__(general_info)
        self.main_parcel = main_parcel
        self.other_parcels = other_parcels

    @property
    def body(self):
        return (
            f"Lote de terreno {self.main_parcel.name},{self.main_parcel.describe_block()}"
            f" da planta {self.main_parcel.site_plan_identification},"
            f" localizado nesta capital, no bairro {self.main_parcel.district},"
            f"{self.main_parcel.describe_side_of_street()} {self.main_parcel.street.description},"
            f"{self.main_parcel.describe_property_number()}{self.main_parcel.describe_distance_to_corner()}"
            f" esquina formada com a {self.main_parcel.corner_street.description},"
            f" de forma {self.main_parcel.shape}, com área total de {self.main_parcel.area} metros quadrados,"
            " e com as seguintes medidas, características e confrontações do ponto de vista de quem da frente o observa:"
            f"{self.describe_front(self.main_parcel.front.segments)};"
            f"{self.describe_side(SideEnum.LEFT, self.main_parcel.left_side.segments)};"
            f"{(self.describe_side(SideEnum.BACK, self.main_parcel.back.segments) +";") if self.main_parcel.back is not None else ""} e,"
            f"{self.describe_side(SideEnum.RIGHT, self.main_parcel.right_side.segments)},"
            f" fechando o perímetro. \n\n{self.main_parcel.print_property_identifier()}"
        )

    #TODO: considerar elevar para classes mãe
    def generate_memorial(self):

        self.main_parcel.define_confrontations(self.other_parcels)

        full_text = f"{self.heading}\n\n {self.body}\n\n{self.architect_identification}"

        return (full_text, CreateMemorialResult(self.heading, self.body, self.architect_identification))
