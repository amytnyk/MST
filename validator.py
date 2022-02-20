from typing import Callable
from networkx.algorithms import tree
from algorithms import algorithms
import generator


def check_algorithm(func: Callable) -> bool:
    checks = 100
    for i in range(checks):
        graph = generator.gnp_random_connected_graph(100, .5)
        mst1 = func(graph)
        for u, v, data in mst1.edges(data=True):
            data['weight'] = graph.get_edge_data(u, v)['weight']
        mst2 = tree.minimum_spanning_tree(graph, algorithm="prim")
        if mst1.size(weight="weight") != mst2.size(weight="weight"):
            return False
    return True


if __name__ == "__main__":
    for name, func in algorithms().items():
        print(f"Validating \033[1;33;92m{name}\x1b[0m ... ", end='')
        if check_algorithm(func):
            print("\033[1;33;92mOK\033[0m")
        else:
            print("\033[1;33;91mFail\033[0m")
