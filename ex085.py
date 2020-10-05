lista_principal = list()
lista_par = list()
lista_impar = list()

for i in range(1, 8):
    num = int(input(f'Digite o {i}º número: '))
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
    
    if i == 7:
        lista_par.sort()
        lista_impar.sort()

        lista_principal.append(lista_par[:])
        lista_principal.append(lista_impar[:])

        lista_par.clear()
        lista_impar.clear()

print(f'Valores pares: {lista_principal[0]}')
print(f'Valores impares: {lista_principal[1]}')