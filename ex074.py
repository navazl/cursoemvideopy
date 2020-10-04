from random import randint

random = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Números sorteados: ', end='')
for n in random:
    print(f'{n} ', end ='')
print(f'\nMaior número: {max(random)}')
print(f'Menor número: {min(random)}')