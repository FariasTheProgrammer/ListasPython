import calendar
import datetime

ano = int(input('Que ano você quer analisar? E se quiser o ano atual, só digitar 0: '))

if ano == 0:
    atual = datetime.datetime.now().year
    if calendar.isleap(atual):
        print('{} É um ano bissexto.'.format(atual))
    else:
        print('O ano atual não é bissexto.')
else:
    biounao = calendar.isleap(ano)
    if biounao is True:
        print('É bissexto')
    else:
        print('Não é bissexto.')