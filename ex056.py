somaidade = 0
medidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print(f'{c}ª pessoa:')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Homem ou Mulher [H] e [M]: '))
    somaidade += idade
    if c == 1 and sexo in 'Hh':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Hh' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade < 20:
        totmulher20 += 1

medidade = somaidade / 4
print(f"A média de idade do grupo é de {medidade} anos.")
print(f"O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}")
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')