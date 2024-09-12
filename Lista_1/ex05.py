merc = float(input("Insira o valor da sua mercadoria: "))
porc= int(input("Insira a porcentagem de desconto: "))
calc = merc - (merc * porc / 100)
print (f"A mercadoria custa R${merc}. Depois do desconto o valor será: R${calc}")