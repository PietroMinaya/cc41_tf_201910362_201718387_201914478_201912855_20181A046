import numpy as np
import numpy.random as npr

def generar_almacenes(cantidad):
  almacenes = npr.randint(0, 2000, (cantidad, 2), dtype=np.int)
  return almacenes