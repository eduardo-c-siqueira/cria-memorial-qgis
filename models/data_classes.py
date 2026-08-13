from dataclasses import dataclass
from qgis.core import QgsVectorLayer, QgsFeature

@dataclass
class GeneralInfoObject:

    stamp: str
    arquitect: str
    arquitect_gender: str
    cau_code: str
    block: str
    site_plan: str
    site_plan_code: str
    district: str
    property_identifier: str

@dataclass
class FeatureContext:
    layer: QgsVectorLayer
    feature: QgsFeature

@dataclass
class MainParcelDialogResult:
    street_side: str
    main_street_name: str
    main_street_code: str
    number: str
    shape: str
    distance_to_corner: str
    cross_street_name: str
    cross_street_code: str
    property_identifier: str