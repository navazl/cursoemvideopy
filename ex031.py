distância = float(input('Qual a distância da viagem em Km: '))
if distância <= 200:
    distância = distância * 0.50
    print(f"Você pagará R${distância:.2f}")
else:
    distância = distância * 0.45
    print(f"Você pagará R${distância:.2f}")