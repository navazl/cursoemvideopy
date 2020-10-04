'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''

num = int(input(f'Valor 1: ')), int(input(f'Valor 2: ')), int(input(f'Valor 3: ')), int(input(f'Valor 4: '))
print(f'Você digitou os valores {num}.')
print(f'Quantidade de vezes que apareceu o 9: {num.count(9)}.')
if 3 in num:
    print(f'Posição em que o 3 apareceu: {num.index(3)}ª posição.')
else:
    print('O 3 não foi digitado.')

cont = 0
for n in num:
    if n % 2 == 0:
        cont += 1

print(f'Quantidade de números pares: {cont}')