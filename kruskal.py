from typing import List
import networkx as nx


class DSU:
    def __init__(self, vertex_count: int):
        self.parents: List[int] = list(range(vertex_count))
        self.ranks: List[int] = [1] * vertex_count

    def union(self, node1: int, node2: int):
        node1, node2 = self.find(node1), self.find(node2)
        if node1 != node2:
            if self.ranks[node1] < self.ranks[node2]:
                node1, node2 = node2, node1
            self.parents[node2] = node1
            self.ranks[node1] += self.ranks[node2]

    def find(self, node: int) -> int:
        while self.parents[node] != node:
            node = self.parents[node]
        return node


def build_mst(graph: nx.Graph) -> nx.Graph:
    dsu = DSU(len(graph))
    mst = nx.Graph()
    for node_from, node_to, _ in sorted(graph.edges(data=True), key=lambda x: x[2]['weight']):
        component_from, component_to = dsu.find(node_from), dsu.find(node_to)
        if component_from != component_to:
            dsu.union(component_from, component_to)
            mst.add_edge(node_from, node_to)
    return mst
