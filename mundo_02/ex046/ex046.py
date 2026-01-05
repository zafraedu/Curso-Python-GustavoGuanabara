from time import sleep
from emoji import emojize

for i in range(10, -1, -1):
    sleep(1)
    print(i, end=' ')
print()
print(f'{emojize(':fireworks:')}'
      f'{'\033[31m'}{'=-='*3}'
      f'{emojize(':fireworks:')}'
      f'{'\033[32m'}{'=-='*3}'
      f'{emojize(':fireworks:')}'
      f'{'\033[33m'}{'=-='*3}'
      f'{emojize(':fireworks:')}'
      f'{'\033[34m'}{'=-='*3}'
      f'{emojize(':fireworks:')}'
      f'{'\033[35m'}{'=-='*3}'
      f'{emojize(':fireworks:')}'
      f'{'\033[36m'}{'=-='*3}'
      f'{emojize(':fireworks:')}')
