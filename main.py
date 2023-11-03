from Classes_Xadrez import Peça, Tabuleiro
from utils import verifica_peça_no_tabuleiro

import numpy as np

turno=0

tab = Tabuleiro()
P1 = Peça([4, 4], 'P1', tab)
P2 = Peça([3, 4], 'P2', tab)
mapeamento_peças = {'P1': P1, 'P2': P2}

print(tab.get_estado())


while True:
    peça_desejada = input('Peça: ')
    peça_desejada = verifica_peça_no_tabuleiro(mapeamento_peças, peça_desejada)

    peça_movendo = mapeamento_peças[peça_desejada]
    pos_atual = peça_movendo.get_posi()
    pos_desejada = list(map(int,input('Digite a posição desejada, para selecionar outra peça, digite -1: ').split()))
    if pos_desejada[0] == -1:
        #recomeça o loop
        continue

    peça_movendo.set_posi(pos_atual, pos_desejada)

    print(tab.get_estado())