# Description : Advent of Code 2024 - Day 3
# Écris une fonction qui trie une liste de prénoms par ordre alphabétique, mais ceux qui commencent par une voyelle doivent apparaître en premier.
# Exemple : ['alice', 'bob', 'eve', 'charlie'] donne ['alice', 'eve', 'bob', 'charlie'].

def sort_names(liste) -> list:
    liste_voyelles = [nom for nom in liste if nom[0].lower() in "aeiouy"]
    liste_consonnes = [nom for nom in liste if nom[0].lower() not in "aeiouy"]

    return sorted(liste_voyelles) + sorted(liste_consonnes)

print(sort_names(['alice', 'bob', 'eve', 'charlie']))  # ['alice', 'eve', 'bob', 'charlie']
print(sort_names(['alice', 'bob', 'eve', 'charlie', 'yves']))  # ['alice', 'eve', 'yves', 'bob', 'charlie']