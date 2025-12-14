# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e
# mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 Ate 30: Sobrepeso
# - 30 ate 40 Obesidade
# - Acima de 40: Obesidade Morbida

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
    print('Obesidade morbida')
