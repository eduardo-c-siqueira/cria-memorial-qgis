from qgis.PyQt.QtCore import QSettings

from .enums import Gender, DocumentFormat

class UserSettings:

    def __init__(self):
        self.settings = QSettings("EduardoCSiqueiraDev", "Cria Memorial")

    # preferencia de formato saida
    @property
    def output_doc_format_preference(self):
        return DocumentFormat(self.settings.value("preferences/output_format", DocumentFormat.DEFAULT.value))

    @output_doc_format_preference.setter
    def output_doc_format_preference(self, format: DocumentFormat):
        self.settings.setValue("preferences/output_format", format.value)

    # caminho do template docx
    @property
    def docx_template_path(self):
        return self.settings.value("paths/docx_template", "")

    @docx_template_path.setter
    def docx_template_path(self, value: str):
        self.settings.setValue("paths/docx_template", value)

    # caminho da logo da autarquia
    @property
    def atc_logo_path(self):
        return self.settings.value("paths/atc_logo", "")

    @atc_logo_path.setter
    def atc_logo_path(self, value: str):
        self.settings.setValue("paths/atc_logo", value)

    # caminho da logo principal
    @property
    def main_logo_path(self):
        return self.settings.value("paths/main_logo", "")

    @main_logo_path.setter
    def main_logo_path(self, value: str):
        self.settings.setValue("paths/main_logo", value)
    
    # texto do cabeçalho para pdf
    @property
    def pdf_header_textlines(self) -> list[str]:
        return self.settings.value("pdf_header/textlines", ['','','','','','','',''])

    @pdf_header_textlines.setter
    def pdf_header_textlines(self, value: list[str]):
        self.settings.setValue("pdf_header/textlines", value)

    # último nome de arquitetx preenchido 
    @property
    def last_architect_name(self):
        return self.settings.value("last_used/architect_name", "")

    @last_architect_name.setter
    def last_architect_name(self, value: str):
        self.settings.setValue("last_used/architect_name", value)

    # último gênero de arquitetx selecionado
    @property
    def last_architect_gender(self):
        return Gender(self.settings.value("last_used/architect_gender", Gender.DEFAULT.value))
    
    @last_architect_gender.setter
    def last_architect_gender(self, gender: Gender):
        self.settings.setValue("last_used/architect_gender", gender.value)

    # último valor preenchido para CAU
    @property
    def last_cau_code(self):
        return self.settings.value("last_used/cau_code", "")

    @last_cau_code.setter
    def last_cau_code(self, value: str):
        self.settings.setValue("last_used/cau_code", value)

    # último valor preenchido para Quadra
    @property
    def last_block(self) -> str:
        return self.settings.value("last_used/block", "")

    def set_last_block(self, value: str):
        self.settings.setValue("last_used/block", value)

    @property
    def recycle_block(self):
        return self.settings.value("recycling/block", False, bool)

    @recycle_block.setter
    def recycle_block(self, value: bool):
        self.settings.setValue("recycling/block", value)

    # último valor preenchido para Planta
    @property
    def last_site_plan(self) -> tuple[str, str]:
        return self.settings.value("last_used/site_plan", ""), self.settings.value("last_used/site_plan_code", "")

    def set_last_site_plan(self, site_plan: str, code: str):
        self.settings.setValue("last_used/site_plan", site_plan)
        self.settings.setValue("last_used/site_plan_code", code)

    @property
    def recycle_site_plan(self):
        return self.settings.value("recycling/site_plan", False, bool)

    @recycle_site_plan.setter
    def recycle_site_plan(self, value: bool):
        self.settings.setValue("recycling/site_plan", value)

    # último valor preenchido para Rua
    @property
    def last_street(self) -> tuple[str, str]:
        return self.settings.value("last_used/street", ""), self.settings.value("last_used/street_code", "")

    def set_last_street(self, street: str, code: str):
        self.settings.setValue("last_used/street", street)
        self.settings.setValue("last_used/street_code", code)

    @property
    def recycle_street(self):
        return self.settings.value("recycling/street", False, bool)

    @recycle_street.setter
    def recycle_street(self, value: bool):
        self.settings.setValue("recycling/street", value)

    # último valor preenchido para Bairro
    @property
    def last_district(self) -> str:
        return self.settings.value("last_used/district", "")

    def set_last_district(self, value: str):
        self.settings.setValue("last_used/district", value)

    @property
    def recycle_district(self):
        return self.settings.value("recycling/district", False, bool)

    @recycle_district.setter
    def recycle_district(self, value: bool):
        self.settings.setValue("recycling/district", value)

    # último valor preenchido para Rua da Esquina
    @property
    def last_corner_street(self) -> tuple[str, str]:
        return self.settings.value("last_used/corner_street", ""), self.settings.value("last_used/corner_street_code", "")

    def set_last_corner_street(self, street: str, code: str):
        self.settings.setValue("last_used/corner_street", street)
        self.settings.setValue("last_used/corner_street_code", code)
        
    @property
    def recycle_corner_street(self):
        return self.settings.value("recycling/corner_street", False, bool)

    @recycle_corner_street.setter
    def recycle_corner_street(self, value: bool):
        self.settings.setValue("recycling/corner_street", value)
