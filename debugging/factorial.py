#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0:  # Gestion des cas où la factorielle est indéfinie
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    while n > 1:
        result *= n
        n -= 1  # On décrémee n chaque itération
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:  # Vérifie qu'un seul argument est passé
        print("Usage: ./factorial.py <number>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])  # Conversion en entier
        print(factorial(number))  # Calcul et affichage de la factorielle
    except ValueError as e:
        print(e)
        sys.exit(1)

