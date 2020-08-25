num = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão: 
[1] para BINÁRIO 
[2] para OCTAL 
[3] para HEXADECIMAL''')
base_de_conversão = int(input('Qual dessas você escolhe? '))

if base_de_conversão == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif base_de_conversão == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif base_de_conversão == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Você digitou um número invalido!')