# VRP-COMPLE
## Integrantes
- Dana Brigitte Vallejos Nesteres - U201910362
- Pietro Gerardo Minaya Mundines - U201718387
- Adrian  Chavez
- Bryan Vela
- Raquel Chavez
## Generacion del Data Set
- Para el problema VRP en su version de multiples puntos de distribución, vamos a requerir generar 2 data sets diferentes: Almacenes y Casas.
- La ubicacion de cada Almacen y Casa estara representado por un punto que se encuentra dentro de la ciudad
- Cada dataset sera guardado en un archivo csv
### Generacion del Data Set de Almacenes
- La generacion del data set de las casas sera por medio de una funcion, la cual me retornara una lista de listas, estas listas seran los puntos dentro del grafo
```python
%%file casas.py
import numpy as np
import numpy.random as npr

def generarCasas(cantidad):
  casas = npr.randint(0, 2000, (cantidad, 2), dtype=np.int)
  return casas
```
### Verificacion de puntos Duplicados
## Vehiculos de Entrega
## Espacio de Busqueda
### Espacio Inicial
### Estado Final
### Transiciones
## Algoritmos
### Dana Vallejos
### Pietro Minaya
### Adrian Chavez
### Raque Chavez
### Bryan Vela
## Reporte de Actividades
### Leyenda de Milestones
| # Milestone | Nombre |
|---|---|
| 1 |  Trabajo Parcial |
| 2 |  Hito 1 Trabajo Final |
| 3 |  Hito 2 Trabajo FInal |
| 4 |  Hito 3 Trabajo Final |
| 5 |  Hito 4 Trabajo Final |
| 6 |  Presentacion Trabajo Final |
### Leyenda de Issues
| # Issue | Nombre | # Milestone |
|---|---|---|
| 1 | Actualizar lista de integrantes | 1 |
| 2 | Generar Primera Version de Almacenes | 1 |
| 3 | Generar Primera Version de Puntos de Entrega | 1 |
| 4 | Verificar que no existan puntos duplicados | 1 |
| 5 | Generar descripción de datos de vehículos de entrega indicando según su criterio, calculo de costo. | 1 |
| 6 | Definir espacio de búsqueda, estado inicial, posible estado final, transiciones.  | 1 |
| 7 | Algoritmo de Dana Vallejos| 1 |
| 8 | Algoritmo de Pietro Minaya  | 1 |
| 9 | Algoritmo de Adrian Chavez  | 1 |
| 10 | Algoritmo de Raquel Chavez  | 1 |
|  11 | Algoritmo de Bryan Vela | 1 |
|  12 | Reporte de Actividades | 1 |
|  13 | Video en Youtube del Github  | 1 |
### Tabla de Responsabilidades
| # Issue  |  Pietro  |  Dana |  Bryan |  Raquel | Adrian |
|---|---|---|---|---|---|
| 1 | x | x | x | x | x |
| 2 |   | x |   |   |   |
| 3 | x |   |   |   |   |
| 4 |   |   | x |   |   |
| 5 |   |   |   | x |   |
| 6 |   |   |   |   | x |
| 7 |   | x |   |   |   |
| 8 | x |   |   |   |   |
| 9 |   |   |   |   | x |
| 10 |   |   |   | x |   |
|  11 |   |   | x |   |   |
|  12 | x |   |   |   |   |
|  13 | x |   |   |   |   |
## Videos de Exposicion
- Trabajo Parcial:
