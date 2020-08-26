from datetime import date

ano_de_nascimento = int(input('Qual é o ano de nascimento do atleta? '))

atual = date.today().year
idade = atual - ano_de_nascimento

print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print(f'Categoria: MIRIM.')

elif idade <= 14:
    print(f'Categoria: INFANTIL.')

elif idade <= 19:
    print(f'Categoria: JUNIOR.')

elif idade <= 25:
    print(f'Categoria: SÊNIOR.')

else:
    print(f'Categoria: MASTER.')




