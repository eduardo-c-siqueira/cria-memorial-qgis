from ..utils.string_format import number_in_full, format_name, segment_ordinal

class Street:
    def __init__(self, name, code):
        self.name = format_name(name)
        self.code = code
        if self.code and self.code.strip() is not "":
            self.description = f"{self.name} ({self.code})"
        else:
            self.description = self.name

class Segment:
    def __init__(self, index:int, measure, confrontations):
        self.ordinal = segment_ordinal(index)
        self.measure = measure
        self.confrontations = confrontations

    def list_confrontations(self):
        if self.confrontations and self.confrontations.strip() is not "":
            return f" e confronta com {self.confrontations}`"
        else:
            return ""

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
            return f"{start} apresenta {self.segments[0].measure} metros{self.segments[0].list_confrontations()}"
        else:
            segment_descriptions = []
            for s in self.segments:
                segment_descriptions.append(f"`o {s.ordinal} segmento apresenta {s.measure} metros{s.list_confrontations()}")
                return f"`{start} apresenta {number_in_full(len(self.segments))} segmentos: {", ".join(segment_descriptions)}`"

class Front (Side):

    def __init__(self, name, segments: list[Segment], street: Street):

        super().__init__(name, segments)
        self.street = street

    def describe_front(self):
        if len(self.segments) == 1:
            return f"`apresenta {self.segments[0].measure} metros de frente para a {self.street.description}{self.segments[0].list_confrontations()}"
        else:
            segment_descriptions = []
            for s in self.segments:
                segment_descriptions.append(f"o {s.ordinal} segmento apresenta {s.measure} metros{s.list_confrontations()}")
            return f"`apresenta {number_in_full(len(self.segments))} segmentos de frente para a {self.street.description}: {", ".join(segment_descriptions)}"