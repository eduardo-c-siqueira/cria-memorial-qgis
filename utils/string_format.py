def format_name(nome: str):
    prepositions = ['de', 'do', 'da', 'dos', 'das', 'e']
    word_list = nome.lower().split()
    processed_word_list = []
    for index, p in enumerate(word_list):
        if p in prepositions and index != 0:
            processed_word_list.append(p)
        else:
            processed_word_list.append(p.capitalize())
    return " ".join(processed_word_list)

def number_in_full(num):
    numbers_in_full = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quartoze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte"]
    return numbers_in_full[num]

def segment_ordinal(index: int):
    #the parameter should be the index of the segment in the list, so that 0 would be first, 1 - second, and so on
    ordinals = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto', 'sétimo', 'oitavo', 'nono', 'décimo']
    return ordinals[index]

def float_to_string_2f(num: float) -> str:
    return f"{num:.2f}".replace(".",",")

def float_to_string_4f(num: float) -> str:
    return f"{num:.4f}".replace(".",",")

def apply_thousands_separator(num: str) -> str:

    integer_str, separator, decimals = num.partition(",")
    
    sign = ""
    if integer_str.startswith(("-", "+")):
        sign, integer_str = integer_str[0], integer_str[1:]

    groups = []
    while integer_str:
        groups.append(integer_str[-3:])
        integer_str = integer_str[:-3]

    result = ".".join(reversed(groups))

    return sign + result + separator + decimals

def check_plural(condition: bool):
    return "s" if condition else ""