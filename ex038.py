n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

if n1 > n2:
    print(f'O primeiro valor ({n1}) é maior.')

elif n2 > n1:
    print(f'O segundo valor ({n2}) é maior.')

elif n1 == n2:
    print(f'Os dois valores são iguais.')