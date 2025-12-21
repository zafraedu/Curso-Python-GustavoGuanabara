# Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero_usuario = int(input('Digite um número entre 0 e 20: '))
while numero_usuario not in range(0, 21):
    numero_usuario = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Voce digitou o numero {numeros[numero_usuario]}')