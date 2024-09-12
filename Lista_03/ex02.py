while True:
    user = str(input('Insira o nome do usuário: '))
    senh = str(input('Insira a senha do usuário: '))
    if user != senh:
        print('Usuário aprovado!')
        break
    else: 
       print('Tente novamente. Usuário inválido!') 
