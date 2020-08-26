from datetime import date
ano_de_nascimento = int(input('Qual a sua data de nascimento? '))
atual = date.today().year
idade = atual - ano_de_nascimento

print(f'Quem nasceu em {ano_de_nascimento} tem {idade} anos no ano {atual}.')

if idade < 18:
    tempo = 18 - idade
    print(f'Você tem {idade} anos e ainda vai se alistar ao exercito!')
    print(f'Falta {tempo} anos para você se alistar.')
    print(f'Seu alistamento será em {atual + tempo}.')
elif idade == 18:
    print(f'Você tem {idade} e já é hora de se alistar ao exercito!')
else:
    tempo = idade - 18  
    print(f'Você tem {idade} anos e já passou do tempo do alistamento!')
    print(f'Faz {tempo} que passou do prazo de você se alistar.')
    print(f'Seu alistamento foi em {atual - tempo}.')