"""
search.py
---------
Búsqueda A* usando la política de costos y heurística provistas por la
base de conocimiento (KnowledgeBase). Se asume grafo dirigido no negativo.
"""

from typing import Dict, List, Tuple, Optional
from heapq import heappush, heappop
from knowledge_base import KnowledgeBase, Edge


class RoutePlanner:
    """
    Planificador que ejecuta A* sobre el grafo y consulta a la KB para
    calcular costos de transición y heurística.
    """

    def __init__(self, kb: KnowledgeBase):
        self.kb = kb
        # construir adyacencias: nodo -> List[(destino, tiempo_min, linea)]
        self.adj: Dict[str, List[Tuple[str, float, str]]] = {}
        for e in self.kb.edges:
            self.adj.setdefault(e.origen, []).append((e.destino, e.tiempo_min, e.linea))
            # si el sistema es bidireccional, descomentar la siguiente línea:
            self.adj.setdefault(e.destino, []).append((e.origen, e.tiempo_min, e.linea))

    def a_star(self, origen: str, destino: str, criterio: str) -> Dict:
        """
        Retorna un dict con la ruta, costo acumulado según criterio y metadatos.
        """
        if origen not in self.adj or destino not in self.kb.nodos:
            raise ValueError("Origen/Destino no válidos en la red")

        # Cada estado: (estacion, linea_actual)
        start_state = (origen, None)

        open_heap: List[Tuple[float, Tuple[str, Optional[str]]]] = []
        heappush(open_heap, (0.0, start_state))

        g_cost: Dict[Tuple[str, Optional[str]], float] = {start_state: 0.0}
        came_from: Dict[Tuple[str, Optional[str]], Tuple[Tuple[str, Optional[str]], float, str]] = {}

        while open_heap:
            _, (u, linea_u) = heappop(open_heap)

            if u == destino:
                # reconstruir camino
                path = []
                estado = (u, linea_u)
                while estado in came_from:
                    prev, costo_step, linea_usada = came_from[estado]
                    path.append((estado[0], linea_usada, costo_step))
                    estado = prev
                path.append((origen, None, 0.0))
                path.reverse()

                total_cost = g_cost[(u, linea_u)]
                return {
                    "ruta": path,  # [(estacion, linea, costo_step)]
                    "costo_total": total_cost,
                    "criterio": criterio,
                    "nodos_explorados": len(g_cost)
                }

            for v, tiempo_min, linea_v in self.adj.get(u, []):
                # costo de transición segun KB + criterio
                costo_step = self.kb.costo_arista(
                    a=u, b=v,
                    linea_actual=linea_u if linea_u is not None else linea_v,
                    linea_siguiente=linea_v,
                    criterio=criterio,
                    tiempo_min=tiempo_min
                )
                new_state = (v, linea_v)
                tentative = g_cost[(u, linea_u)] + costo_step
                if tentative < g_cost.get(new_state, float("inf")):
                    g_cost[new_state] = tentative
                    came_from[new_state] = ((u, linea_u), costo_step, linea_v)
                    f = tentative + self.kb.heuristica(v, destino, criterio)
                    heappush(open_heap, (f, new_state))

        raise RuntimeError("No se encontró ruta (grafo desconectado o criterio imposible).")


