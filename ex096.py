def área(x, y):
    total = x * y
    print(f'A area de um terreno {x}x{y} é de {total}m².')


largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o comprimento: '))
área(largura, comprimento)
