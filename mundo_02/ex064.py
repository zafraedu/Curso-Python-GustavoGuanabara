# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

count = 0
n = int(input('Digite um numero [999 para parar]: '))
result = 0
while n != 999:
    if n != 999:
        result += n
        count += 1
    n = int(input('Digite um numero [999 para parar]: '))
print(f'{count} numeros foram digitados e a soma entre todos da {result}')