# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while 1:
    n = int(input('Input a number: '))
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} X {i:<2} = {n * i}')
        i += 1
    print('+-'*20)
