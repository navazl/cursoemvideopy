salario = float(input('Qual é o salário de Funcionário? R$'))
aumento = salario + (salario * 15 / 100)
print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber {aumento:.2f}')