# Description : Advent of code 2024 - Day 8
# Crée une liste de dictionnaires à partir d'un fichier texte formaté comme un tableau CSV simple (colonnes séparées par des virgules).
# Exemple : "nom,age\nAlice,30\nBob,25\nCharlie,35" donne [{'nom': 'Alice', 'age': '30'}, {'nom': 'Bob', 'age': '25'}, {'nom': 'Charlie', 'age': '35'}].

def csv_to_dicts(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    return [dict(zip(lines[0].split(','), line.split(','))) for line in lines[1:]]

print(csv_to_dicts('data.csv')) # [{'nom': 'Alice', 'age': '30'}, {'nom': 'Bob', 'age': '25'}, {'nom': 'Charlie', 'age': '35'}]