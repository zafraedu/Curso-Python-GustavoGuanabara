nome = str(input('Qual é o seu nome? '))

print(nome.upper())
print(nome.lower())
print(len(nome.strip()) - nome.strip().count(' '))
print(len(nome.strip()[:nome.lstrip().find(' ')]))
