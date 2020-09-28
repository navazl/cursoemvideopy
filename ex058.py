import random
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
num_random = random.randrange(0, 11)
num = int(input('Em que número eu pensei? '))
vezes = 0
while num != num_random:
    num = int(input('Errou. Tente novamente: '))
    vezes += 1
print(f'O número foi {num_random}, você acertou depois de {vezes} tentativas.')
