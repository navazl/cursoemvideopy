totgasto = maisde1000 = cont = menor = 0
produtomaisbarato = ''
while True:
    cont += 1

    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))

    totgasto += preço
    if preço >= 1000:
        maisde1000 += 1
    if cont == 1 or preço < menor:
        produtomaisbarato = nome
        menor = preço
    
    verificacao = str(input('Quer continuar [S/N]? ')).upper()
    if verificacao == 'N':
        break

print('=' * 30)   
print(f'Total da compra: {totgasto:.2f}')
print(f'Produtos custando mais de R$1000.00: {maisde1000:}')
print(f'O item mais barato foi: {produtomaisbarato} custando R${menor:.2f}')