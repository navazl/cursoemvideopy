def leiaInt(txt):
    while True:
        try:
            num = int(input(txt))
        except (ValueError, TypeError):
            print('Tenta novamente.')
            continue
        except (KeyboardInterrupt):
            print('Interrompido pelo usuário.')
            return 0        
        else:
            return num

def leiaFloat(txt):
    while True:
        try:
            num = float(input(txt))
        except (ValueError, TypeError):
            print('Tente novamente.')
            continue
        except (KeyboardInterrupt):
            print('Interrompido pelo usuário.')
            return 0
        else:
            return num
        
numero = leiaInt('Digite um número Int: ')
numero2 = leiaFloat('Digite um número Float: ')
print(f'O número Int digitado é {numero}. O número Float digitado é {numero2}.')