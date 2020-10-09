def voto(ano):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    if 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'



ano_de_nascimento = int(input('Em que ano você nasceu? '))
print(voto(ano_de_nascimento))