# Description : Advent of Code 2024 - Day 10
# Crée un programme qui convertit un nombre décimal en binaire, hexadécimal, et octal.
# Exemple : 10 donne 1010, A, 12.

def convert_decimal_to_binary(decimal):
    return bin(decimal)[2:]

def convert_decimal_to_hexadecimal(decimal):
    return hex(decimal)[2:]

def convert_decimal_to_octal(decimal):
    return oct(decimal)[2:]

def main(decimal):
    print(f"Binary: {convert_decimal_to_binary(decimal)}")
    print(f"Hexadecimal: {convert_decimal_to_hexadecimal(decimal)}")
    print(f"Octal: {convert_decimal_to_octal(decimal)}")

main(10)
main(16)