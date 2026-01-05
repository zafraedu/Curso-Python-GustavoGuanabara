from mundo_03.ex115.utils import titulo, d_error

def show_users():
    try:
        with open('database.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(d_error['archivo'])
    else:
        titulo('PESSOAS CADASTRADAS')
        print(content)


def add_user():
    titulo('NOVO CADASTRO')

    name = ' '.join(str(input('Nome: ')).strip().title().split())
    while True:
        try:
            age = int(input('Idade: '))
        except ValueError:
            print(d_error['idade'])
        else:
            break

    with open('database.txt', 'a') as file:
        file.write(f'{name:<42}{age:<2} anos\n')


def select_function(option):
    if option == 1:
        show_users()
    else:
        add_user()
