from fractions import Fraction

def frac(f):
  if f.denominator == 1:
    return(str(f))
  else:
    return(("-" if f.numerator < 0 else "") + "\\frac{" + str(abs(f.numerator)) + "}{" + str(f.denominator) + "}")