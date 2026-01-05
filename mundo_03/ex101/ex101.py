#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano_nas: int):
    from datetime import date
    idade = date.today().year - ano_nas
    if 18 <= idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    else:
        return f'Com {idade} anos: VOTO OPCIONAL'


print('-' * 30)
ano_nascimento = int(input('Em que ano voce nasceu? '))
print(voto(ano_nascimento))
