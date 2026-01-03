from utilidadesCeV import dado
from utilidadesCeV import moeda


p = dado.leiaDinheiro(input('Digite o preço: R$'))
moeda.resumo(p, 80, 35)
