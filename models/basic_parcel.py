from .data_classes import FeatureContext

class BasicParcel:

    def __init__(self, name: str, block: str, site_plan_name: str, site_plan_code: str, feature_context: FeatureContext):
        self.name = name
        self.block = block
        self.site_plan_name = site_plan_name
        self.site_plan_code = site_plan_code or ""
        self.feature_context = feature_context

    def describe_block(self):
        if self.block and self.block.strip() is not "":
            return f" da quadra {self.block},"
        else:
            return ""


    def describe_site_plan(self):
        if self.site_plan_code and self.site_plan_code.strip() is not "":
            return f"{self.site_plan_name} {self.site_plan_code}"
        else:
            return self.site_plan_name