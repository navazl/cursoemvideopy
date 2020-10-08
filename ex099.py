
def maior(* p):
    print('=' * 30)
    print('Analisando valores')

    for k in p:
        if k > 0:
            print(f'{k} ', end='')
    print(f'Foram informados {len(p)} números.')
    print(f'O maior valor informado foi {max(p)}')

# Programa principal.
maior(2, 4, 5, 8, 10, 4)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()