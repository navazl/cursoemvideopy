import math
co = float(input('Qual o comprimento do cateto oposto: '))
ca = float(input('Qual o comprimenot do cateto adjacente: '))
hi = math.hypot(co, ca)
print(f'A hipotenusa vai medir {hi:.2f}')