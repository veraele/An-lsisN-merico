def f1(x):
    return x

def f2(x):
    return -x

def areaTrapecio(b1,b2,h):
    return ((b1+b2)/2)*h

def areaEntreCurvas(limInf, limSup, particion):
    acum = 0
    while limInf < limSup :
        arTrA=areaTrapecio(abs(f1(limInf)),abs(f1(limInf+ particion)), particion)
        arTrB=areaTrapecio(abs(f2(limInf)),abs(f2(limInf+ particion)), particion)

        if(f1(limInf)<0):
          if(f2(limInf)<0):
            if(f1(limInf)<f2(limInf)):
              acum += arTrA - arTrB
            else:
              acum +=  arTrB - arTrA
          else:
            acum +=  arTrB + arTrA
        elif (f2(limInf)<0):
          if(f1(limInf)<0):
            if(f1(limInf)<f2(limInf)):
              acum += arTrA - arTrB
            else:
              acum +=  arTrB - arTrA
          else:
            acum +=  arTrB + arTrA
        print(limInf, " area acum: ", acum)
        limInf += particion
    
    return acum
    

print('area= '+str(areaEntreCurvas(0,1,0.01)))
