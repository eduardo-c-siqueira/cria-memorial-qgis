from enum import StrEnum

class Gender(StrEnum):

    MALE = "&Masculino"
    FEMALE = "&Feminino"
    DEFAULT = ""

class DocumentFormat(StrEnum):

    DOCX = ".docx"
    PDF = ".pdf"
    IMAGE = "image"
    DEFAULT = DOCX

    @property
    def filter(self):
        return {
            DocumentFormat.DOCX: "Documentos Word 2007+ (*.docx)",
            DocumentFormat.PDF: "PDF (*.pdf)",
            DocumentFormat.IMAGE: "Imagem (*.jpg *.jpeg *.png *.JPG *.JPEG *.PNG)"
        }[self]

class SideEnum(StrEnum):

    FRONT = "frente"
    LEFT = "esquerdo"
    RIGHT = "direito"
    BACK = "fundos"

    def begin_description(self):
        return {
            SideEnum.LEFT: f" pelo lado {self.value},",
            SideEnum.RIGHT: f" pelo lado {self.value},",
            SideEnum.BACK: " pela linha dos fundos,",
        }[self]