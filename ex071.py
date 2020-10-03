sacado = int(input('Valor a ser sacado: R$: '))
cedulasde50 = cedulasde20 = cedulasde10 = cedulasde5 = cedulasde1 = 0
while True:
    if sacado >= 50:
        cedulasde50 += 1
        sacado - 50
        if sacado < 50:
            cedulasde20
