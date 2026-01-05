frase = str(input('Digite uma frase qualquer: ')).lower().replace(' ', '')

if frase == frase[::-1]:
    print('Esta frase SI es un palíndromo')
else:
    print('Esta frase NO es un palíndromo')

# reverse_frase = ''
# for i in range(len(frase), 0, -1):
#     reverse_frase += frase[i - 1]
# if reverse_frase == frase:
#     print('Esta frase SI es un palíndromo')
# else:
#     print('Esta frase NO es un palíndromo')
