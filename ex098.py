def contador(x, y, z):
    if z == 0:
        z =+ 1
    if z > 0:
        if x <= y:
            while x <= y:
                print(f'{x} ', end='')
                x += z
        if x >= y:
            while x >= y:
                print(f'{x} ', end='')
                x -= z
    else:
        while x >= y:
            if z < 0:
                print(f'{x} ', end='')
                x += z

    print('Fim!')

def lin():
    print('=' * 30)


# PROGRAMA PRINCIPAL
lin()
print('Contagem de 1 até 10 de 1 em 1')
contador(1, 10, 1)

lin()
print('Contagem de 10 até 0 de 2 em 2')
contador(10, 0, -2)

lin()
print('Escolha a contagem: ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)

lin()

print('Obrigado por usar o programa!')