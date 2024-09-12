import random

lista = [random.randint(1, 100) for x in range(10)]

menor = lista[0]
maior = lista[0]
i = 1

while i < len(lista):
    if lista[i] < menor:
        menor = lista[i]  
    if lista[i] > maior:    
        maior = lista[i]  
    i += 1


print(f"Lista: {lista}")
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
