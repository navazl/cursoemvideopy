vel = int(input('Qual a velocidade do carro? ')) # Lê a velocidade do carro.
if vel > 80: # Verifica se a velocidade do carro é maior que 80km/h.
    multa = (vel - 80) * 7.00 # Descobre quantos Km/h ele está acima do limite e multiplica por R$7,00 (preço da multa).
    print(f"Você foi multado e terá que pagar R${multa:.2f}")
print("Tenha um bom dia, dirija com segurança!")
