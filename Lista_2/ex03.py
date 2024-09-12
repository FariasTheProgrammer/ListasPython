peso_peixe = float(input('Insira o peso do peixe em kilograma: '))

if peso_peixe>=50:    
    multa = (peso_peixe - 50) * 4
    excesso = (peso_peixe - 50)
    print(f'Passou do peso em {excesso}kg. O valor a ser pago de multa será R${multa:.2f}')

elif peso_peixe<50:
    multa = "Zero"
    excesso = "Zero"
    print(f'Peso ultrapassado: {excesso} e multa igual a: {multa} ')
    