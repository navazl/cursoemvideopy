primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
num = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while num != total:
        print(f'{primeiro_termo} > ', end='')
        primeiro_termo += razao
        num += 1
    print('Pausa')
    mais = int(input('Quantidade de termos adicionais: '))
print(f'Total de vezes: {total}')