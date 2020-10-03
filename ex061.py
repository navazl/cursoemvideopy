num = int(input('Digite um número: '))
f = 1
while num > 0:
    print(f'{num}', end='')
    print(' x ' if num > 1 else ' = ', end='')
    f *= num
    num -= 1

print(f)