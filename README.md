# VRP-COMPLE
## Integrantes
- Dana Brigitte Vallejos Nesteres - U201910362
- Pietro Gerardo Minaya Mundines - U201718387
- Adrián Amir Chávez Berrocal-U201912855
- Bryan Deison Vela Alvarado - U20181A046
- Raquel Chavez
## Generacion del Data Set
- Para el problema VRP en su version de multiples puntos de distribución, vamos a requerir generar 2 data sets diferentes: Almacenes y Casas.
- La ubicacion de cada Almacen y Casa estara representado por un punto que se encuentra dentro de la ciudad
- Cada dataset sera guardado en un archivo csv
### Generacion del Data Set de Almacenes
- Para generar el data set de los almacenes vamos a usar una funcion en python la cual nos va a retornar una lista de listas, estas listas van a contener 2 elementos [x , y] los cuales me representan a las coordenadas x e y dentro del plano cartesiano respectivamente.
```python
%%file almacenes.py
import numpy as np
import numpy.random as npr

def generar_almacenes(cantidad):
  almacenes = npr.randint(0, 2000, (cantidad, 2), dtype=np.int)
  return almacenes
```
### Generacion del Data Set de Casas
- La generacion del data set de las casas sera por medio de una funcion, la cual me retornara una lista de listas, estas listas seran los puntos dentro del grafo
```python
%%file casas.py
import numpy as np
import numpy.random as npr

def generarCasas(cantidad):
  casas = npr.randint(0, 2000, (cantidad, 2), dtype=np.int)
  return casas
```
### Verificacion de los puntos duplicados
- Para verificar que no existan puntos duplicados lo que haremos es primero obtener las 2 listas de puntos con las funciones previamente creadas. Despues, vamos a verificar si algun punto que este dentro de la lista de casas se encuentra dentro de la lista de almacenes, en caso se encuentre generaremos un nuevo punto hasta que no se duplique. Una vez que ambas listas esten sin repeticiones procederemos a generar los archivos csv
```python
%%file generacion.py
import casas as c
import almacenes as a
import numpy as np
import numpy.random as npr

casas = c.generarCasas(2500)
almacenes = a.generar_almacenes(200)
for i, _ in enumerate(casas):
  while casas[i] in almacenes:
    casas[i] = npr.randint(0, 2000, (1, 2), dtype=np.int)
np.savetxt('casas.csv', casas, fmt="%i", delimiter=",", header="x,y", comments="")
np.savetxt('almacenes.csv', almacenes, fmt="%i", delimiter=",", header="x,y", comments="")
```

## Vehiculos de Entrega
 - Es un elemento importante en la resolucion del VRP ya que estos nos determinaran el coste que existe entre las rutas.
 - Despues de una investigacion con distintas fuentes, las caracteristicas mas importantes son:
	 1. Capacidad de carga del vehículo
	 2. Costo por  unidad recorrida
### Capacidad de carga
- La capacidad de carga promedio de los vehiculos de transporte de alimentos es de 20 toneladas
### Costo por unidad recorrida
- El costo por unidad recorrida depende de muchos factores, pero para simplificar el problema las vamos a resumir en dos:
	1. Costo del combustible
	2. Combustible consumido por unidad recorrida
- Para el costo del combustible, normalmente se usa el Gasohol 90 que en el mercado actual esta costando S/.15.00 el galon
- En promedio estos vehiculos consumen cerca de 0.005 a 0.01 galones por unidad recorrida, esto depende de el tipo de terreno y la velocidad a la que viaja, que por motivos de simplificación del problema asumiremos que los vehiculos viajaran a una velocidad constante de 1 unidad por segundo y el terreno es liso, por lo que nuestros vehiculos consumiran  0.005 galones por unidad recorrida.
- Considerando que el costo del galon es de S/.15.00 y nos cuesta recorrer una unidad 0.005 galones, tendriamos un costo total de: S/.0.075 por unidad recorrida.

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
