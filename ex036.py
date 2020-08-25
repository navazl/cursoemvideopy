valor_da_casa = float(input('Qual é o valor da casa? R$'))
salário_do_comprador = float(input('Qual é o salário do comprador? R$'))
pagar_em_qnts_anos = int(input('Quantos anos você vai pagar? '))

prestacao_mensal = valor_da_casa / (pagar_em_qnts_anos * 12)
exceder = salário_do_comprador + (salário_do_comprador * 30 / 100)

print(f'Para pagar uma casa de R${valor_da_casa} em {pagar_em_qnts_anos} anos a prestação será de R${prestacao_mensal:.2f}.')
if salário_do_comprador <= exceder:
    print('O seu empréstimo foi negado!')
else:
    print('O seu empréstimo foi aceito!') 