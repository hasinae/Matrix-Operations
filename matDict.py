import matrix as m
import swapRows as sr
import multRow as mr
import multAddRows as mar
from fractions import Fraction

# matrix registry
mats = {}

# augments registry
augs = {}

def getMatrix(aug = False):
  global mats
  global augs

  line = input("  > ").replace(" ", "").split("=")
  print("")

  mats[line[0]] = m.get(line[1])
  if aug:
    augs[line[0]] = m.get(input("  > ").replace(" ", ""))
  
  m.display(mats[line[0]])
  print("")


def swapRows(aug = False):
  global mats
  global augs
  
  line = input("  > ").replace(" ", "").split("=")
  print("")
  data = list(map(int, line[1].split(",")))
  
  m.display(mats[line[0]])
  mats[line[0]] = sr.do(mats[line[0]], data[0], data[1])
  sr.display(data[0], data[1])
  m.display(mats[line[0]])
  print("")


def multRow(aug = False):
  global mats
  global augs
  
  line = input("  > ").replace(" ", "").split("=")
  print("")
  data = list(map(Fraction, line[1].split(",")))
  
  m.display(mats[line[0]])
  mats[line[0]] = mr.do(mats[line[0]], data[0].numerator, data[1])
  mr.display(data[0].numerator, data[1])
  m.display(mats[line[0]])
  print("")


def multAddRows(aug = False):
  global mats
  global augs
  
  line = input("  > ").replace(" ", "").split("=")
  print("")
  data = list(map(Fraction, line[1].split(",")))
  
  m.display(mats[line[0]])
  mats[line[0]] = mar.do(mats[line[0]], data[0].numerator, data[1], data[2].numerator)
  mar.display(data[0].numerator, data[1], data[2].numerator)
  m.display(mats[line[0]])
  print("")

