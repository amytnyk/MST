import argparse
from itertools import product
from timeit import timeit
from core.algorithms import algorithms
from typing import Callable
from utils.progressbar import SingleProgressBar
from utils import generator


def run(func: Callable, name: str, vertex_count: int, density: float, iters: int):
    time_taken = 0

    for _ in SingleProgressBar(range(iters), f'V={vertex_count}, D={density} ({name})'):
        graph = generator.gnp_random_connected_graph(vertex_count, density)
        time_taken += timeit(lambda: func(graph), number=1)

    return time_taken / iters


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vertex_count_interval", type=int, default=10)
    parser.add_argument("--vertex_count", type=int, default=1000)
    parser.add_argument("--iters", type=int, default=100)
    args = parser.parse_args()

    results = [['vertex_count', 'density', 'algorithm', 'time']]
    vertices = range(args.vertex_count_interval, args.vertex_count + 1, args.vertex_count_interval)
    densities = [0.1, 0.5, 0.9]
    for vertex_count, density, (name, func) in product(vertices, densities, algorithms().items()):
        time = run(func, name, vertex_count, density, args.iters)
        results.append(list(map(str, [vertex_count, density, name, time])))

        with open('../results/results.csv', 'w', encoding='utf-8') as file:
            file.write('\n'.join(map(lambda x: ','.join(x), results)))
        print()


if __name__ == "__main__":
    main()