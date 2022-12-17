import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

# ノード配置
pos = [None, None, None, None]
pos[0] = {'0001': (np.cos(0*2*np.pi/7), np.sin(0*2*np.pi/7)),
       '0010': (np.cos(1*2*np.pi/7), np.sin(1*2*np.pi/7)),
       '0100': (np.cos(2*2*np.pi/7), np.sin(2*2*np.pi/7)),
       '0101': (np.cos(3*2*np.pi/7), np.sin(3*2*np.pi/7)),
       '1000': (np.cos(4*2*np.pi/7), np.sin(4*2*np.pi/7)),
       '1001': (np.cos(5*2*np.pi/7), np.sin(5*2*np.pi/7)),
       '1010': (np.cos(6*2*np.pi/7), np.sin(6*2*np.pi/7))}

pos[1] = {'ε': (0.0, 0.0),
       '1': (1.0, 0.0),
       '0': (2.0, 0.0),
       '00': (3.0, 0.0),
       '000': (4.0, 0.0)}

nodes_2 = [x+y+z for x in ['A', 'T', 'C', 'G'] for y in ['A', 'T', 'C', 'G'] for z in ['A', 'T', 'C', 'G']]
nodes_2.remove('AAA')
nodes_2.remove('TTT')
nodes_2.remove('CCC')
nodes_2.remove('GGG')
tmp_p = {}
for i, node in enumerate(nodes_2):
      tmp_p.update({node: (2*np.cos(i*2*np.pi/len(nodes_2)), 2*np.sin(i*2*np.pi/len(nodes_2)))})
pos[2] = tmp_p

pos[3] = {'ε': (0.0, 0.0),
       'A': (1.0, 0.0),
       'T': (0.0, 1.0),
       'C': (-1.0, 0.0),
       'G': (0.0, -1.0)}




paths = ['1_debruijin.txt', '1_crochemore.txt', '2_debruijin.txt', '2_crochemore.txt']
for idx, path in enumerate(paths):
       plt.figure(figsize=(4,4))

       # 有向グラフの作成
       G = nx.DiGraph()

       # 重み付きのファイルの読み込み
       G = nx.read_weighted_edgelist(path, nodetype=str, create_using=nx.DiGraph)

       # エッジの色分け
       edge_labels = [str(int(w['weight'])) for i, j, w in G.edges(data=True)]
       edge_color = [e.replace('0', 'red') for e in edge_labels]
       edge_color = [e.replace('1', 'green') for e in edge_color]
       edge_color = [e.replace('2', 'orange') for e in edge_color]
       edge_color = [e.replace('3', 'purple') for e in edge_color]

       nx.draw_networkx(G, pos[idx], with_labels=True, edge_color=edge_color, alpha=1.0, connectionstyle="arc3, rad=0.3")

       # 表示
       plt.axis("off")
       plt.show()