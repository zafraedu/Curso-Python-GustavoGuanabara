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
