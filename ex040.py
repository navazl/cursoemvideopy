nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))

media = (nota_1 + nota_2) / 2

print(f'Tirando {nota_1} e {nota_2}, a média do aluno é {media:.1f}')
if media < 5.0:
    print('REPROVADO!')
elif media > 5.0 and media < 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')




