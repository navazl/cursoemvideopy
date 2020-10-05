matriz = list()

lista1 = list()
lista2 = list()
lista3 = list()
listamaior = list()

soma = soma3coluna = soma2linha = 0

for v in range(0, 3):
    num1 = int(input(f'Valor para [0, {v}]: '))
    lista1.append(num1)
    if num1 % 2 == 0:
        soma += num1
    if v == 2:
        soma3coluna += num1

for v in range(0, 3):
    num2 = int(input(f'Valor para [1, {v}]: '))
    lista2.append(num2)
    if num2 % 2 == 0:
        soma += num2
    if v == 2:
        soma3coluna += num2
    listamaior.append(num2)    

for v in range(0, 3):
    num3 = int(input(f'Valor para [2, {v}]: '))
    lista3.append(num3)
    if num3 % 2 == 0:
        soma += num3
    if v == 2:
        soma3coluna += num3


matriz.append(lista1)
matriz.append(lista2)
matriz.append(lista3)

for v in matriz:
    print(f'[{v[0]:^5}] [ {v[1]:^5} ] [ {v[2]:^5} ]')

print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da 3 coluna é {soma3coluna}')
print(f'O maior número da segunda linha é {max(listamaior)}')