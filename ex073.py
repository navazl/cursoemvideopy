top20brasileirao = 'Atlético-MG', 'Internacional', 'Palmeiras', 'São Paulo', 'Vasco', 'Flamengo', 'Fluminense', 'Sport', 'Santos', 'Fortaleza', 'Athletico-PR', 'Ceará', 'Corinthians', 'Atlético-GO', 'Grêmio', 'Bahia', 'Bragantino', 'Coritiba', 'Botafogo', 'Goiás'
print(f'Os 5 primeiros colocados são: {top20brasileirao[:5]}')
print(f'Os 4 últimos colocados são: {top20brasileirao[-4:]} ')
print(f'Os times em ordem alfabética são: {sorted(top20brasileirao)}')
print(f'O Corinthians está ná {top20brasileirao.index("Corinthians") + 1}ª posição.')