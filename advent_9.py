# Description : Advent of Code 2024 - Day 9
# Écris un générateur de mots de passe aléatoires respectant certains critères : longueur minimale, majuscules, chiffres, caractères spéciaux.
# Exemple : generate_password(8, True, True, True) donne "aB3@cdEf".

import random

def generate_password(length, uppercase, digits, special_chars):
    valid_chars = []
    password = ""

    valid_chars += [chr(i) for i in range(65, 91)] if uppercase else []
    valid_chars += [chr(i) for i in range(48, 58)] if digits else []
    valid_chars += [chr(i) for i in range(33, 48)] if special_chars else []


    for i in range(length):
        password += random.choice(valid_chars)

    return password

print(generate_password(8, True, True, True)) # aB3@cdEf
print(generate_password(20, True, True, False)) # aB3cdEf
