# VRP-COMPLE
## Integrantes
- Dana Brigitte Vallejos Nesteres - U201910362
- Pietro Gerardo Minaya Mundines - U201718387
- Adrián Amir Chávez Berrocal-U201912855
- Bryan Deison Vela Alvarado - U20181A046
- Raquel Silvia Chávez Cruz - U201914478
## Introducción
- La complejidad de un algoritmo es la cantidad de tiempo que tarda un algoritmo en ejecutarse, en función de la longitud de la entrada. Mide el tiempo necesario para ejecutar cada instrucción de código en un algoritmo. Esto nos ayuda a comparar entre la efectividad de un algoritmo y otro, y decidir cuál es el que nos conviene implementar. En el presente trabajo buscaremos resolver el problema de enrutamiento de vehículos o VRP tomando en cuenta variables como el tiempo y el costo de entrega y optando por la mejor solución según lo analizado.

## Descripción del problema
- El problema que se busca resolver es el enrutamiento de vehículos o VRP. El VRP es una constante en el negocio de entregas. Sucede debido a las limitaciones de entrega y recursos que enfrentan las empresas de reparto al idear rutas de vehículos de costo mínimo. Con la propagación masiva de COVID-19, las empresas de entrega están manejando mayores volúmenes de entrega. El repentino aumento en las entregas ha hecho que el problema de enrutamiento de vehículos sea bastante difícil de resolver. Por eso, el objetivo de este proyecto es resolverlo de tal modo que se puedan reducir los costos operativos y mejorar la calidad de los servicios de entrega.
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


##  Espacio de Busqueda
- El espacio de busqueda es el dominio por el cual un algoritmo busca dar una solución.
-  Para el presente problema, primero debemos definir los elementos que van a afectar nuestro espacio de búsqueda y estos son:
	1. Ciudad: Representado por un grafo del tipo grilla de 2000x2000
	2. Almacenes y Casas: Reprresentados por un nodo del grafo
	3. Vehiculos de Transporte
### Estado Inicial
- Es el estado en el que va a comenzar a correr nuestro algoritmo, en el problema VRP sera el siguiente:
![enter image description here](http://memetic-computing.org/lescas/sites/all/images/img149.jpg)
### Estado Final:
- Es el estado objetivo, al que debe llegar nuestro algoritmo, para nuestro problema sera el siguiente:
![enter image description here](http://myweb.sabanciuniv.edu/msadati/files/2021/03/MDVRP-p08.png)
### Estados Transitorios
- Son los estados intermedios por los cuales van a pasar desde el estado inicial al estado final.
## Algoritmos
### Dana Vallejos
Topic | Desc
-|-
Autor | Dana vallejos
Técnica principal | Backtracking
Mi idea para resolver este problema es medir las distancias más cortas entre puntos (entre el almacén y los puntos de entrega) y en caso sobrepase una distancia, saltarnos ese punto de entrega y asignarlo al siguiente almacén más cercano. Una vez que llega a zonear todo, se aplica el algoritmo bfs y así unir toda la zona y resolver el problema. La complejidad esperada es de: O (|A|*|V|2)
### Pietro Minaya
Topic | Desc
-|-
Autor | Pietro Minaya
Técnica principal | Divide y Venceras

Mi idea para resolver este problema es dividir mi espacio de busqueda por zonas, ya que por ejemplo para resolver el VRP con 4 zonas debo reslver el VRP de 2 zonas, asi hasta llegar al caso base que seria resolver el VRP de 1 zona y con ello aplicar un algoritmo de pathing que puede ser Djikstra para poder determinar la ruta mas corta para poder unir una zona, y asi para todas las zonas. La complejidad esperada es de: O(|A| log |V|)*|V|
### Adrian Chavez
Topic | Desc
-|-
Autor | Adrián Chávez
Técnica principal | Backtracking

Mi idea para resolver la problemática planteada es calcular la distancia más corta entre los nodos, más específico, entre los almacenes y los puntos de entrega. En caso un punto de entrega sobrepase el límite establecido, se salta ese nodo y se asigna al almacén más cercano y, de esta manera, se cubren todos los puntos para aplicar el algoritmo de orden topológico y se puedan unir todas las zonas para tener un panorama completo y resuelto del problema. La complejidad esperada es de: O (|A|*(|V|^2))
### Raque Chavez
Topic | Desc
-|-
Autor | Raquel Chavez
Técnica principal | Fuerza Bruta

Mi idea para resolver este problema es dividir mi espacio de busqueda por zonas por medio de un algoritmo de fuerza bruta que mida todas las distancias entre todos los puntos de los almacenes y las casas.  Una vez haiga asignado a cada casa a un podria ejecutar un algoritmo de BFS el cual me retorne la ruta mas corta para unir ese "sub grafo". La complejidad esperada seria de 0(|V|^3)
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
