from datetime import date

year = int(input('Year: '))
if year == 0:
    year = date.today().year

if year % 4 == 0 and year % 100 != 100 or year % 400 == 0:
    print('True')
else:
    print('False')

# if year % 4:
#     print('False')
# else:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('True')
#         else:
#             print('False')
#     else:
#         print('True')
