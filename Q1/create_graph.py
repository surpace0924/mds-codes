import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

nodes = [x+y+z for x in ['A', 'T', 'C', 'G'] for y in ['A', 'T', 'C', 'G'] for z in ['A', 'T', 'C', 'G']]

write_str = ''
for u in nodes:
    for v in nodes:
        # uからvにエッジが引ける時
        if u[1:] == v[:-1]:
            label = v[0]
            if label == 'A':
                label = '0'
            if label == 'T':
                label = '1'
            if label == 'C':
                label = '2'
            if label == 'G':
                label = '3'
            tmp_str = u + ' ' + v + ' ' + label + '\n'

            # 禁止語は除外
            if "AAA" in tmp_str or "TTT" in tmp_str or "CCC" in tmp_str or "GGG" in tmp_str:
                continue

            write_str += tmp_str

f = open('2_debruijin.txt', 'w')
f.write(write_str)
f.close()