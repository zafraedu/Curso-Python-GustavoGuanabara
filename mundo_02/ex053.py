# Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
# ex: de frente para tras == de tras para frente [a torre da derrota, arara, asacada da casa]

frase = str(input('Digite uma frase qualquer: ')).lower().replace(' ', '')

if frase == frase[::-1]:
    print('Esta frase SI es un palindromo')
else:
    print('Esta frase NO es un palindromo')

# reverse_frase = ''
# for i in range(len(frase), 0, -1):
#     reverse_frase += frase[i - 1]
# if reverse_frase == frase:
#     print('Esta frase SI es un palindromo')
# else:
#     print('Esta frase NO es un palindromo')

