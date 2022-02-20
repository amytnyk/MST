from itertools import combinations, groupby
import random
import networkx as nx


def gnp_random_connected_graph(num_of_nodes: int,
                               completeness: float) -> nx.Graph:
    edges = combinations(range(num_of_nodes), 2)
    graph = nx.Graph()
    graph.add_nodes_from(range(num_of_nodes))

    for _, node_edges in groupby(edges, key=lambda x: x[0]):
        node_edges = list(node_edges)
        random_edge = random.choice(node_edges)
        graph.add_edge(*random_edge)
        for e in node_edges:
            if random.random() < completeness:
                graph.add_edge(*e)

    for (u, v, w) in graph.edges(data=True):
        w['weight'] = random.randint(0, 100)

    return graph
