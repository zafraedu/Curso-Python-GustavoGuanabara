import requests  # PyPI install package


def url_funciona(url, timeout=5):
    try:
        requests.get(url, timeout=timeout)  # Sem um tempo limite, o programa poderia ficar esperando indefinidamente.
        return '\033[32mConsegui acessar o site do Pudim com sucesso!\033[m'
    except requests.exceptions.RequestException:
        return '\033[31mO site Pudim não esta acessível no momento'


print(url_funciona('https://pudim.com.br'))

# Você não precisa instalar nada. (Ele já vem com o Python)

# from urllib.request import urlopen
# from urllib.error import URLError, HTTPError
#
# try:
#     urlopen('https://pudim.com.br', timeout=5)
#     print('\033[32mConsegui acessar o site do Pudim com sucesso!\033[m')
# except (HTTPError, URLError):
#     print('\033[31mO site Pudim não está acessível no momento')
