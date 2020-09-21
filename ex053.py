frase = str(input('Digite um frase: ')).strip().upper().split()
junto = ''.join(frase)
invertida = junto[::-1]
print(f'O inverso de {junto} é {invertida}.')
if junto == invertida:
    print('A frase digitada é um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')