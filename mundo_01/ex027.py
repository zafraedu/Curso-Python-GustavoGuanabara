# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
#
# Ex: Ana Maria de Souza
# primeiro: Ana
# último: Souza

nome = input('Nome: ')
nome = nome.split()

print(f'primeiro: {nome[0]}')
print(f'último: {nome[len(nome) - 1]}')
