valor = float(input('Qual o valor a ser pago? R$'))
print('''
FORMAS DE PAGAMENTO:
[ 1 ] À VISTA NO DINHEIRO/CHEQUE: 10% DE DESCONTO.
[ 2 ] À VISTA NO CARTÃO: 5% DE DESCONTO.
[ 3 ] 2X NO CARTÃO: PREÇO NORMAL.
[ 4 ] 3X OU MAIS NO CARTÃO: 20% DE JUROS.
''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    print('Sua compra será paga à vista no dinheiro/cheque.')
    valor_final = valor - (valor * 10 / 100)
    print(f'Sua compra de R${valor:.2f} irá custar R${valor_final:.2f} no final.')

elif opcao == 2:
    print('Sua compra será paga à vista no cartão.')
    valor_final = valor - (valor * 5 / 100)
    print(f'Sua compra de R${valor:.2f} irá custar R${valor_final:.2f} no final.')

elif opcao == 3:
    parcelas = valor / 2
    print(f'Sua compra será paga em 2x R${parcelas:.2f} no cartão SEM JUROS.')
    valor_final = valor
    print(f'Sua compra de R${valor:.2f} irá custar R${valor_final:.2f} no final.')

elif opcao == 4:
    valor_final = valor + (valor * 20 / 100)
    total_de_parcelas = int(input('Quantas vezes você quer parcelar no cartão? '))
    parcelas = valor_final / total_de_parcelas
    print(f'Sua compra será parcelada em {total_de_parcelas}x de R${parcelas:.2f} no cartão COM JUROS.')
    print(f'Sua compra de R${valor:.2f} irá custar R${valor_final:.2f} no final.')

else:
    print('Opção invalida. Tente novamente!')

