lista = []
count = 0
while True:
    count += 1
    lista.append(int(input(f'Número {count}: ')))
    verificacao = str(input('Quer continuar? [S/N]: ')).upper()
    if verificacao == 'N':
        break
print(f'Quantidade de números digitados: {len(lista)}')
lista.sort(reverse=True)
print(f'Lista de valores, ordenada em forma decrescente: {lista}.')
if 5 in lista:
    print('O valor 5 foi digitado e está na lista.')
else:
    print('O valor 5 não foi digitado e não está na lista.')
