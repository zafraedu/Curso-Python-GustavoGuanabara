# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um
# triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

c1 = float(input('Cateto oposto: '))
c2 = float(input('Cateto adjacente: '))
# h = (c1**2 + c2**2)**(1/2) # without module
h = hypot(c1, c2)
print(f'Hipotenusa: {h:.2f}')
