print('Digite dois números')
n1 = float(input('Primeiro: '))
n2 = float(input('Segundo: '))
opcao = 0
while opcao != 5:
    print('=--='* 8)
    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa
    ''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        print(f'Os números foram: {n1} e {n2}. A soma é {n1 + n2}')
    if opcao == 2:
        print(f'Os números foram: {n1} e {n2}. A multiplicação é {n1 * n2}')
    if opcao == 3:
        print(f'Os números foram: {n1} e {n2}. O maior é {max(n1, n2)}')
    '''possivel solução, sem função:
        if n1 > n2 == True:
            print(f'O maior número entre {n1} e {n2} é {n2}')
        else:
            print(f'O maior número entre {n1} e {n2} é {n1}')'''
    if opcao == 4:
        print('Digite dois números')
        n1 = float(input('Primeiro: '))
        n2 = float(input('Segundo: '))
print('Obrigado por usar o programa!')