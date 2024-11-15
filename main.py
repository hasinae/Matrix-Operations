import numpy as np
from fractions import Fraction
import matrix as m
import matDict as d

# COPY PASTE LATEX CODE INTO https://latex.codecogs.com/eqneditor/editor.php

while True:
  line = input("> ")
  
  # mat:    A = 1,2;3,4
  # swap:   A = row1,row2
  # multr:  A = row,scalar
  # maddr:  A = row1,scalar,row2
  # show:   A
  # mmult:  C = A,B
  # madd:   C = A,B
  # det:    A
  # ident:  A = size
  # zero:   A = size
  
  if line == "mat":
    d.getMatrix()

  elif line == "augm":
    d.getMatrix(True)
    
  elif line == "swap":
    d.swapRows()
    
  elif line == "multr":
    d.multRow()
    
  elif line == "maddr":
    d.multAddRows()
    
  elif line == "show":
    name = input("  > ")
    print("")
    m.display(d.mats[name])
    print("")
    
  elif line == "mmult":
    line2 = input("  > ").replace(" ", "").split("=")
    print("")
    names = line2[1].split(",")
    d.mats[line2[0]] = np.matmul(d.mats[names[0]],d.mats[names[1]])
    m.display(d.mats[line2[0]])
    print("")    

  elif line == "madd":
    line2 = input("  > ").replace(" ", "").split("=")
    print("")
    names = line2[1].split(",")
    d.mats[line2[0]] = np.add(d.mats[names[0]],d.mats[names[1]])
    m.display(d.mats[line2[0]])
    print("")        
    
  elif line == "det":
    name = input("  > ")
    print("")
    print(int(np.linalg.det(d.mats[name])))
    print("")
  
  elif line == "exit":
    break
    
  else:
    print("\nInvalid command\n")