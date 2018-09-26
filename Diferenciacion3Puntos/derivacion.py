import math
from sympy import *
import numpy as np

def fx(x):
  return x*math.exp(x)

def df(x):
  return math.exp(x)+x*math.exp(x)

def formula(x,h):
  return (0.5/h) * (-3*fx(x)+ 4 * fx(x+h) - fx(x+(2*h))) + ((h**2)/3)

print("derivda en 2: ",df(2),"\n")
for x in range(1,5):
  print("x= ",2+0.1**x,"valor: ",formula(2,0.1**x), "Error= ",abs(formula(2,0.1**x)-df(2)))
