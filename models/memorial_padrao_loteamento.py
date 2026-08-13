from .memorial_padrao_base import MemorialPadraoBase
from .full_parcel import FullParcel

class MemorialPadraoLoteamento(MemorialPadraoBase):
  def __init__(self, titulo_carimbo, arquitetx, genero_arquitetx, cau, lote: FullParcel):
      super().__init__(titulo_carimbo, arquitetx, genero_arquitetx, cau)
      self.lote = lote

  def geraMemorial(self):

      texto = f"""
      MEMORIAL DESCRITIVO DO {self.titulo_carimbo}
      Lote de terreno {self.lote.name},{self.lote.describe_block()} da planta {self.lote.describe_site_plan()},
      localizado nesta capital, no bairro {self.lote.district}, {self.lote.describe_side_of_street()} {self.lote.street.description},
      {self.lote.describe_property_number()} {self.lote.describe_distance_to_corner()} esquina formada com a {self.lote.corner_street.description},
      de forma {self.lote.shape}, com área total de {self.lote.area} metros quadrados, e com as seguintes medidas, características e confrontações do ponto de vista de quem da frente o observa:
      {self.lote.front.describe_front()};
      {self.lote.lado1.describe_side()};
      {self.lote.lado2.describe_side()}; e,
      {self.lote.lado3.describe_side()}, fechando o perímetro. {self.lote.print_property_identificer()}
      {self.identificaArquitetx()}"""

      return texto