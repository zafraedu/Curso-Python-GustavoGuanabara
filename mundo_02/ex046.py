# Faça um programa que mostre no tela uma contagem regressiva para o estouro de fogos de artificio,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
import emoji


for i in range(10, -1, -1):
    sleep(1)
    print(i)
print(f'{emoji.emojize(':fireworks:')}'
      f'{'\033[31m'}{'=-='*3}'
      f'{emoji.emojize(':fireworks:')}'
      f'{'\033[32m'}{'=-='*3}'
      f'{emoji.emojize(':fireworks:')}'
      f'{'\033[33m'}{'=-='*3}'
      f'{emoji.emojize(':fireworks:')}'
      f'{'\033[34m'}{'=-='*3}'
      f'{emoji.emojize(':fireworks:')}'
      f'{'\033[35m'}{'=-='*3}'
      f'{emoji.emojize(':fireworks:')}'
      f'{'\033[36m'}{'=-='*3}'
      f'{emoji.emojize(':fireworks:')}')
