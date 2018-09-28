# coding: utf-8
# Your code here!
import math
from decimal import Decimal

def calcularArea(base,h):
    return  base*h

def formulaNormal(x,sigma, u):
    evaluado = (1/(sigma * math.sqrt(2*math.pi))) * math.exp((-0.5*((x-u)/sigma)**2))
    return evaluado

def reinman(comienzo, fin, baseFrag, sigma, u):
    aproximacion = 0
    while comienzo < fin:
        aproximacion += calcularArea(baseFrag,formulaNormal(comienzo +(baseFrag/2), sigma, u))
        #print(calcularArea(baseFrag,formulaNormal(comienzo +baseFrag, sigma, u),formulaNormal(comienzo +(2*baseFrag), sigma, u)))
        comienzo += baseFrag
def rieman2(comienzo,fin, baseFrag):
    evaluado=0
    while comienzo < fin:
        evaluado += calcularArea(baseFrag,form(comienzo +(baseFrag/2)))
        #print(calcularArea(baseFrag,formulaNormal(comienzo +baseFrag, sigma, u),formulaNormal(comienzo +(2*baseFrag), sigma, u)))
        comienzo += baseFrag
        return evaluado
def form(x):
    return (1/math.sqrt(2*math.pi)) * math.e **(-0.5*((x)**2))
    
print("\n decimales ")
print("0.0000 || ", end="")
for i in range(0,10):
  print("0.00" + str(i) + "0",end = " | ")

print("\n")
x = 0
cont = 0
print("0.0000 || ", end="")
while x < 1:
    y = Decimal(rieman2(-10,x,0.001))
   
    print(round(y,4),end=" | ")
    cont += 1
    if(cont== 10):
        max = Decimal(x+0.001)
        print()
        print(str(round(max,4))+" || ", end="")
        cont = 0
    x += 0.001
    
#print(reinman(-1,0,0.1,1,0))
