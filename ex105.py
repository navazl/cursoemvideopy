def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional
    :return: retonra o valor
    """
    média = sum(n) / len(n)
    if sit == False:
        d = {'total': sum(n), 'maior_nota': max(n), 'menor_nota': min(n), 'média': f'{média:.2f}'}
    else:
        if média >= 7:
            d = {'total': sum(n), 'maior_nota': max(n), 'menor_nota': min(n), 'média': f'{média:.2f}', 'situação': 'BOA'}
        elif média >= 5:
            d = {'total': sum(n), 'maior_nota': max(n), 'menor_nota': min(n), 'média': f'{média:.2f}', 'situação': 'RAZOAVEL'}
        else:
            d = {'total': sum(n), 'maior_nota': max(n), 'menor_nota': min(n), 'média': f'{média:.2f}', 'situação': 'RUIM'}
    return d

resp = notas(5, 2, 6, sit=True)
print(resp)
help(notas)