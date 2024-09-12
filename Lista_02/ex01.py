lado1 = float(input('Insira o valor do seu primeiro lado do seu triângulo: '))
lado2 = float(input('Insira o valor do seu segundo lado do seu triângulo: '))
lado3 = float(input('Insira o valor do seu terceiro lado do seu triângulo: '))

if lado1 == lado2 == lado3:
    print('Seu triângulo é equilátero!')
    
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print('Seu triângulo é isósceles!')
    
else: 
    print ('Seu triângulo é escaleno!')