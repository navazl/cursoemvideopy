#codigo mal resolvido

cont18 = conth = contm = 0

while True:
    idade = int(input('Idade: '))
    sexo = verificacao = ''

    sexo = str(input('Masculino ou Feminino [M/F]? ')).upper()

    
    if idade >= 18:
        cont18 += 1
    if sexo == 'M':
        conth += 1
    if sexo == 'F':
        if idade <= 20:
            contm += 1
    

    verificacao = str(input('Quer continuar [S/N]? ')).upper()

    if verificacao == 'N':
        break

print('FIM!')
print(f'Total de pessoas com mais de 18 anos: {cont18}.')
print(f'Total de homens cadastrados: {conth}.')
print(f'Total de mulheres com menos de 20 anos: {contm}')