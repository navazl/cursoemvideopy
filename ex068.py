import random
cont = 0
while True:
    num = int(input('Valor: '))
    p_ou_i = str(input('Par ou Ímpar [P/I]? ')).upper()
    print('=' * 15)

    if p_ou_i == 'P':
        p_ou_i = 'PAR'
    if p_ou_i == 'I':
        p_ou_i = 'IMPAR'
    num_random = random.randrange(0, 11)

    total = num + num_random
    totalpoui = ''
    if total % 2 == 0:
        totalpoui = 'PAR'
    else:
        totalpoui = 'IMPAR'

    print(f'Você jogou {num} e o Computador jogou {num_random}. Total de {total}, deu {totalpoui}.')
    print('=' * 15)
    
    if p_ou_i == totalpoui:
        print('VOCÊ GANHOU! ')
        print('VAMOS JOGAR NOVAMENTE...')
    else: 
        print('VOCÊ PERDEU')
        break

    cont += 1
    
print(f'Obrigado por jogar! Você venceu {cont} vezes.')