from typing import Dict, Callable
import kruskal
import prim


def algorithms() -> Dict[str, Callable]:
    return {'prim': prim.build_mst, 'kruskal': kruskal.build_mst}
