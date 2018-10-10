
distanciaeuclediana<-function(x,x1,y,y1)
{
  return (sqrt ( (x1-x)^2 + (y1-y)^2 ))
}
copokoch<-function(iter,s)
{
  matriz<- koch(side = s, niter = iter)
  plot(matriz[, 1], matriz[, 2], type = "l", asp = TRUE, col = "gray")
  segments(matriz[nrow(matriz), 1], matriz[nrow(matriz), 2], matriz[1, 1], matriz[1, 2], col = "gray")
  return (matriz)
}
dis=0
n<- 3 #iteraciones
l0<- 1 #longitud inicial
m=copokoch(n,l0)

dis=0
m=koch(side = 1, n = n)
for(i in 2:nrow(m)){
  x=m[i-1,1]
  y=m[i-1,2]
  x1=m[i,1]
  y1=m[i,2]
  dis=dis+distanciaeuclediana (x, x1, y, y1)
}
x=m[nrow(m),1]
y=m[nrow(m),2]
x1=m[1,1]
y1= m[1,2]
dis=dis+distanciaeuclediana (x, x1, y, y1)
print(dis)
l<- 3*((4/3)^(n-1))*l0 #longitud en la n-esima iteracion 
print(l)
print(dis)
