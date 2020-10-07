aproveitamento = {}
gols = []

aproveitamento['nome_do_jogador'] = str(input('Nome do jogador: ')).title()
aproveitamento['n_de_partidas'] = int(input('Quantas partidas jogadas: '))

for n in range(0, aproveitamento['n_de_partidas']):
    gol = int(input(f'Quantos gols feito na {n + 1} partida: '))
    gols.append(gol)
aproveitamento['gols'] = gols
aproveitamento['total'] = sum(gols)

print('=-' * 30)
print(aproveitamento)
print('=-' * 30)

for k, v in aproveitamento.items():
    print(f'{k} : {v}')
print('=-' * 30)
print(f'O jogador {aproveitamento["nome_do_jogador"]} jogou {aproveitamento["n_de_partidas"]} partidas.')

for k, v in enumerate(gols):
    print(f'Na partida {k + 1} ele fez {v} gols')

print(f'Um total de {sum(gols)} gols.')