# Description : Advent of Code 2024 - Day 1
# Écris une fonction qui prend une liste de nombres et retourne la somme cumulée.
# Exemple : [1, 2, 3] donne [1, 3, 6].

def sum_list(liste) -> list:
    somme = 0
    return [somme := somme + i for i in liste]

print(sum_list([1, 2, 3]))  # [1, 3, 6]
print(sum_list([1, 2, 3, 4]))  # [1, 3, 6, 10]