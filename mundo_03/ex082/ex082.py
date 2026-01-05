numeros = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    validation = input('Quer continuar ? [S/N] ')
    if validation.lstrip().lower()[0] == 'n':
        break
print('='*30)
print('Lista completa:', numeros)
print('Valores PARES:', list(i for i in numeros if not i % 2))
print('Valores ÍMPARES:', list(i for i in numeros if i % 2))
