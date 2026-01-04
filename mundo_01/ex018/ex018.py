from math import sin, cos, tan, radians

n = int(input('Ângulo: '))

soh = sin(radians(n))
cah = cos(radians(n))
toa = tan(radians(n))

print(f'Seno: {soh:.2f}\nCosseno: {cah:.2f}\nTangente: {toa:.2f}')
