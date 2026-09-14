from .complements import Street, Front, Side
from .segment import Segment
from .data_classes import FeatureContext
from ..utils.string_format import float_to_string, check_plural
from .basic_parcel import BasicParcel

class FullParcel(BasicParcel):

    def __init__(
            self,
            base_parcel: BasicParcel, 
            district: str = "", 
            side_of_the_street: str = "", 
            street: Street | None = None, 
            number: str = "", 
            shape: str = "", 
            distance_to_corner: float = 0, 
            corner_street: Street | None = None, 
            property_identifier: str = "",
            ):
        
        super().__init__(base_parcel.name, base_parcel.block, base_parcel.site_plan_name, base_parcel.site_plan_code, base_parcel.feature_context)
        self.district = district
        self.side_of_the_street = side_of_the_street.lower()
        self.street = street 
        self.number = number
        self.shape = shape.lower()
        self.distance_to_corner = distance_to_corner
        self.corner_street = corner_street
        self.property_identifier = property_identifier

    def describe_side_of_street(self):
        if self.side_of_the_street:
            return f"no lado {self.side_of_the_street} da"
        else:
            return "na"

    def describe_property_number(self):
        if self.number:
            return f" número {self.number},"
        else:
            return ""

    def describe_distance_to_corner(self):
        if self.distance_to_corner != 0.00:
            return f"a {float_to_string(self.distance_to_corner)} metro{check_plural(self.distance_to_corner > 1)} da"
        else:
            return "na"

    def print_property_identificer(self):
        if self.property_identifier is not None and self.property_identifier.strip() != "":
            return f" Indicação fiscal {self.property_identifier}."
        else:
            return ""

    def define_sides(self, front: list[Segment], left: list[Segment], right: list[Segment], back: list[Segment] | None = None):

        #TODO: resolver caso de street undefined
        self.front = Front("frente", front, self.street)
        self.left_side = Side("esquerdo", left)
        self.right_side = Side("direito", right)
        self.back = Side("fundos", back) if back is not None else None

    def define_confrontations(self, other_parcels: list[BasicParcel]):
    
        for segment in self.front.segments:
            segment.define_confrontations(other_parcels)
            self.front.adjust_confrontations()
        for segment in self.right_side.segments:
            segment.define_confrontations(other_parcels)
        for segment in self.left_side.segments:
            segment.define_confrontations(other_parcels)
        if self.back:
            for segment in self.back.segments:
                segment.define_confrontations(other_parcels)

    @property
    def area(self):
        return float_to_string(self.feature_context.feature.geometry().area())