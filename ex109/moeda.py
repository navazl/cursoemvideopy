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
