fumou = int(input('Insira quantos cigarros você fuma por dia: '))
anos = int(input('Por quantos anos você fumou?: '))

qtddias = (anos * 365) 
qtdcigarro = qtddias * fumou

min_perdidos = qtdcigarro * 10
dias_perdidos = float(min_perdidos / 1440)

print (f'Dias perdidos: {dias_perdidos:.2f}')