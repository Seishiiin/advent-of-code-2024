# Description : Advent of Code 2024 - Day 4
# Génère une table de multiplication pour un nombre donné
# Exemple : 3 donne : 1 x 3 = 3, 2 x 3 = 6, 3 x 3 = 9, 4 x 3 = 12, 5 x 3 = 15, 6 x 3 = 18, 7 x 3 = 21, 8 x 3 = 24, 9 x 3 = 27, 10 x 3 = 30.

def table_multiplication(x) -> list:
    return [f"{i} x {x} = {i * x}" for i in range(1, 11)]

print(table_multiplication(3)) # ['1 x 3 = 3', '2 x 3 = 6', '3 x 3 = 9', '4 x 3 = 12', '5 x 3 = 15', '6 x 3 = 18', '7 x 3 = 21', '8 x 3 = 24', '9 x 3 = 27', '10 x 3 = 30']
print(table_multiplication(5)) # ['1 x 5 = 5', '2 x 5 = 10', '3 x 5 = 15', '4 x 5 = 20', '5 x 5 = 25', '6 x 5 = 30', '7 x 5 = 35', '8 x 5 = 40', '9 x 5 = 45', '10 x 5 = 50']

# ----------------------------------------------------------------------------------------------------------------------
# Corrigé :
def table_multiplication(x, n=10) -> list:
    return [f"{i} x {x} = {i * x}" for i in range(1, n + 1)]

print(table_multiplication(3))  # Par défaut, 1 à 10
print(table_multiplication(3, 15))  # De 1 à 15
