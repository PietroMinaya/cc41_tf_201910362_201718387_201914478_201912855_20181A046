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
def generar_almacenes(cantidad, n_city):
  almacenes = npr.randint(0, n_city, (cantidad, 2), dtype=np.int)
  return almacenes
```
### Generacion del Data Set de Casas
- La generacion del data set de las casas sera por medio de una funcion, la cual me retornara una lista de listas, estas listas seran los puntos dentro del grafo
```python
def generarCasas(cantidad, n_city):
  casas = npr.randint(0, n_city, (cantidad, 2), dtype=np.int)
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
Algoritmo | Djikstra
Complejidad Temporal | O (E + V*logV)

La idea subyacente en este algoritmo consiste en ir explorando todos los caminos más cortos que parten del vértice origen y que llevan a todos los demás vértices; cuando se obtiene el camino más corto desde el vértice origen hasta el resto de los vértices que componen el grafo, el algoritmo se detiene. Se trata de una especialización de la búsqueda de costo uniforme y, como tal, no funciona en grafos con aristas de coste negativo (al elegir siempre el nodo con distancia menor, pueden quedar excluidos de la búsqueda nodos que en próximas iteraciones bajarían el costo general del camino al pasar por una arista con costo negativo)
#### Codigo Del Algoritmo
```py
def dijkstra(G, s):
  n = len(G)
  visited = [False]*n
  path = [None]*n
  cost = [math.inf]*n
  cost[s] = 0
  queue = [(0, s)]
  while queue:
    g_u, u = hq.heappop(queue)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        f = g_u + w
        if f < cost[v]:
          cost[v] = f
          path[v] = u
          hq.heappush(queue, (f, v))
  return path, cost
```
#### Procesamiento de Grupos con el Algoritmo:
```py
def procesar_grupo_dijkstra(grupo, plt=None, ncity=80):
  nodos = grupo["casas"]
  nodos.append(grupo["almacen"])
  label = list()
  for nodo in nodos:
    label.append(str(get_node(nodo, ncity)))
  grafo = [[] for _ in range(len(nodos))]
  for i, _ in enumerate(nodos):
    for j, _ in enumerate(nodos):
      if i == j: continue
      grafo[i].append((j, manhattan_distance(nodos[i], nodos[j])))
  path, cost = dijkstra(grafo, len(nodos) - 1)
  if(plt == None): return adjlShow(grafo, weighted=True, path=path, labels=label)
  else: 
    for i in range(len(path)):
      point1 = get_coord(int(label[i]), ncity)
      point2 = get_coord(int(label[path[i]]), ncity)
      plt.plot([point1[0], point2[0]], [point1[1], point2[1]])
```

### Pietro Minaya
Topic | Desc
-|-
Autor | Pietro Minaya
Algoritmo | Prim
Complejidad Temporal | O (n^2)

El algoritmo de Prim es un algoritmo dedicado a encontrar un arbol de expansion minima (MST por sus siglas en ingles), es decir, que va a buscar la forma en la cual poder unir todos los nodos de mi grafo para que se recorra con el menor costo posible. Este algoritmo es ideal para este problema ya que como contamos con carros ilimitados lo que debemos buscar es el MST para conectar todos los puntos con el menor costo posible.
#### Codigo Del Algoritmo
```py
def prim(G):
  n = len(G)
  visited = [False]*n
  path = [-1]*n
  cost = [math.inf]*n
  q = [(0, 0)]
  while q:
    _, u = hq.heappop(q)
    if not visited[u]:
      visited[u] = True
      for v, w in G[u]:
        if not visited[v] and w < cost[v]:
          cost[v] = w
          path[v] = u
          hq.heappush(q, (w, v))

  return path, cost
```
#### Procesamiento de Grupos con el Algoritmo:
```py
def procesar_grupo_prim(grupo, plt=None, ncity=80):
  nodos = grupo["casas"]
  nodos.append(grupo["almacen"])
  label = list()
  for nodo in nodos:
    label.append(str(get_node(nodo, ncity)))
  grafo = [[] for _ in range(len(nodos))]
  for i, _ in enumerate(nodos):
    for j, _ in enumerate(nodos):
      if i == j: continue
      grafo[i].append((j, manhattan_distance(nodos[i], nodos[j])))
  path, cost = prim(grafo)
  if(plt == None): return adjlShow(grafo, weighted=True, path=path, labels=label)
  else: 
    for i in range(len(path)):
      point1 = get_coord(int(label[i]), ncity)
      point2 = get_coord(int(label[path[i]]), ncity)
      plt.plot([point1[0], point2[0]], [point1[1], point2[1]])
```
### Adrian Chavez
Topic | Desc
-|-
Autor | Adrián Chávez
Algoritmo | Kruskal
Complejidad Temporal | O (|E|*log(|V|))

El algoritmo de Kruskal es un algoritmo de la teoría de grafos para encontrar un árbol recubridor mínimo en un grafo conexo y ponderado. Es decir, busca un subconjunto de aristas que, formando un árbol, incluyen todos los vértices y donde el valor de la suma de todas las aristas del árbol es el mínimo. Si el grafo no es conexo, entonces busca un bosque expandido mínimo (un árbol expandido mínimo para cada componente conexa).
#### Codigo Del Algoritmo
```py
def kruskal(G):
  n = len(G)
  edges = []
  for u in range(n):
    for v, w in G[u]:
      hq.heappush(edges, (w, u, v))
  uf = DisjointSet(n)
  T = []
  while edges and n > 0:
    w, u, v = hq.heappop(edges)
    if not uf.sameset(u, v):
      uf.union(u, v)
      T.append((u, v, w))
      n -= 1
  return T
```
#### Procesamiento de Grupos con el Algoritmo:
```py
def procesar_grupo_kruskal(grupo, plt=None, ncity=80):
  nodos = grupo["casas"]
  nodos.append(grupo["almacen"])
  label = list()
  for nodo in nodos:
    label.append(str(get_node(nodo, ncity)))
  label[-1] = str(get_node(nodo, ncity))
  grafo = [[] for _ in range(len(nodos))]
  for i, _ in enumerate(nodos):
    for j, _ in enumerate(nodos):
      if i == j: continue
      grafo[i].append((j, manhattan_distance(nodos[i], nodos[j])))
  T = kruskal(grafo)
  n = len(grafo)
  Gp = [[] for _ in range(n)]
  for u, v, _ in T:
    Gp[u].append(v)
    Gp[v].append(u)
  path = bfs(Gp, 10)
  if(plt == None): return adjlShow(grafo, weighted=True, path=path, labels=label)
  else: 
    for i in range(len(path)):
      if path[i] == None: continue
      point1 = get_coord(int(label[i]), ncity)
      point2 = get_coord(int(label[path[i]]), ncity)
      plt.plot([point1[0], point2[0]], [point1[1], point2[1]])
```
### Raquel Chavez
Topic | Desc
-|-
Autor | Raquel Chavez
Técnica principal | Bellman Ford
Complejidad Temporal | O (E*V)

Mi idea para resolver este problema es dividir mi espacio de busqueda por zonas por medio de un algoritmo de fuerza bruta que mida todas las distancias entre todos los puntos de los almacenes y las casas.  Una vez haiga asignado a cada casa a un podria ejecutar un algoritmo de BFS el cual me retorne la ruta mas corta para unir ese "sub grafo". La complejidad esperada seria de 0(|V|^3)
#### Codigo Del Algoritmo
```py
def bellmanFord(G, s):
  n = len(G)
  cost = [float('inf')]*n
  cost[s] = 0
  path = [-1]*n
  for _ in range(n-1):
    for u in range(n):
      for v, w in G[u]:
        if cost[u] + w < cost[v]:
          cost[v] = cost[u] + w
          path[v] = u
  for u in range(n):
    for v, w in G[u]:
      if cost[u] + w < cost[v]:
        return None, None
  return path, cost
```
#### Procesamiento de Grupos con el Algoritmo:
```py
def procesar_grupo_bellman_ford(grupo, plt=None, ncity=80):
  nodos = grupo["casas"]
  nodos.append(grupo["almacen"])
  label = list()
  for nodo in nodos:
    label.append(str(get_node(nodo, ncity)))
  grafo = [[] for _ in range(len(nodos))]
  for i, _ in enumerate(nodos):
    for j, _ in enumerate(nodos):
      if i == j: continue
      grafo[i].append((j, manhattan_distance(nodos[i], nodos[j])))
  path, cost = bellmanFord(grafo, len(nodos) - 1)
  if(plt == None): return adjlShow(grafo, weighted=True, path=path, labels=label)
  else: 
    for i in range(len(path)):
      point1 = get_coord(int(label[i]), ncity)
      point2 = get_coord(int(label[path[i]]), ncity)
      plt.plot([point1[0], point2[0]], [point1[1], point2[1]])
```

### Bryan Vela
Topic | Desc
-|-
Autor | Bryan Vela
Algoritmo | Nearest Neighbor
Complejidad Temporal | O(V*E)

El algoritmo de Nearest Neighbor es un algoritmo voraz de cercania, que su filosofia se encuentra en siempre seguir el enlace con el menor costo posible.
#### Codigo Del Algoritmo
```py
def nearest_neighbor(G):
  visited = [False for _ in G]
  path = [-1 for _ in G]
  path[0] = -1
  visited[0] = True
  for node, edge in enumerate(G):
    min = float("Inf")
    minV = None
    for a in edge:
      if min > a[1]:
        if visited[a[0]] == False:
          min = a[1]
          minV = a[0]
    if minV:     
      path[node] = minV
      visited[minV] = True
  return path
```
#### Procesamiento de Grupos con el Algoritmo:
```py
def procesar_grupo_nearest_neighbor(grupo, plt=None, n_city=80):
  nodos = grupo["casas"]
  nodos.append(grupo["almacen"])
  label = list()
  for nodo in nodos:
    label.append(str(get_node(nodo, n_city)))
  grafo = [[] for _ in range(len(nodos))]
  for i, _ in enumerate(nodos):
    for j, _ in enumerate(nodos):
      if i == j: continue
      grafo[i].append((j, manhattan_distance(nodos[i], nodos[j])))
  path = nearest_neighbor(grafo)
  for i in range(len(path)):
      point1 = get_coord(int(label[i]), n_city)
      point2 = get_coord(int(label[path[i]]), n_city)
      plt.plot([point1[0], point2[0]], [point1[1], point2[1]])
```
## Elaboracion del Grafo
### Función para generar grafo por un tamaño dado
``` py
def create_city(size):
  G = [[] for _ in range(size**2)]
  ultima = False
  for i in range(size ** 2):
    if i % size == 0:
      G[i].append(i+1)
    elif (i + 1) % size == 0:
      G[i].append(i-1)
    else:
      G[i].append(i+1)
      G[i].append(i-1)
    if (size - 1)*size == i:
      ultima = True
    if not ultima:
      G[i].append(i+size)
      G[i + size].append(i)
  identificador = ["N" for _ in range(size**2)]
  return G, identificador
```

### Generacion de la Ciudad
``` py
n_city = 2000
G, identificador = create_city(n_city)
generar_puntos(2500, 250, n_city)
almacenes = pd.read_csv("almacenes.csv", header=None).to_numpy()
casas = pd.read_csv("casas.csv", header=None).to_numpy()
casas = casas[1:]
almacenes = almacenes[1:]
plt.subplots(figsize=(20, 20))
plt.ylabel('Eje Y')
plt.xlabel('Eje X')
plt.scatter(almacenes[:, 0], almacenes[:, 1])
plt.scatter(casas[:, 0], casas[:, 1])
```
![enter image description here](https://raw.githubusercontent.com/PietroMinaya/cc41_tf_201910362_201718387_201914478_201912855_20181A046/main/grafo.png)
### Heuristica de Manhattan
Una Heuristica es un metrica que nos va ayudar a hacer medicions para estimar los pesos de nuestros grafos, existen diferentes tipos de Heuristica para dicha tarea como la Euriliana, Euclidiana y la de Manhattan. En este caso elegimos la heuristica de Manhattan ya que esta solo considera movimientos en horizontal y vertical sin considerar movimientos en diagonal, como nuestro grafo solo considera movimientos horizontales y verticales es perfecta para nuestra solución.

```py
def manhattan_distance(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
```

## Solución
```py
plt.subplots(figsize=(20, 20))
plt.ylabel('Eje Y')
plt.xlabel('Eje Y')
for grupo in grupos:
  procesar_grupo_nearest_neighbor(grupo, plt, n_city)
plt.scatter(almacenes[:, 0], almacenes[:, 1])
plt.scatter(casas[:, 0], casas[:, 1])
```
![enter image description here](https://raw.githubusercontent.com/PietroMinaya/cc41_tf_201910362_201718387_201914478_201912855_20181A046/main/solución.png)

## Videos de Exposicion
- Trabajo Parcial: [https://youtu.be/Q-11WAOT0Pg](https://youtu.be/Q-11WAOT0Pg)
