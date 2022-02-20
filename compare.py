import argparse
from timeit import timeit
from algorithms import algorithms
from typing import Callable
from progressbar import SingleProgressBar
import generator
import validator


def run(func: Callable, vertex_count: int, density: float):
    time_taken = 0
    iters = 100

    for _ in SingleProgressBar(range(iters), 'Testing'):
        graph = generator.gnp_random_connected_graph(vertex_count, density)
        time_taken += timeit(lambda: func(graph), number=1)

    return time_taken / iters


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("vertex_count", type=int)
    parser.add_argument("density", type=float)
    args = parser.parse_args()
    for name, func in algorithms().items():
        print(f"\n\033[1;33;92m{name}\x1b[0m: ")
        print(f"Validating ... ", end='')
        if validator.check_algorithm(func):
            print("\033[1;33;92mOK\033[0m")
            print(f"\nAverage time taken: {run(func, args.vertex_count, args.density):.5f}s")
        else:
            print("\033[1;33;91mFail\033[0m")


if __name__ == "__main__":
    main()
