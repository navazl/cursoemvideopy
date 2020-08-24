import random
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
num = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(2)
num_random = random.randrange(0, 6)
if num != num_random:
    print(f"Ganhei! Eu pensei no número {num_random} não no número {num}.")
else: 
    print('Parabens! Você conseguiu me vencer!')
