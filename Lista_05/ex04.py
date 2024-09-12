acumulador = 0
for x in range (18644, 33088):
    str_x = str(x)
    if '2' in str_x and '7' not in str_x:
        acumulador += 1
print(acumulador)