import random

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

numero = []

entrada = []


def trescifras():
    for i in range(0, 3):
        numero.append(random.choice(numeros))

    if numero[0] == numero[1] or numero[0] == numero[2] or numero[1] == numero[2]:
        trescifras()


def cuatrocifras():
    for i in range(0, 4):
        numero.append(random.choice(numeros))

    if numero[0] == numero[1] or numero[0] == numero[2] or numero[0] == numero[3] or numero[1] == numero[2] \
            or numero[1] == numero[3] or numero[2] == numero[3]:
        cuatrocifras()


def cincocifras():
    for i in range(0, 5):
        numero.append(random.choice(numeros))

    if numero[0] == numero[1] or numero[0] == numero[2] or numero[0] == numero[3] or numero[0] == numero[4] \
            or numero[1] == numero[2] or numero[1] == numero[3] or numero[1] == numero[4] \
            or numero[2] == numero[3] or numero[2] == numero[4] or numero[3] == numero[4]:
        cincocifras()


def comprobar():
    intentos = 0

    entrada = input("digite el numero que posiblemente sea:\n")

    if len(entrada) == 3:
        intentos = 10
    if len(entrada) == 4:
        intentos = 15
    if len(entrada) == 5:
        intentos = 20

    for i in range(intentos):
            fijas = 0
            picas = 0
            if intentos == 1:
                print("perdiste F en el chat ")
                exit()
            else:
                for i in range(len(entrada)):
                    if numero[i] == entrada[i]:
                        fijas = fijas + 1
                    if numero[i] in entrada:
                        picas = picas + 1
                if fijas == len(entrada):
                    print("ganaste!!!")
                    exit()
                print("tienes ", fijas, "fijas y tienes ", picas, "picas\n intentos restantes: ",intentos-1)
                entrada = input("digite el numero que posiblemente sea:\n")
                intentos= intentos-1


print("¿Con cuanta cifras desea jugar?")

opcion = input("a para 3 cifras\nb para 4 cifras\nc para 5 cifras\n")

if opcion == "a":
    print("opcion de 3 cifras")
    trescifras()

    print("el numero que debe encontrar es: ")
    for i in range(0, len(numero)):
        print(numero[i], end=" ")
    print()
    comprobar()


elif opcion == "b":
    print("opcion de 4 cifras")
    cuatrocifras()

    print("el numero que debe encontrar es: ")
    for i in range(0, len(numero)):
        print(numero[i], end=" ")
    print()

    comprobar()

elif opcion == "c":
    print("opcion de 5 cifras")
    cincocifras()

    print("el numero que debe encontrar es: ")
    for i in range(0, len(numero)):
        print(numero[i], end=" ")
    print()

    comprobar()

else:
    print("opcion invalida")
