import random

lista = [random.randint(1, 100) for x in range(20)]

lista_par = []
lista_impar = []

for numero in lista:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

print(f"Lista original: {lista}")
print(f"Lista de números pares: {lista_par}")
print(f"Lista de números ímpares: {lista_impar}")
