expr = str(input("Digite uma expressão:"))
pilha = 0

for cont in expr:
    if cont == "(":
        pilha += 1
    if cont == ")":
        pilha -= 1
    if pilha < 0:
        break

if pilha == 0:
    print("Sua expressão é VALIDA!")
else:
    print("Sua expressão é INVALIDA!")