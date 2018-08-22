from sympy import *
from math import *
from numpy import*

def funcion(x):
    return float(ln(x+2)-sin(x))

xu=-1
x=-1.1
e=0.00000001

l=funcion(x)
xaux=x
fx=funcion(x)
fu=funcion(xu)

print(funcion(xu))
while abs(0-l)>e:
    xaux=x
    u=(x-xu)
    t=(fx-fu)
    fx=funcion(x)
    fu=funcion(xu)
    if(fx-fu!=0):
        x=x-fx*(u/t)
    xu=xaux
    l=funcion(x)

print(str(x))
