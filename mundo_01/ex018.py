# Faça um programa que leia um ângulo qualquer e
# mostre na tela o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians

n = int(input('Ângulo: '))

soh = sin(radians(n))
cah = cos(radians(n))
toa = tan(radians(n))

print(f'Seno: {soh}\nCosseno: {cah}\nTangente: {toa}')

