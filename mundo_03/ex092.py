# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime
ano_atual = datetime.now().year

pessoa = {
    'nome': str(input('Nome: ')).strip().capitalize(),
    'idade': ano_atual - int(input('Ano de nacimento: ')),
    'ctps': int(input('Carteira de Trabalho (0 nao tem): '))
}
if pessoa['ctps']:
    pessoa['contratação'] = int(input('Ano de Contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = 35 - (ano_atual - pessoa['contratação']) + pessoa['idade']
print('-='*20)
for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')
