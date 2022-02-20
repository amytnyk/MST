from typing import Callable
from networkx.algorithms import tree
from core.algorithms import algorithms
from utils import generator
import unittest


def check_algorithm(function: Callable):
    def check():
        checks = 50
        for i in range(checks):
            graph = generator.gnp_random_connected_graph(100, .5)
            mst1 = function(graph)
            for u, v, data in mst1.edges(data=True):
                data['weight'] = graph.get_edge_data(u, v)['weight']
            mst2 = tree.minimum_spanning_tree(graph, algorithm="prim")

            assert mst1.size(weight="weight") == mst2.size(weight="weight")
    return check


if __name__ == "__main__":
    suite = unittest.TestSuite()
    for name, func in algorithms().items():
        suite.addTest(unittest.FunctionTestCase(check_algorithm(func)))
    unittest.TextTestRunner().run(suite)
