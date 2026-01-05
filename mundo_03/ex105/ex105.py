def notas(*marks, sit=False) -> dict:
    """
    Função para analisar notas e situações de vários alunos.
    :param marks: Uma ou mais notas dos alunos (aceita várias).
    :param sit: (opcional) indica se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    notas_dict =  {
        'maior': max(marks),
        'menor': min(marks),
        'média': sum(marks) / len(marks)
    }
    if sit:
        if notas_dict['média'] > 7:
            notas_dict['situação'] = 'BOA'
        elif notas_dict['média'] < 5:
            notas_dict['situação'] = 'RUIM'
        else:
            notas_dict['situação'] = 'RAZOÁVEL'
    return notas_dict


print(notas(5.5, 2.5, 10, 6.5, sit=True))
help(notas)
