numeros = list(range(1,11))

for numero in numeros:
    print('Tabuada do {}:'.format(numero))
    for outro_numero in numeros:
        print('{:^30}'.format(numero * outro_numero))
    print('--------------')