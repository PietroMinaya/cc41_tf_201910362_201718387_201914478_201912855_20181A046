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