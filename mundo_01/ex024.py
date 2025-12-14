# Crie um programa que leia o nome de uma cidade e diga se ela come\a ou nao com o nome "SANTO"

nome = input('Cidade: ')
print('SANTO'  == nome.upper().strip()[:5])
