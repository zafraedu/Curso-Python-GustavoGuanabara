# O mesmo professor do desafio anterior quer sortear a ordem de apresentaçao de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

from random import shuffle, random

a1 = input('Primero aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

alunos = [a1, a2, a3, a4]
shuffle(alunos)

print(f'A ordem de apresentaçao será\n{alunos}')
