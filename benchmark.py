import argparse
import os.path
from itertools import product
from timeit import timeit
from core.algorithms import algorithms
from typing import Callable, List
from utils.progressbar import SingleProgressBar
from utils import generator


def run(func: Callable, name: str, vertex_count: int, density: float, iters: int):
    time_taken = 0

    for _ in SingleProgressBar(range(iters), f'V={vertex_count}, D={density} ({name})'):
        graph = generator.gnp_random_connected_graph(vertex_count, density)
        time_taken += timeit(lambda: func(graph), number=1)

    return time_taken / iters


def load_results(no_cache: bool = False) -> List[List[str]]:
    if not no_cache and os.path.exists('results/results.csv'):
        with open('results/results.csv', 'r', encoding='utf-8') as file:
            return list(map(lambda x: x.split(','), filter(None, file.read().split('\n'))))
    return [['vertex_count', 'density', 'algorithm', 'time']]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vertex_count_interval", type=int, default=10)
    parser.add_argument("--vertex_count", type=int, default=1000)
    parser.add_argument("--iters", type=int, default=100)
    parser.add_argument("--no_cache", action='store_true')
    args = parser.parse_args()

    results = load_results(args.no_cache)
    vertices = range(args.vertex_count_interval, args.vertex_count + 1, args.vertex_count_interval)
    densities = [0.1, 0.5, 0.9]
    for vertex_count, density, (name, func) in product(vertices, densities, algorithms().items()):
        config = list(map(str, [vertex_count, density, name]))
        if not len(list(filter(lambda x: x[:3] == config[:3], results))):
            config.append(str(run(func, name, vertex_count, density, args.iters)))
            results.append(config)

            with open('results/results.csv', 'w', encoding='utf-8') as file:
                file.write('\n'.join(map(lambda x: ','.join(x), results)))
            print()


if __name__ == "__main__":
    main()
