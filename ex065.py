verificacao = ''
cont = soma = media = maior = menor = 0
while verificacao != 'N':
    n = int(input('Digite um número: '))
    verificacao = str(input('Deseja continuar? [S/N] ')).upper()
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = soma / cont
print(f'''
Números digitados: {cont} 
Média: {media}
Maior: {maior}
Menor: {menor}
''')