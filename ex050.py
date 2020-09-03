soma = 0
cont = 0
for c in range (0, 6):
    numeros = int(input('Digite um número: '))
    if numeros % 2 == 0:
        soma += numeros
        cont += 1

print(f'Você digitou {cont} números pares e a soma entre eles foi {soma}')