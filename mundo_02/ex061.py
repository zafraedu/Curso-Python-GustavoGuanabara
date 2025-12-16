# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input('Primeiro termo da progressao aritimetica: '))
razao = int(input('Razao da progressao aritimetica: '))
decimo = primeiro_termo + (10 - 1) * razao

while primeiro_termo <= decimo:
    print(primeiro_termo, end = ' ')
    primeiro_termo += razao
