numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte')

numero_usuario = int(input('Digite um número entre 0 e 20: '))
while numero_usuario not in range(0, 21):
    numero_usuario = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Voce digitou o numero {numeros[numero_usuario]}')
