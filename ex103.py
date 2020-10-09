def ficha(nome='<desconhecido>', gol= 0):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if gol.isnumeric():
        gol = int(gol)
    else:
        gol = 0
    return f'O jogador {nome} fez {gol} gol(s) nesse campeonato.'

nome_do_jogador = str(input('Nome do jogador: '))
gols = input('Número de gols: ')
print(ficha(nome_do_jogador, gols))