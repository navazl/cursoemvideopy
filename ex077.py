palavras = 'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro'
for i in palavras:
    print(f'\nNa palavra {i.upper()} tem: ', end='')
    for letra in i:
        if letra.lower() in 'aeiou':
            print(letra, end =' ')