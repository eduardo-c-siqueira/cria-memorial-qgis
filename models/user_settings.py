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