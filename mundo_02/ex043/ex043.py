kg = float(input('Digite seu peso em Kilos '))
m = float(input('Digite sua altura em Metros '))
imc = kg / (m * m)

if imc < 18.5:
    print('Abaixo do peso')
elif  18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobre peso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
