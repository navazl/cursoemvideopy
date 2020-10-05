from random import randint
from time import sleep
count = 0
jogos = list()
num_jogos = int(input('Número de jogos: '))
for i in range(0, num_jogos):
    num_sorteado = list()
    for i in range (0, 6):
        num_sorteado.append(randint(1, 61))
    jogos.append(num_sorteado)

print(f'SORTEANDO {num_jogos} JOGOS')
for v in jogos:
    count += 1
    print(f'Jogo {count}: {v}')
    sleep(1)
