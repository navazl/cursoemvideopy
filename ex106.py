while True:
    ajuda = str(input('[FIM para terminar] help: ')).upper()
    help(ajuda)
    if ajuda == 'FIM':
        break
print('Obrigado por usar!')