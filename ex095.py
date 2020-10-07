jogadores = []


while True:
    aproveitamento = {}
    gols = []
    aproveitamento['nome_do_jogador'] = str(input('Nome do jogador: ')).title()
    aproveitamento['n_de_partidas'] = int(input('Quantas partidas jogadas: '))

    for n in range(0, aproveitamento['n_de_partidas']):
        gol = int(input(f'Quantos gols feito na {n + 1} partida: '))
        gols.append(gol)
    aproveitamento['gols'] = gols
    aproveitamento['total'] = sum(gols)
    jogadores.append(aproveitamento.copy())

    while True:
        verificacao = str(input('Quer continuar? [S/N]: ')).upper()
        if verificacao in 'SN':
            break
        print('Digite apenas S ou N.')
    if verificacao == 'N':
        break

print('=-' * 30)
for g in jogadores:
    for k, v in g.items():
        print(f'{k}', end='')
        print(f'{v}', end='')
    print()
print('=-' * 30)

