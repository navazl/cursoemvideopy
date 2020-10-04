extenso = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
num = int(input('Número: '))
while num >= 20 or num <= 0:
    num = int(input('Tente novamente. Número: '))
print(f'Você digitou o número {extenso[num]}.')