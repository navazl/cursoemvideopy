lista = list()
dados = list()
totcadastro = mai = men = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))

    if len(lista) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]

    lista.append(dados[:])
    dados.clear()
    totcadastro += 1

    verificacao = str(input('Quer continuar? [S/N] ')).upper()
    if verificacao == 'N':
        break

print(f'Quantidade de cadastros: {totcadastro}.')
print(f'Maior peso: {mai}Kg. Peso de: ', end ='')

for p in lista:
    if p[1] == mai:
        print(f'{p[0]}, ')

print()

print(f'Menor peso: {men}Kg. Peso de: ', end='')
for p in lista:
    if p[1] == men:
        print(f'{p[0]}, ')