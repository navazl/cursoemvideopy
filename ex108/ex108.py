from moeda import metade, dobro, aumentar, diminuir, moeda

p = float(input('Digite o preço: R$'))
print(f'Metade de {moeda(p)} é R${moeda(metade(p))}')
print(f'O dobro de {moeda(p)} é R${moeda(dobro(p))}')
print(f'Aumentando 10% é R${moeda(aumentar(p, 10))}')
print(f'Diminuindo 13$ é R${moeda(diminuir(p, 13))}')
