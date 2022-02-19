import random
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations, groupby
from networkx import Graph
import kruskal
import prim
import utils


def build_mst(graph: Graph, algorithm: str):
    edges = utils.get_edges(graph)
    if algorithm == 'prim':
        return prim.build_mst(edges)
    elif algorithm == 'kruskal':
        return kruskal.build_mst(edges)


G = gnp_random_connected_graph(zZZ, 1, True)

h = nx.Graph(utils.build_nx_graph(build_mst(G, 'prim')))
w = 0
for edge in h.edges(data=True):
    w += edge[-1]["weight"]

h = nx.Graph(utils.build_nx_graph(build_mst(G, 'kruskal')))
w2 = 0
for edge in h.edges(data=True):
    w2 += edge[-1]["weight"]
nx.draw(h, node_color='lightblue',
        with_labels=True,
        node_size=500)

plt.show()
