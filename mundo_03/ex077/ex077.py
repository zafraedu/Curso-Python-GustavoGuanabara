palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR')

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos', end=' ')
    for l in palavra:
        if l.lower() in 'aeiou':
            print(l.upper(), end=' ')
