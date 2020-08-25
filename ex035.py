a = float(input('Coloque o valor de um lado: '))
b = float(input('Coloque o valor de outro lado: '))
c = float(input('Coloque o valor de outro lado: '))

if abs(b - c) < a <  b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print(f'Os lados {a}, {b} e {c} podem formar triângulo.')
else:
    print(f'Os lados {a}, {b} e {c} não podem formar triângulo.')