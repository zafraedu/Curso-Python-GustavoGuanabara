def escreva(txt):
    print('-' * (len(txt) + 4))
    print(f'{txt:^{(len(txt) + 4)}}')
    print('-' * (len(txt) + 4))


escreva('hola')
escreva('eduardo zafra')
escreva('Curso de Python no Youtube')
