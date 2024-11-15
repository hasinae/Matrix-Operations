import numpy as np
from fractions import Fraction
from fracDisplay import frac

def get(line):
  return np.array([list(map(Fraction,line.split(";")[i].split(","))) for i in range(len(line.split(";")))])

# DESC: displays matrix in latex
def display(A):
  print("\\left[\\begin{array}{@{}", end = "")
  
  for i in range(A.shape[0]):
    print("c", end = "")
    
  print("@{}}")
  
  for i in range(A.shape[0]):
    for j in range(A.shape[1]):
      A[i, j] = Fraction(A[i, j])
  
      print(frac(A[i, j]) + (" & " if j != A.shape[1]-1 else "\\\\"), end = "")
    print("")
    
  print("\\end{}\\right]")