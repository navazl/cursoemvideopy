lista = list()

count = 0

while True:
    aluno = list()
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    verificacao = str(input('Quer continuar? [S/N] ')).upper()
    if verificacao == 'N':
        break  

print('=' * 30)
print(f'{"Num":<4}{"Nome":<10}{"Média":>8}')
for v in lista:
    print(f'{count:<4} {v[0]:<10} {v[2]:>8.1f} ')

    count += 1

print('=' * 30)

while True:
    verificar = int(input('Mostrar a nota de qual aluno? [999 para interromper] '))
    if verificar == 999:
        break
    print(f'As notas de {lista[verificar][0]} é {lista[verificar][1]}')


print('Obrigado por usar o programa!')
