"""
main.py
-------
CLI para planificar la mejor ruta entre dos estaciones usando un SBC
(reglas lógicas) + búsqueda A*.

Uso:
    python main.py --origen E1 --destino E9 --criterio tiempo
Criterios soportados: tiempo | estaciones | trasbordos
"""

import argparse
import json
from typing import Dict, Set, List
from knowledge_base import KnowledgeBase, Edge
from search import RoutePlanner


def cargar_red(path_json: str):
    with open(path_json, "r", encoding="utf-8") as f:
        data = json.load(f)
    estaciones = set(data["estaciones"])
    lineas = {k: set(v) for k, v in data["lineas"].items()}
    edges = [Edge(**e) for e in data["conexiones"]]
    return estaciones, lineas, edges


def imprimir_resultado(res: Dict):
    print("\n=== RESULTADO ===")
    print(f"Criterio: {res['criterio']}")
    print(f"Costo total: {res['costo_total']:.2f}")
    print(f"Nodos explorados: {res['nodos_explorados']}")
    print("\nRuta (estación -> línea usada -> costo paso):")
    for est, linea, c in res["ruta"]:
        linea_txt = linea if linea is not None else "-"
        print(f"  {est:>3}  |  {linea_txt:<2}  |  {c:.2f}")


def main():
    parser = argparse.ArgumentParser(description="SBC de rutas con A*")
    parser.add_argument("--origen", required=True, help="Estación de origen")
    parser.add_argument("--destino", required=True, help="Estación destino")
    parser.add_argument("--criterio", default="tiempo", choices=["tiempo", "estaciones", "trasbordos"])
    parser.add_argument("--red", default="data/network_sample.json", help="Ruta al JSON con la red")
    args = parser.parse_args()

    nodos, pertenencia_linea, edges = cargar_red(args.red)
    kb = KnowledgeBase(nodos=nodos, edges=edges, pertenencia_linea=pertenencia_linea)
    planner = RoutePlanner(kb)

    resultado = planner.a_star(args.origen, args.destino, args.criterio)
    imprimir_resultado(resultado)


if __name__ == "__main__":
    main()
