import math


def calcularArea(base,altura):
    return  base*altura

def formulaNormal(x,sigma, u):
    evaluado = (1/(sigma * math.sqrt(2*math.pi))) * math.exp((-0.5*((x-u)/sigma)**2))
    return evaluado

def reinman(comienzo, fin, baseFrag, sigma, u):
    aproximacion = 0
    while comienzo < fin:
        aproximacion += calcularArea(baseFrag,formulaNormal(comienzo + (baseFrag/2), sigma, u))
        comienzo += baseFrag
    return aproximacion
    
print(reinman(-30,0,1,1,0))
