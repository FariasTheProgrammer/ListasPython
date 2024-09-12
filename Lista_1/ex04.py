sal= float(input("Insira o seu salário: "))
porc= int(input("Insira a porcentagem do aumento: "))
calc = sal + (sal * porc / 100)
print (f"O seu salário aumentou R${calc}. Depois do aumento seu salário será: R${calc}")