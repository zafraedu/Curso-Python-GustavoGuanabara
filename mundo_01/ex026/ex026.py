frase = str(input('Digite um frase: ')).strip().upper()

print(f'A frase tem {frase.count("A")} letras "A".')
print(f'A primeira letra "A" se encontra na posição {frase.find('A')}')
print(f'A última letra "A" se encontra na posição {frase.rfind('A')}')
