from random import randint

def sorteia(x):
    print('Sorteando 5 valores: ', end='')
    for value in range(0, 5):
        raldo = randint(1, 10)
        print(f'{raldo} ', end='')
        lista.append(raldo)
    print('FIM!')

def somaPar(x):
    soma = 0
    for v in x:
        if v % 2 == 0:
            soma += v
    print(f'Os valores pares de {x} somados dão {soma}')


lista = list()
sorteia(lista)
somaPar(lista)