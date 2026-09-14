def string_to_float(text:str) -> float:
    if text.count(",") > 1:
        raise NotImplementedError
    else:
        formatted_text = text.replace(",",".")
        return float(formatted_text)
