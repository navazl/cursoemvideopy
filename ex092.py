from datetime import date

dados = {}
ano_atual = date.today().year

dados['nome'] = str(input('Nome: '))
ano_de_nascimento = int(input('Ano de nascimento: '))
dados['idade'] = ano_atual - ano_de_nascimento
dados['carteira_de_trabalho'] = int(input('Carteira de trabalho (0 não tem):'))

if dados['carteira_de_trabalho'] != 0:
    dados['ano_de_contratação'] = int(input('Ano da contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano_de_contratação'] + 35) - ano_atual)

for k, v in dados.items():
    print(f'{k}: {v}')
print(dados)