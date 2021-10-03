import numpy as np
import numpy.random as npr

def generarCasas(cantidad):
  casas = npr.randint(0, 2000, (cantidad, 2), dtype=np.int)
  return casas