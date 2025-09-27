"""
knowledge_base.py
-----------------
Base de conocimiento y motor de reglas (encadenamiento hacia adelante simple)
para un sistema inteligente basado en conocimiento (SBC) que apoya la
planificación de rutas en un sistema de transporte masivo local.
"""

from dataclasses import dataclass
from typing import Dict, List, Tuple, Set


@dataclass(frozen=True)
class Edge:
    origen: str
    destino: str
    tiempo_min: float
    linea: str


class KnowledgeBase:
    """
    Contiene hechos y aplica reglas para derivar una política de costos dinámica.
    """

    def __init__(self, nodos: Set[str], edges: List[Edge], pertenencia_linea: Dict[str, Set[str]]):
        self.nodos = nodos
        self.edges = edges
        self.pertenencia_linea = pertenencia_linea  # linea -> set(estacion)

        # Parámetros (ajustables):
        self.penalidad_trasbordo = 4.0  # minutos extra por cambio de línea
        self.penalidad_estacion = 1.0   # costo base por estación (criterio "estaciones")
        self.penalidad_trasbordo_unidades = 1.0  # costo base por trasbordo (criterio "trasbordos")

    # === Reglas Auxiliares ===

    def misma_linea(self, a: str, b: str, linea: str) -> bool:
        """R1: Verifica si dos estaciones pertenecen a una misma línea concreta."""
        return a in self.pertenencia_linea.get(linea, set()) and b in self.pertenencia_linea.get(linea, set())

    def hay_cambio_linea(self, linea_actual: str, linea_siguiente: str) -> bool:
        """R2: Detecta cambio de línea (trasbordo)."""
        return linea_actual != linea_siguiente

    # === Política de costo derivada por reglas ===

    def costo_arista(self, a: str, b: str, linea_actual: str, linea_siguiente: str, criterio: str, tiempo_min: float) -> float:
        """
        Aplica reglas para devolver el costo de ir de a -> b por una arista de 'linea_siguiente'.
        - criterio: 'tiempo' | 'estaciones' | 'trasbordos'
        """
        costo = 0.0

        if criterio == "tiempo":
            costo += tiempo_min
            if self.hay_cambio_linea(linea_actual, linea_siguiente):
                costo += self.penalidad_trasbordo  # R2
        elif criterio == "estaciones":
            costo += self.penalidad_estacion
            if self.hay_cambio_linea(linea_actual, linea_siguiente):
                costo += self.penalidad_estacion  # pequeño castigo por cambiar
        elif criterio == "trasbordos":
            # Solo cuenta trasbordos: moverse sin cambiar de línea ~0, cambiar de línea suma 1
            costo += 0.0
            if self.hay_cambio_linea(linea_actual, linea_siguiente):
                costo += self.penalidad_trasbordo_unidades
        else:
            raise ValueError("Criterio no soportado")

        return costo

    # === Heurística (para A*) ===

    def heuristica(self, actual: str, destino: str, criterio: str) -> float:
        """
        Estimación admisible simple.
        """
        if actual == destino:
            return 0.0

        if criterio == "tiempo":
            return 1.0
        elif criterio == "estaciones":
            return 1.0
        elif criterio == "trasbordos":
            return 0.0
        return 0.0
