# Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou nao formar um triangulo

from mycolours import color

r1 = float(input(f'{color['y']}r1: {color['none']}'))
r2 = float(input(f'{color['m']}r2: {color['none']}'))
r3 = float(input(f'{color['c']}r3: {color['none']}'))

# if r1 + r2 > r3:
#     if r2 + r3 > r1:
#         if r3 + r1 > r2:
#             print('True')
#         else:
#             print('False')
#     else:
#         print('False')
# else:
#     print('False')

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('True')
else:
    print('False')