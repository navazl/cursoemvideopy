cadastros = list()
soma = 0
while True:
    cadastro = {}
    cadastro['nome'] = str(input('Nome: ')).title()

    while True:
        cadastro['sexo'] = str(input('Sexo [M/F]: ')).upper()
        if cadastro['sexo'] in 'MF':
            break
        print('Digite apenas M ou F.')

    cadastro['idade'] = int(input('Idade: '))
    soma += cadastro['idade']
    cadastros.append(cadastro.copy())

    while True:
        verificacao = str(input('Quer continuar? [S/N]: ')).upper()
        if verificacao in 'SN':
            break
        print('Digite apenas S ou N.')
    if verificacao == 'N':
        break

print('=-' * 30)
média = soma / len(cadastros)
print(f'Número de pessoas cadastradas: {len(cadastros)}')
print(f'A média de idade é {média:.2f} anos.')
print(f'Lista de mulheres é ', end='')
for v in cadastros:
    if v['sexo'] == 'F':
        print(f'{v["nome"]} ', end='')

print()

print('Pessoas com idade acima da média: ', end='')
for g in cadastros:
    if g['idade'] > média:
        print('     ', end ='')
        for k, v in g.items():
            print(f'{k} = {v}; ', end='')
