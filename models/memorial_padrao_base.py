from .data_classes import GeneralInfoObject

class MemorialPadraoBase:

    def __init__(self, general_info: GeneralInfoObject):
        self.general_info = general_info
        self.stamp = self.general_info.stamp
        self.architect = self.general_info.architect
        self.architect_gender = self.general_info.architect_gender
        self.cau_code = self.general_info.cau_code

    def identificaArquitetx(self):
        x = "x"
        if self.architect_gender == "Masculino":
            x = "o"
        elif self.architect_gender == "Feminino":
            x = "a"

        return f"Arquitet{x} {self.architect} CAU {self.cau_code}"