num = int(input('Digite um número inteiro: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[34m', end= ' ')
        tot += 1
    else:
        print('\033[32m', end = ' ')
    print(f'{c}', end = ' ')
print(f'\n\033[mO número {num} foi divisível {tot} vezes.')
if tot == 2:
    print('É por isso ele é primo.')
else:
    print('Por isso ele não é primo.')
    