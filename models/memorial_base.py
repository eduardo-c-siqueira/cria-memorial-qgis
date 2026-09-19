from .data_classes import GeneralInfoObject

class MemorialBase:

    def __init__(self, general_info: GeneralInfoObject):
        self.general_info = general_info
        self.stamp = self.general_info.stamp
        self.architect = self.general_info.architect
        self.architect_gender = self.general_info.architect_gender
        self.cau_code = self.general_info.cau_code

    @property
    def heading(self):
        return f"MEMORIAL DESCRITIVO DO {self.stamp}"

    @property
    def architect_identification(self):

        x = "x"

        if self.architect_gender == "Masculino":
            x = "o"
        elif self.architect_gender == "Feminino":
            x = "a"

        return f"Arquitet{x} {self.architect}\nCAU {self.cau_code}"