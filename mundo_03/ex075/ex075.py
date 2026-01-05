numeros = ''
for i in range(4):
    numeros += input('Digite um numero: ')

tupla_str = tuple(numeros)
print(tupla_str)
print(f'O valor 9 apareceu {tupla_str.count('9')}{'vez' if tupla_str.count('9') == 1 else 'vezes'}')
print(f'pos valor 3: {tupla_str.index('3') if '3' in tupla_str else 'nao se encontra na lista'}')
print('Os valores pares digitados foram', len(tuple(x for x in tupla_str if int(x) % 2 == 0)))
