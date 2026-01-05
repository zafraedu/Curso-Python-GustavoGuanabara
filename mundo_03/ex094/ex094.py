from statistics import mean

pessoas = []
while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoa['sexo'] = str(input('Sexo: [M/F] ').strip().upper())
    while len(pessoa['sexo']) != 1 or pessoa['sexo'] not in 'MF':
        print('\033[31merror:\033[m Por favor, digite apenas M ou F.')
        pessoa['sexo'] = str(input('Sexo: [M/F] ').strip().upper())
    pessoa['idade'] = str(input('Idade: ')).strip()
    while not pessoa['idade'].isdigit():
        print('\033[31merror:\033[m Por favor, digite um valor numérico.')
        pessoa['idade'] = str(input('Idade: ')).strip()
    pessoa['idade'] = int(pessoa['idade'])
    pessoas.append(pessoa)

    validation = str(input('Quer continuar? [S/N] ')).strip().upper()
    while len(validation) != 1 or validation not in 'SN':
        print('\033[merror:\033[m Responda apenas S ou N.')
        validation = str(input('Quer continuar? [S/N] ')).strip().upper()
    if validation == 'N':
        break
print('-=' * 20)
print(f'A) Ao todo temos {len(pessoas)} cadastradas.')
print(f'B) A média de idade é de {mean(list(pessoa['idade'] for pessoa in pessoas)):.1f} anos.')
mulheres_cadastradas = [pessoa['nome'] for pessoa in pessoas if pessoa['sexo'] == 'F']
if mulheres_cadastradas:
    print('C) As mulheres cadastradas foram', end=' ')
    for nome in mulheres_cadastradas:
        print(nome, end=' ')
    print('.\n')
else:
    print('C) Nenhuma mulher foi cadastrada.')
print('D) Lista de pessoas com idade acima da média:')
media_idade = mean(list(pessoa['idade'] for pessoa in pessoas))
for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        for k, v in pessoa.items():
            print(f'\t{k} = {v};', end=' ')
        print()
print('<< ENCERRADO >>')
