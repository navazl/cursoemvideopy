qntd_dias = int(input('Quantidade de dias que ele foi alugado? '))
qntd_km = float(input('Quantidade de Km? '))
preço = (qntd_dias * 60) + (qntd_km * 0.15)
print(f'O total a pagar é {preço}')