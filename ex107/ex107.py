from moeda import metade, dobro, aumentar, diminuir

p = float(input('Digite o preço: R$'))
print(f'Metade de {p} é R${metade(p)}')
print(f'O dobro de {p} é R${dobro(p)}')
print(f'Aumentando 10% é R${aumentar(p, 10)}')
print(f'Diminuindo 13$ é R${diminuir(p, 13)}')
