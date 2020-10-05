num = []

for i in range(0, 5):
    num.append(int(input(f'Valor {i}: ')))
maior = max(num)
menor = min(num)

for k, v in enumerate(num):
    if v == maior:
        print(f'O maior valor: {v} na posição {k}ª.')

for k, v in enumerate(num):
    if v == menor:
        print(f'O menor valor: {v} na posição {k}ª.')
    
