from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for n in range(0, 7):
    nasc = int(input(f'Em que ano a {n + 1}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Tivemos {totmaior} maiores de idade e {totmenor} menores de idade.')