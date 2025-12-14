# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2m(sqrt)

largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura * altura
q_litro = area / 2

print(f'Será necessario {q_litro} litros de tinta para pintar {area} metros cuadrados')
