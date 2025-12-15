# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.

n = int(input('Digite um numero: '))

for i in range(1, 11):
    print(f'{n} X {i:2} = {n * i}')
