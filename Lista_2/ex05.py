n1 = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
n3 = int(input('Insira o terceiro número: '))

if n1 >= n2 and n1 >= n3:
    print('O maior número é o primeiro.')
    
elif n2 >= n1 and n2 >= n3: 
    print('O maior número é o segundo.')

else:
    print('O maior número é o terceiro.')

#menor

if n1 <= n2 and n1 <= n3:
    print('O menor número é o primeiro.')
    
elif n2 <= n1 and n2 <= n3: 
    print('O menor número é o segundo.')

else:
    print('O menor número é o terceiro.')
