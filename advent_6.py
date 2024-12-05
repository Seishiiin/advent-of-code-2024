# Description : Advent of Code 2020 - Day 6
# Trouve toutes les paires d'éléments dans une liste qui, additionnés, donnent une somme spécifique.
# [1, 2, 3, 4, 5, -1] et 4 => (1, 3), (2, 2), (3, 1), (-1, 5)

def find_pair_oneline(liste, somme) -> list :
    return [f"({i}, {somme-i})" for i in liste if somme - i in liste]

print(find_pair_oneline([1, 2, 3, 4, 5, -1], 4)) # => [(1, 3), (2, 2), (3, 1), (-1, 5)]
print(find_pair_oneline([1, 2, 3, 4, 5, -1], 5)) # => [(1, 4), (2, 3), (3, 2), (4, 1), (-1, 6)]