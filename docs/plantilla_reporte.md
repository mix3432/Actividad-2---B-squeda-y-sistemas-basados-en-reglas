# Sistema Inteligente Basado en Conocimiento para Rutas de Transporte Masivo

**Curso:** Sistemas Inteligentes basados en conocimiento  
**Integrantes:** (Nombres, códigos)  
**Repositorio Git:** <URL>  
**Video (5 min):** <URL>

## 1. Introducción
Breve contexto del sistema de transporte y la motivación.

## 2. Marco teórico
- Representación del conocimiento con reglas (cap. 2 y 3, Benítez, 2014).
- Búsquedas heurísticas (cap. 9, Benítez, 2014).
- A* y admisibilidad de heurísticas.

## 3. Base de conocimiento
- Hechos: estaciones, líneas, conexiones, tiempos.
- Reglas:
  - R1: misma línea  sin penalidad de trasbordo.
  - R2: cambio de línea  penalidad de trasbordo.
  - R3: heurística conservadora para A*.

## 4. Diseño e implementación
- Arquitectura (módulos).
- Datos `data/network_sample.json`.
- Parámetros ajustables.

## 5. Experimentos y pruebas
- Casos: E1E9 con criterios `tiempo`, `estaciones`, `trasbordos`.
- Capturas de consola.
- Resultados de `pytest`.

## 6. Discusión
Ventajas/limitaciones y mejoras futuras.

## 7. Conclusiones
Conclusión sobre reglas + A*.

## 8. Referencias
- Benítez, R. (2014). *Inteligencia artificial avanzada*. Barcelona: Editorial UOC.
- Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.
- Pearl, J. (1984). *Heuristics: Intelligent Search Strategies for Computer Problem Solving*. Addison-Wesley.
