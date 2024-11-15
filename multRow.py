import numpy as np
from fractions import Fraction
from fracDisplay import frac
  
# DESC: returns elementary matrix to multiply row r by scalar k
def elemMat(size, r, k):
  I = np.identity(size)  # create identity matrix able to be multiplied
  I[r-1, :] *= float(k)  # multiply row r by k
  return I

# DESC: mutiplies row r by scalar k
def do(A, r, k):
  E = elemMat(A.shape[0], r, k)
  return np.matmul(E, A)

# DESC: displays row multiply in latex
def display(r, k):
  print("\\xrightarrow[]{" + frac(k) + "R_{" + str(r) + "}\\to R_{" + str(r) + "}}")