from moeda import metade, dobro, aumentar, diminuir, moeda

p = float(input('Digite o preço: R$'))
print(f'Metade de {moeda(p)} é {metade(p, format=True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, format=True)}')
print(f'Aumentando 10% é {aumentar(p, 10)}')
print(f'Diminuindo 13$ é {diminuir(p, 13, format=True)}')
