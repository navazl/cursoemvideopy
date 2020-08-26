peso = float(input('Peso (em Kg): '))
altura = float(input('Altura (em m): '))

imc = peso / (altura ** 2)

print(f'Você pesa {peso}Kg e tem {altura}m de altura. Seu IMC é {imc:.2f}.')
if imc < 18.5:
    print(f'Você está abaixo do peso.')
elif imc >= 18.5 and imc <= 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc <= 30:
    print('Você está em sobrepeso.')
elif imc >= 30 and imc <= 40:
    print('Você está em obesidade.')
else:
    print('Você está em obesidade morbida.')