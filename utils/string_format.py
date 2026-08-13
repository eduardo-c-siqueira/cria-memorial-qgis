def format_name(nome: str):
    prepositions = ['de', 'do', 'da', 'dos', 'das', 'e']
    word_list = nome.lower().split()
    processed_word_list = []
    for index, p in enumerate(word_list):
        if p in prepositions and index is not 0:
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