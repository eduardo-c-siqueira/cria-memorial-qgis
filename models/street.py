from ..utils.string_format import format_name

class Street:
    def __init__(self, name: str, code: str | None = None):
        self.name = format_name(name)
        self.code = code
        if self.code and self.code.strip() != "":
            self.description = f"{self.name} ({self.code})"
        else:
            self.description = self.name