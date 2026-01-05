# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados.
# Ao final, mostre o conteúdo das três listas geradas.

numeros = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    validation = input('Quer continuar ? [S/N] ')
    if validation.lstrip().lower()[0] == 'n':
        break
print('='*30)
print('Lista completa:', numeros)
print('Valores PARES:', list(i for i in numeros if not i % 2))
print('Valores IMPARES:', list(i for i in numeros if i % 2))
