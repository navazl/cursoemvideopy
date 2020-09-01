total = 0
contador = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        contador += 1
        total = total + c
print(f'A soma de {contador} valores solicitados foi {total}.')