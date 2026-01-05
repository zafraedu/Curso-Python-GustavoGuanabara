# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numeros = list()
while 1:
    numeros.append(int(input('Digite um valor: ')))

    validation = input('Quer continual ? [S/N] ')
    if validation in 'nN':
        break
numeros.sort(reverse=True)
print(f'Foram digitados {len(numeros)} números.')
print('Os valores em ordem decrescente sao', numeros)
print('O valor 5 esta na lista' if numeros.count(5) else 'O valor 5 nao esta na lista')