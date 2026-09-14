from ..utils.string_format import float_to_string, check_plural
from .basic_parcel import BasicParcel
from .data_classes import FeatureContext

class Segment:
    def __init__(self, name, feature_context: FeatureContext):
        self.name = name
        self.feature_context = feature_context
        self.street_confrontations = None
        self.confrontations = []

    def define_confrontations(self, other_parcels: list[BasicParcel]):

        if self.street_confrontations:
            self.confrontations = self.street_confrontations 
        else: 
            self.confrontations = []

        for parcel in other_parcels:
            parcel_geom = parcel.feature_context.feature.geometry()
            self_geom = self.feature_context.feature.geometry()
            intersection = self_geom.intersection(parcel_geom)
            if not intersection.isEmpty() and intersection.length() > 0:
                self.confrontations.append(parcel.name)

    def list_confrontations(self):
        if self.confrontations:
            return f" e confronta com {", ".join(self.confrontations)}"
        else:
            return ""

    def set_street_confrontations(self, streets: list[str]):
        self.street_confrontations = streets

    def describe_measure(self):
        return f"{self.measure_str} metro{check_plural(self.measure_flt > 1)}"

    @property
    def measure_flt(self) -> float:
        return self.feature_context.feature.geometry().length()
    @property
    def measure_str(self) -> str:
        return float_to_string(self.measure_flt)