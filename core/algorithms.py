from typing import Dict, Callable
from core import kruskal
from core import prim


def algorithms() -> Dict[str, Callable]:
    return {'prim': prim.build_mst, 'kruskal': kruskal.build_mst}
