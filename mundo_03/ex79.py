# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()
while  1:
    numero = int(input('Digite um valor '))
    if numero in numeros:
        print('Valor duplicado! Nao vou adicionar')
    else:
        numeros.append(numero)
    numeros.sort()

    validation = input('Quer continuar ? [S/N] ')
    if validation.lstrip()[0] in 'nN':
        break

print('Voce digitou os valores', numeros)
