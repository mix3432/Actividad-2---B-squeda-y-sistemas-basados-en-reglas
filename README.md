# IA Rutas SBC

Sistema inteligente basado en conocimiento + búsqueda A* para obtener rutas óptimas en un sistema de transporte masivo.

## Requisitos
- Python 3.9+ (sin librerías externas)

## Ejecutar
python main.py --origen E1 --destino E9 --criterio tiempo
python main.py --origen E1 --destino E9 --criterio trasbordos
python main.py --origen E1 --destino E9 --criterio estaciones

## Probar
python -m pytest -q

## Estructura
- knowledge_base.py: reglas/costos/heurística
- search.py: A* apoyado en reglas
- data/network_sample.json: red de ejemplo
- tests/test_core.py: pruebas básicas
- docs/: reporte y guion de video

## Notas
- Edita data/network_sample.json para tu sistema real.
- Penalidades en KnowledgeBase: penalidad_trasbordo, penalidad_estacion, penalidad_trasbordo_unidades.
