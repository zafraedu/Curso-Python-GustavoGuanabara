# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informaçoes sobre ele

text = input('Digite algo: ')

print(type(text))
print(isinstance(text, str))
print('alphanumeric: ', text.isalnum())
print('numeric: ', text.isnumeric())
print('alphabet: ', text.isalpha())
print('title : ', text.istitle())
print('minusculas: ', text.islower())
print('maiusculas: ', text.isupper())
print('only space: ', text.isspace())
print('float : ', text.isdecimal())
print('tabla ASCII: ', text.isascii())



