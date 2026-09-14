from ..utils.string_format import number_in_full, format_name, segment_ordinal, check_plural
from ..models.segment import Segment

class Street:
    def __init__(self, name: str, code: str | None = None):
        self.name = format_name(name)
        self.code = code
        if self.code is not None and self.code.strip() != "":
            self.description = f"{self.name} ({self.code})"
        else:
            self.description = self.name

#TODO: implementar forma de lidar com confrontações idênticas

class Side:
    def __init__(self, name, segments: list[Segment]):
        self.name = name    
        self.segments = segments

    def describe_side(self):
        start = ""

        if self.name == "fundos":
            start = "pela linha dos fundos,"
        else:
            start = f"pelo lado {self.name},"

        if len(self.segments) == 1:
            return f"{start} apresenta {self.segments[0].describe_measure()}{self.segments[0].list_confrontations()}"
        else:
            segment_descriptions = []
            for index, s in enumerate(self.segments):
                segment_descriptions.append(f"o {segment_ordinal(index)} segmento apresenta {s.describe_measure()}{s.list_confrontations()}")
            return f"{start} apresenta {number_in_full(len(self.segments))} segmentos: {", ".join(segment_descriptions)}"

#TODO: Consertar a forma de criar e descrever a rua com base na confrontação do segmento
class Front (Side):

    def __init__(self, name, segments: list[Segment], street: Street | None = None):

        super().__init__(name, segments)
        self.street = street

    def adjust_confrontations(self):
        if self.street is None and self.segments[0].street_confrontations:
                    first_street_confrontation = self.segments[0].street_confrontations[0]
                    self.street = Street(first_street_confrontation)
                    self.segments[0].street_confrontations.remove(first_street_confrontation)
        
        if self.segments[0].street_confrontations:
            street_repeated = next((street for street in self.segments[0].street_confrontations if street == self.street.description), None)
            if street_repeated:
                self.segments[0].street_confrontations.remove(street_repeated)

    def describe_front(self):

        if len(self.segments) == 1:
            return f"apresenta {self.segments[0].describe_measure()} de frente para a {self.street.description}{self.segments[0].list_confrontations()}"
        else:
            segment_descriptions = []
            for index, s in enumerate(self.segments):
                segment_descriptions.append(f"o {segment_ordinal(index)} segmento apresenta {s.describe_measure()}{s.list_confrontations()}")
            return f"apresenta {number_in_full(len(self.segments))} segmentos de frente para a {self.street.description}: {", ".join(segment_descriptions)}"