from .complements import Street, Front, Side
from .data_classes import FeatureContext

from .basic_parcel import BasicParcel

class FullParcel(BasicParcel):

    def __init__(self, name: str, block: str, site_plan_name: str, site_plan_code: str, qgs_feature: FeatureContext, district: str, side_of_the_street: str, 
                street: Street, number: str, shape: str, distance_to_corner: str, corner_street: Street, area: str, property_identifier: str, front: Front,
                front_is_street: bool, sides: list[Side]):
        
        super().__init__(name, block, site_plan_name, site_plan_code, qgs_feature)
        self.district = district
        self.side_of_the_street = side_of_the_street
        self.street = street 
        self.number = number
        self.shape = shape
        self.distance_to_corner = distance_to_corner
        self.corner_street = corner_street
        self.area = area
        self.property_identifier = property_identifier
        self.front = front
        self.front_is_street = front_is_street
        self.lado1 = sides[0]
        self.lado2 = sides[1]
        self.lado3 = sides[2] or None

    def describe_side_of_street(self):
        if self.side_of_the_street and self.side_of_the_street.strip() is not "":
            return f"no lado ${self.side_of_the_street} da"
        else:
            return "na"

    def describe_property_number(self):
        if self.number and self.number.strip() is not "":
            return f" número {self.number},"
        else:
            return ""

    def describe_distance_to_corner(self):
        if self.distance_to_corner is not "0,00":
            return f"a {self.distance_to_corner} metros da"
        else:
            return "na"

    def print_property_identificer(self):
        if self.property_identifier and self.property_identifier.strip() is not "":
            return f" Indicação fiscal ${self.property_identifier}."
        else:
            return ""