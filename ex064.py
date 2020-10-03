num = cont = soma = 0
while num != 999:
    num = int(input('Digite um numero [999 para parar]: '))
    soma += num
    cont += 1
    if num == 999:
        cont -= 1
        soma -= 999
print(f'Total de números digitados: {cont}')
print(f'A soma entre todos eles: {soma}')