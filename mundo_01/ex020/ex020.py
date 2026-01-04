from random import shuffle

a1 = input('Primero aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')

alunos = [a1, a2, a3, a4]
shuffle(alunos)

print(f'A ordem de apresentação será\n{alunos}')
