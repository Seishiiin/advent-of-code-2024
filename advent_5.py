# Description : Advent of Code 2024 - Day 5
# Prends une liste de chaînes et retourne une nouvelle liste où chaque chaîne est inversée.
# Exemple : ["abc", "def"] donne ["cba", "fed"].

def reverse_string_in_list(liste) -> list:
    liste_reverse = []

    for i in liste:
        liste_reverse.append(i[::-1])

    return liste_reverse

print(reverse_string_in_list(["abc", "def"]))  # ['cba', 'fed']
print(reverse_string_in_list(["abc", "def", "ghi"]))  # ['cba', 'fed', 'ihg']

# ----------------------------------------------------------------------------------------------------------------------
# Corrigé :
def reverse_string_in_list(liste) -> list:
    return [i[::-1] for i in liste]

print(reverse_string_in_list(["abc", "def"]))  # ['cba', 'fed']
print(reverse_string_in_list(["abc", "def", "ghi"]))  # ['cba', 'fed', 'ihg']