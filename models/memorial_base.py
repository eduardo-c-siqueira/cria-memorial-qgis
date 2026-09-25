from abc import ABC, abstractmethod

from .data_classes import GeneralInfoObject
from .enums import Gender

class MemorialBase(ABC):

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
    @abstractmethod
    def body(self):
        pass

    @property
    def architect_identification(self):

        x = "x"

        if self.architect_gender == Gender.MALE:
            x = "o"
        elif self.architect_gender == Gender.FEMALE:
            x = "a"

        return f"Arquitet{x} {self.architect}\nCAU {self.cau_code}"

    @abstractmethod
    def generate_memorial(self):
        pass