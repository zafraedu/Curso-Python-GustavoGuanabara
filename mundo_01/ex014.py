# Escreva um programa que converta uma temperatura digitada em °C e converta en °F.

c = float(input('Temperatura em °C: '))
f = (c * 1.8) + 32

print(f'A temperatura de {c}°C corresponde a {f:.1f}°F.')