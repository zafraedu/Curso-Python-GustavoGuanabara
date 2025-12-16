# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitaçao novamente até um valor correto.

sexo = input('Digite:\n'
             '[\033[1mF\033[m] para Feminino\n'
             '[\033[1mM\033[m] para Masculino\n')
while 'M' != sexo.lstrip().upper()[0] != 'F':
    sexo = input('Digite:\n'
                 '[\033[1mF\033[m] para Feminino\n'
                 '[\033[1mM\033[m] para Masculino\n')
print('ACABOU')
