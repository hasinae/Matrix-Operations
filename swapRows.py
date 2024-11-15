import numpy as np
from fractions import Fraction

# DESC: returns elementary matrix to swap rows r1 & r2
def elemMat(size, r1, r2):
  I = np.identity(size)  # create identity matrix able to be multiplied
  I[[r1-1, r2-1]] = I[[r2-1, r1-1]]  # swap rows r1 & r2
  return I

# DESC: swaps rows r1 & r2
def do(A, r1, r2):
  E = elemMat(A.shape[1], r1, r2)
  return np.matmul(E, A)

# DESC: displays row swap in latex
def display(r1, r2):
  print("\\xrightarrow[]{R_{",r1,"}\\leftrightarrow R_{",r2,"}}")