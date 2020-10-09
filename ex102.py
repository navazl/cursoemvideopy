def factorial(n, show=False):
    """
    Calcula a fatorial de um número.
    :param n: O número a ser fatorado.
    :param show: (opcional) Diz se irá mostrar na tela o processo.
    :return: Retorna um valor.
    """
    f = 1
    for c in range(n, 0, -1):
        if show == True:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f
        

print(factorial(5, show=True))
help(factorial)