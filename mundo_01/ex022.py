# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas
# - O nome com todas as letras minúsculas
# - Quantas letras ao todox (sem sonsiderar espaços)
# - Quantas letras tem o primeiro nome

nome = str(input('Qual é o seu nome? '))

print(nome.upper())
print(nome.lower())
print(len(nome.strip()) - nome.strip().count(' '))
print(len(nome.strip()[:nome.lstrip().find(' ')]))
