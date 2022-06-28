"""
Este es un juego de adivinar un número que se genera aleatoriamente
"""

import random

def main():
    lower_limit = int(input("Ingrese un numero menor: "))
    upper_limit = int(input("Ingrese un numero mayor: "))
    number_secret = random.randint(lower_limit, upper_limit)
    tries = 0

    while True:
        tries +=1
        user_number = int(input("Ingrese un número para intentar de nuevo: "))

        if user_number < number_secret:
            print("Ingrese un número más grande")
        elif user_number > number_secret:
            print("Ingrese un número más pequeño")
        else:
            print(f'Ganaste!! el número de intentos fue {tries}')
            break
if __name__ == '__main__':
    main()