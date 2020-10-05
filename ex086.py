matriz = list()

lista1 = list()
lista2 = list()
lista3 = list()

for v in range(0, 3):
    num1 = int(input(f'Valor para [0, {v}]: '))
    lista1.append(num1)

for v in range(0, 3):
    num2 = int(input(f'Valor para [0, {v}]: '))
    lista2.append(num2)

for v in range(0, 3):
    num3 = int(input(f'Valor para [0, {v}]: '))
    lista3.append(num3)

matriz.append(lista1)
matriz.append(lista2)
matriz.append(lista3)

for v in matriz:
    print(f'[{v[0]:^5}] [ {v[1]:^5} ] [ {v[2]:^5} ]')