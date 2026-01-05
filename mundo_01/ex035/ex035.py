from colorama import Fore

r1 = float(input(f'{Fore.YELLOW}r1: {Fore.RESET}'))
r2 = float(input(f'{Fore.MAGENTA}r2: {Fore.RESET}'))
r3 = float(input(f'{Fore.CYAN}r3: {Fore.RESET}'))

if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('True')
else:
    print('False')

# if r1 + r2 > r3:
#     if r2 + r3 > r1:
#         if r3 + r1 > r2:
#             print('True')
#         else:
#             print('False')
#     else:
#         print('False')
# else:
#     print('False')
