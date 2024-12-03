# Description : Advent of Code 2024 - Day 3
# Écris une fonction qui trie une liste de prénoms par ordre alphabétique, mais ceux qui commencent par une voyelle doivent apparaître en premier.
# Exemple : ['alice', 'bob', 'eve', 'charlie'] donne ['alice', 'eve', 'bob', 'charlie'].

def sort_names(liste) -> list :
    voyelles = "aeiouy"
    liste_voyelles = []
    liste_consonnes = []

    for i in liste :
        if i[0] in voyelles :
            liste_voyelles.append(i)
            liste_voyelles.sort()
        else :
            liste_consonnes.append(i)
            liste_consonnes.sort()

    return liste_voyelles + liste_consonnes

print(sort_names(['alice', 'bob', 'eve', 'charlie'])) # ['alice', 'eve', 'bob', 'charlie']
print(sort_names(['alice', 'bob', 'eve', 'charlie', 'yves'])) # ['alice', 'eve', 'yves', 'bob', 'charlie']

# ----------------------------------------------------------------------------------------------------------------------
# Corrigé :
def sort_names(liste) -> list:
    voyelles = "aeiouy"
    liste_voyelles = [nom for nom in liste if nom[0].lower() in voyelles]
    liste_consonnes = [nom for nom in liste if nom[0].lower() not in voyelles]

    return sorted(liste_voyelles) + sorted(liste_consonnes)

print(sort_names(['alice', 'bob', 'eve', 'charlie']))  # ['alice', 'eve', 'bob', 'charlie']
print(sort_names(['alice', 'bob', 'eve', 'charlie', 'yves']))  # ['alice', 'eve', 'yves', 'bob', 'charlie']