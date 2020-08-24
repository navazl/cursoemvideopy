largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
dimensao = largura * altura
print(f'Sua parede tem a dimensão de {largura}x{altura} = {dimensao}m².')
print(f'Para pintar essa parede, você precisará de {dimensao / 2}l de tinta.')