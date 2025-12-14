# Faça um programa que leia uma frase pelo teclado e mostre:
# - Quantas vezes aparece a letra "A".
# - Em que posiçao ela aparece a primera vez.
# - Em que posiçao ela aparece a última vez.

frase = 'Uma fraze no teclado'
frase = frase.strip()

print(f'A frase tem {frase.upper().count("A")} letras "A".')
print(f'A primeira letra "A" se encontra na posiçao {frase.upper().find('A')}')
print(f'A última letra "A" se encontra na posiçao {frase.upper().rfind('A')}')
