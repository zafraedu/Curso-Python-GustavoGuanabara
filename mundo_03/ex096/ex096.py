# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

def area():
    print('Controle de Terrenos')
    print('-'*20)
    largura = float(input('Largura (m): '))
    comprimento = float(input('Comprimento (m): '))
    print(f'A area de um terreno {largura}x{comprimento} e de {largura * comprimento}m2')


area()
