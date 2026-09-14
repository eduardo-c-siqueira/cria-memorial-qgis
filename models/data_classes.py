from dataclasses import dataclass
from qgis.core import QgsVectorLayer, QgsFeature

@dataclass
class GeneralInfoObject:

    stamp: str
    architect: str
    architect_gender: str
    cau_code: str

@dataclass
class FeatureContext:
    layer: QgsVectorLayer
    feature: QgsFeature

@dataclass
class MainParcelDialogResult:
    district: str
    street_side: str
    main_street_name: str
    main_street_code: str
    number: str
    shape: str
    distance_to_corner: str
    cross_street_name: str
    cross_street_code: str
    property_identifier: str

@dataclass
class SidesWidgetResult:
    front: list
    left: list
    right: list
    back: list | None = None