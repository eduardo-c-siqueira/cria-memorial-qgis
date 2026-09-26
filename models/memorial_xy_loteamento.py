from .memorial_xy_base import MemorialXYBase
from .full_parcel import FullParcel
from .basic_parcel import BasicParcel
from .data_classes import CreateMemorialResult, GeneralInfoObject

class MemorialXYLoteamento(MemorialXYBase):
    
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
            f" de forma {self.main_parcel.shape}"
            " e com as seguintes medidas, características e confrontações do ponto de vista de quem da frente o observa:"
            f"{self.describe_all_segments()}"
            f" fechando o perímetro e perfazen a área total de {self.main_parcel.area} m²."
            f"\n\n{self.main_parcel.print_property_identifier()}"
        )

    def generate_memorial(self):

        full_text = f"{self.heading}\n\n {self.body}\n\n{self.architect_identification}"

        return (full_text, CreateMemorialResult(self.heading, self.body, self.architect_identification))