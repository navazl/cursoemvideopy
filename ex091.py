from random import randint
from time import sleep
from operator import itemgetter

dado = dict()
for i in range(1, 5):
    dado[f'Jogador {i}'] = randint(1, 6)

raking = list()

print('Valores sorteados: ')
for k, v in dado.items():
    print(f'{k} tirou {v}')

ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)

print('Ranking: ')
for k, v in enumerate(ranking):
    print(f'{k + 1}° lugar: {v[0]} com {v[1]}.')