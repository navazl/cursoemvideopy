aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input('Média: '))

print(f'Nome do aluno {aluno["nome"]}')
print(f'Média do aluno {aluno["média"]}')

if aluno["média"] >= 7:
    print('Situação: aprovado.')
else:
    print('Situação: reprovado.')