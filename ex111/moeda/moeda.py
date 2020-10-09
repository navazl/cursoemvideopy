def aumentar(n, p, format=False):
    ans = n + (n * (p / 100))
    return ans if format is False else moeda(ans)


def diminuir(n, p, format=False):
    ans = n - (n * (p / 100))
    return ans if format is False else moeda(ans)
    

def dobro(n, format=False):
    ans = n * 2
    return ans if format is False else moeda(ans)


def metade(n, format=False):
    ans = n / 2
    return ans if format is False else moeda(ans)


def moeda(n):
    return f'R${n:.2f}'.replace('.', ',')

def resumo(n, a, d):
    linha(30)
    print(f'Resumo do valor')
    linha(30)
    print(f'Preço analisado: {moeda(n)}')
    print(f'Dobro do preço: {dobro(n, format=True)}')
    print(f'Metade do preço: {metade(n, format=True)}')
    print(f'{a}% de aumento: {aumentar(n, a, format=True)}')
    print(f'{d}% de redução {diminuir(n, d, format=True)}')
    linha(30)

def linha(n):
    print('-' * n)