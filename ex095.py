jogadores = []


while True:
    aproveitamento = {}
    gols = []
    aproveitamento['nome_do_jogador'] = str(input('Nome do jogador: ')).title()
    n_de_partidas = int(input('Quantas partidas jogadas: '))

    for n in range(0, n_de_partidas):
        gol = int(input(f'      Quantos gols feito na {n + 1} partida: '))
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
for k in aproveitamento.keys():
    print(f'{k:<10} ', end='')

print()
print('=-' * 30)

for k, v in enumerate(jogadores):
    print(f'{k:>3} ')
    for g in v.values():
        print(f'{str(g):<15}', end='')
    print()

print('=-' * 30)

while True:
    verificar = int(input('Mostrar dados de qual jogador? [999 para interromper] '))
    if verificar == 999:
        break
    print(f'Ele jogou {len(jogadores[verificar]["gols"])} partidas.')
    for k, v in enumerate(jogadores[verificar]['gols']):
        print(f'Na partida {k + 1} ele fez {v} gols')
print('Obrigado por usar o programa!')