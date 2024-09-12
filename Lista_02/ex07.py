import math

area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

litros_necessarios = area/ 3
latas_necessarias = math.ceil(litros_necessarios / 18)
preco_lata = 80
preco_total = latas_necessarias * preco_lata

print(f"Você precisará de {latas_necessarias} latas de tinta.")
print(f"O preço total será de R$ {preco_total:.2f}.")