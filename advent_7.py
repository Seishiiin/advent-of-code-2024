# Description : Advent of Code 2024 - Day 7
# Vérifie si une chaîne donnée est un palindrome (insensible à la casse et aux espaces).
# Exemple : "kayak" donne True et "hello" donne False.

def is_palindrome(string) -> bool :
    return string.lower().replace(" ", "") == string[::-1].lower().replace(" ", "")

print(is_palindrome("Engage le jeu que je le gagne")) # => True
print(is_palindrome("Salut les amis")) # => False