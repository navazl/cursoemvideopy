def escreva(txt):
    tam = len(txt) + 4
    print('=' * tam)
    print(f'  {txt}')
    print('=' * tam)

algo = str(input('Escreva algo: '))
escreva(algo)
