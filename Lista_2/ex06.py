salAtual= float(input('Insira a quantidade que você recebe por hora: '))
horasTrab = int(input('Insira a quantidade de horas que você trabalha no mês: '))

bruto = salAtual * horasTrab
impRenda = (bruto * 1.11) - bruto
inss = (bruto * 1.08)  - bruto
Sindicato = (bruto * 1.05) - bruto
limpo = bruto - (impRenda + inss + Sindicato) 

print(f'Seu salário bruto é R$:{bruto:.2f}')
print(f'É descontado R$:{impRenda:.2f}, pelo Imposto de renda')
print(f'É descontado R$:{inss:.2f}, pelo INSS')
print(f'É descontado R$:{Sindicato:.2f}, pelo Sindicato')
print(f'Seu salário liquido é R$:{limpo:.2f}')