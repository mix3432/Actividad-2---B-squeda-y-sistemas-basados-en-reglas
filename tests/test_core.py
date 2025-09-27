import json
from knowledge_base import KnowledgeBase, Edge
from search import RoutePlanner


def build_sample():
    data = json.load(open("data/network_sample.json", encoding="utf-8"))
    estaciones = set(data["estaciones"])
    lineas = {k: set(v) for k, v in data["lineas"].items()}
    edges = [Edge(**e) for e in data["conexiones"]]
    kb = KnowledgeBase(estaciones, edges, lineas)
    return kb, RoutePlanner(kb)


def test_tiempo_path():
    kb, rp = build_sample()
    res = rp.a_star("E1", "E9", "tiempo")
    assert res["ruta"][0][0] == "E1"
    assert res["ruta"][-1][0] == "E9"
    assert res["costo_total"] > 0.0


def test_estaciones_path():
    kb, rp = build_sample()
    res = rp.a_star("E1", "E9", "estaciones")
    assert len(res["ruta"]) >= 2


def test_trasbordos_path():
    kb, rp = build_sample()
    res = rp.a_star("E1", "E9", "trasbordos")
    assert res["costo_total"] >= 1.0
