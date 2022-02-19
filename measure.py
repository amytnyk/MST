import argparse
from timeit import timeit
from networkx.algorithms import tree
import generator
import kruskal
import prim
from typing import Callable


def validate(func: Callable) -> bool:
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


def run(func: Callable, vertex_count: int, density: float):
    time_taken = 0
    iters = 60

    length = 120
    char = '\u2501'
    for i in range(iters):
        graph = generator.gnp_random_connected_graph(vertex_count, density)
        time_taken += timeit(lambda: func(graph), number=1)
        print(f"\r\033[1;34m{int(i / iters * length) * char}\033[90m{int(length - i / iters * length) * char}\033[0m", end='')

    return time_taken / iters


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("vertex_count", type=int)
    parser.add_argument("density", type=float)
    args = parser.parse_args()
    for name, func in {'prim': prim.build_mst, 'kruskal': kruskal.build_mst}.items():
        print(f"Validating {name} ... ", end='')
        if validate(func):
            print("\033[1;33;92mOK\033[0m")
            print(f"Testing \033[1;33;92m{name}\x1b[0m:")
            print(f"\nTime taken: {run(func, args.vertex_count, args.density):.5f}s")
        else:
            print("\033[1;33;91mFail\033[0m")


if __name__ == "__main__":
    main()
