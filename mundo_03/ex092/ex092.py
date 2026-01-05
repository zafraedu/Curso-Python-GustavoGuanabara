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
