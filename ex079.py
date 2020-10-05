lista = []
count = 0

while True:
    count += 1

    num = int(input(f'Digite o {count} número: '))
    if num not in lista:
        lista.append(num)

    verificacao = str(input('Quer continuar? [S/N] ')).upper()
    if verificacao == 'N':
        break

print(f'Número digitados em forma crescente: {sorted(lista)}.')