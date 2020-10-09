def leiaInt(txt):
    while True:
        num = str(input(txt))
        if num.isnumeric():
            num = int(num)
            return num
        else:
            print('Erro! Digite um número valido.')
        if num.isnumeric():
            break

numero = leiaInt('Digite um número: ')
print(f'O número que você digitou é {numero}.')