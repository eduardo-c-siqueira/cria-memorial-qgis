from .data_classes import FeatureContext

class BasicParcel:

    def __init__(self, name: str, block: str, site_plan_name: str, site_plan_code: str | None, feature_context: FeatureContext):
        self.name = name
        self.block = block
        self.site_plan_name = site_plan_name
        self.site_plan_code = site_plan_code
        self.feature_context = feature_context

    def describe_block(self):
        if self.block is not None and self.block.strip() != "":
            return f" da quadra {self.block},"
        else:
            return ""

    @property
    def site_plan_identification(self):
        if self.site_plan_code and self.site_plan_code.strip() != "":
            return f"{self.site_plan_name} ({self.site_plan_code})"
        else:
            return self.site_plan_name