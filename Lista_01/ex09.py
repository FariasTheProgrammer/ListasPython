qtddia = int(input('Insira a quantidade de dias que o carro ficou alugado: '))
kmperc = int(input('Insira a quantidade de km que o carro percorreu: '))

calc = (qtddia * 60) + (0.15 * kmperc)

print(f'A quantidade a pagar será: R${calc:.2f}')