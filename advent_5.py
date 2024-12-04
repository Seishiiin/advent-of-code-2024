# Description : Advent of Code 2024 - Day 5
# Prends une liste de chaînes et retourne une nouvelle liste où chaque chaîne est inversée.
# Exemple : ["abc", "def"] donne ["cba", "fed"].

def reverse_string_in_list(liste) -> list:
    return [i[::-1] for i in liste]

print(reverse_string_in_list(["abc", "def"]))  # ['cba', 'fed']
print(reverse_string_in_list(["abc", "def", "ghi"]))  # ['cba', 'fed', 'ihg']