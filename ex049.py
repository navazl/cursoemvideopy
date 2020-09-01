num = int(input('Digite um número: '))
cont = 0
for c in range(0, 10):
    cont += 1
    vezes = num * cont
    print(f'{num} x {cont:2} = {vezes}')