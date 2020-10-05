lista = []
for i in range(0, 5):
    num = int(input(f'Digite o {i} valor: '))
    if i == 0 or num > lista[-1]:
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1
print(f'Valores digitados em ordem: {lista}.')