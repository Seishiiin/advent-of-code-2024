# Description : Advent of Code 2024 - Day 2
# Crée une fonction qui compte le nombre d'occurrences de chaque mot dans un texte donné.
# Exemple, "hello world hello" donne {'hello': 2, 'world': 1}.

def count_words(texte) -> dict :
    mots = texte.split()
    occurrence = {}

    for i in mots :
        if i in occurrence :
            occurrence[i] += 1
        else :
            occurrence[i] = 1

    return occurrence

print(count_words("hello world hello")) # {'hello': 2, 'world': 1}
print(count_words("hello world hello world")) # {'hello': 2, 'world': 2}