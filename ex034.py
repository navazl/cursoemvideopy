salário = float(input('Qual é o salário do funcionário? R$'))

if salário <= 1250.00:
    aumento = salário + (salário * 15 / 100)
    print(f'Quem ganhava R${salário} passa a ganhar R${aumento:.2f} agora.')
else:
    aumento = salário + (salário * 10 / 100)
    print(f'Quem ganhava R${salário} passa a ganhar R${aumento:.2f} agora.')
