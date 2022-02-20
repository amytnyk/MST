import math
import heapq
import networkx as nx


def build_mst(graph: nx.Graph) -> nx.Graph:
    weights = [.0] + [math.inf] * (len(graph) - 1)
    mst = [None] * len(graph)
    visited = [False] * len(graph)
    edges_to_add = [(0, 0)]

    while edges_to_add:
        _, vertex = edges_to_add[0]
        heapq.heappop(edges_to_add)

        if visited[vertex]:
            continue
        visited[vertex] = True

        for _, node, data in graph.edges([vertex], data=True):
            weight = data['weight']
            if weight < weights[node] and not visited[node]:
                weights[node] = weight
                mst[node] = vertex
                heapq.heappush(edges_to_add, (weight, node))

    final_mst = nx.Graph()
    for i, u in enumerate(mst[1:]):
        final_mst.add_edge(i + 1, u)
    return final_mst

