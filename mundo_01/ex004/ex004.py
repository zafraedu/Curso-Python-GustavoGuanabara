text = input('Digite algo: ')

print(type(text))
print('alphanumeric: ', text.isalnum())
print('numeric: ', text.isnumeric())
print('alphabet: ', text.isalpha())
print('title : ', text.istitle())
print('minusculas: ', text.islower())
print('maiusculas: ', text.isupper())
print('only space: ', text.isspace())
print('float : ', text.isdecimal())
print('tabla ASCII: ', text.isascii())



