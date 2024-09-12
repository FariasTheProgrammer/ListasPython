dias = int(input("Insira a quantidade de dias: "))
horas = int(input("Insira a quantidade de horas: "))
minutos = int(input("Insira a quantidade de minutos: "))
segundos = int(input("Insira a quantidade de segundos: "))
calcDia = dias * 86400
calcHoras = horas * 3600
calcMinutos = minutos * 60
calcTotal = calcDia + calcHoras + calcMinutos + segundos
print(f"O seu total em segundo é: {calcTotal}")
