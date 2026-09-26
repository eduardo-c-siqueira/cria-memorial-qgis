from .street import Street

from .segment import Segment

class Side:
    def __init__(self, name, segments: list[Segment]):
        self.name = name
        self.segments = segments

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