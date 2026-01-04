from math import trunc

n = float(input('Number: '))

# print(f'O número {n} tem a parte inteira {n:.0f}.') # without module
print(f'O número {n} tem a parte inteira {trunc(n)}.')
