while True:
    nota = int(input('Insira a nota: '))
    if 0 <= nota <= 10:
        print('Nota válida!')
        break
    else:
        print('Nota inválida. Tente novamente.')
