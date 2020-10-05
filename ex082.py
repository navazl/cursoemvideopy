lista = []
listapar = []
listaimpar = []
count = 0
while True:
    count += 1

    lista.append(int(input(f'Digite o {count} número: ')))
    verificacao = str(input('Quer continuar? [S/N]')).upper()
    if verificacao == 'N':
        break

for v in lista:
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)

print(f'Lista com todos os números: {lista}.')
print(f'Lista com todos os números pares {listapar}.')
print(f'Lista com todos os números impares {listaimpar}.')
