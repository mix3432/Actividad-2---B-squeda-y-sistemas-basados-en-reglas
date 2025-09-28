# IA Rutas SBC (Reglas + A*)

Sistema en Python que calcula rutas en un sistema de transporte masivo usando una base de conocimiento (reglas lógicas) y búsqueda A* con tres criterios:
- tiempo
- estaciones
- trasbordos

## Requisitos
- Python 3.9+ (recomendado 3.10+)
- (Opcional) pytest para pruebas

## Uso
python main.py --origen E1 --destino E9 --criterio tiempo
python main.py --origen E1 --destino E9 --criterio trasbordos
python main.py --origen E1 --destino E9 --criterio estaciones

## Resultados de ejemplo
Salidas en texto plano (UTF-8) dentro de `docs/`:
- docs/salida_tiempo.txt
- docs/salida_trasbordos.txt
- docs/salida_estaciones.txt
- docs/salida_tests.txt  (pytest)

## Probar
python -m pytest -q

## Estructura
- main.py  CLI
- knowledge_base.py  reglas y heurística
- search.py  A*
- data/network_sample.json  red de ejemplo
- tests/test_core.py  pruebas
- docs/  solo resultados (`salida_*.txt`)
