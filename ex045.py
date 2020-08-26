from random import randrange
from time import sleep

print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogada_do_usuario = int(input('Qual é a sua jogada? '))

jogada_do_pc = randrange(1, 4)

if jogada_do_usuario == 1:
    jogada_do_usuario = 'PEDRA'
elif jogada_do_usuario == 2:
    jogada_do_usuario = 'PAPEL'
elif jogada_do_usuario == 3:
    jogada_do_usuario = 'TESOURA'

if jogada_do_pc == 1:
    jogada_do_pc = 'PEDRA'
elif jogada_do_pc == 2:
    jogada_do_pc = 'PAPEL'
elif jogada_do_pc == 3:
    jogada_do_pc = 'TESOURA'

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=' * 25)
print(f'Você jogou {jogada_do_usuario} e o computador jogou {jogada_do_pc}.')
print('-=' * 25)

if jogada_do_usuario == 'PEDRA' and jogada_do_pc == 'PEDRA':
    print('EMPATE!')

elif jogada_do_usuario == 'PAPEL' and jogada_do_pc == 'PAPEL':
    print('EMPATE!')

elif jogada_do_usuario == 'TESOURA' and jogada_do_pc == 'TESOURA':
    print('EMPATE!')

elif jogada_do_usuario == 'PEDRA' and jogada_do_pc == 'TESOURA':
    print('VOCÊ GANHOU!')

elif jogada_do_usuario == 'TESOURA' and jogada_do_pc == 'PAPEL':
    print('VOCÊ GANHOU!')

elif jogada_do_usuario == 'PAPEL' and jogada_do_pc == 'PEDRA':
    print('VOCÊ GANHOU!')

elif jogada_do_pc == 'PEDRA' and jogada_do_usuario == 'TESOURA':
    print('VOCÊ GANHOU!')

elif jogada_do_pc == 'TESOURA' and jogada_do_usuario== 'PAPEL':
    print('VOCÊ GANHOU!')

elif jogada_do_pc == 'PAPEL' and jogada_do_usuario == 'PEDRA':
    print('VOCÊ GANHOU!')   