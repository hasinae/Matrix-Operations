import numpy as np
from fractions import Fraction
from fracDisplay import frac
  
# DESC: returns elementary matrix to multiply row r1 by scalar k, add to row r2
def elemMat(size, r1, k, r2):
  I = np.identity(size)  # create identity matrix able to be multiplied
  I[r2-1, :] += I[r1-1, :] * float(k)  # multiply row r1 by scalar k, add to row r2
  return I

# DESC: multiplies r1 by k, adds to r2
def do(A, r1, k, r2):
  E = elemMat(A.shape[0], r1, k, r2)
  return np.matmul(E, A)

# DESC: displays multiply add rows in latex
def display(r1, k, r2):
  print("\\xrightarrow[]{" + frac(k) + "R_{" + str(r1) + "}+R_" + str(r2) + "\\to R_{",r2,"}}")