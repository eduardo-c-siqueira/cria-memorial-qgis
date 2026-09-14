from .memorial_padrao_base import MemorialPadraoBase
from .full_parcel import FullParcel
from .basic_parcel import BasicParcel

class MemorialPadraoLoteamento(MemorialPadraoBase):
    
    def __init__(self, memorial_padrao_base: MemorialPadraoBase, main_parcel: FullParcel | None = None, other_parcels: list[BasicParcel] | None = None):
        super().__init__(memorial_padrao_base.general_info)
        self.main_parcel = main_parcel
        self.other_parcels = other_parcels

    def geraMemorial(self):

        self.main_parcel.define_confrontations(self.other_parcels)

        texto = (
            f"MEMORIAL DESCRITIVO DO {self.stamp} \n\n"
            f"Lote de terreno {self.main_parcel.name},{self.main_parcel.describe_block()} da planta {self.main_parcel.describe_site_plan()}, "
            f"localizado nesta capital, no bairro {self.main_parcel.district}, {self.main_parcel.describe_side_of_street()} {self.main_parcel.street.description},"
            f"{self.main_parcel.describe_property_number()} {self.main_parcel.describe_distance_to_corner()} esquina formada com a {self.main_parcel.corner_street.description}, "
            f"de forma {self.main_parcel.shape}, com área total de {self.main_parcel.area} metros quadrados, "
            "e com as seguintes medidas, características e confrontações do ponto de vista de quem da frente o observa: "
            f"{self.main_parcel.front.describe_front()}; "
            f"{self.main_parcel.left_side.describe_side()}; "
            f"{(self.main_parcel.back.describe_side() +";") if self.main_parcel.back is not None else ""} e, "
            f"{self.main_parcel.right_side.describe_side()}, fechando o perímetro. \n\n{self.main_parcel.print_property_identificer()}"
            f"\n\n{self.identificaArquitetx()}"
        )

        return texto