lagrange = function(x,y,a){
  n = length(x)
  if(a < min(x) || max(x) < a) stop("No está interpolando")
  X = matrix(rep(x, times=n), n, n, byrow=T)
  mN = a - X; diag(mN) = 1
  mD = X - t(X); diag(mD) = 1
  Lnk = apply(mN, 1, prod)/apply(mD, 2, prod)
  sum(y*Lnk)
}
require(PolynomF)
x = c( 35,48,70,40,22) # n+1 = 11
y = c(35,45,55,65,75)
# Polinomio de ajuste (polinomio interpolante en este caso)
datx = x[1:5]; daty = y[1:5]
polyAjuste = poly.calc(datx,daty)
print('Polinomio: ' )
print(polyAjuste)
plot(datx,daty, pch=19, cex=1, col = "gray", asp=1)
curve(polyAjuste,add=T)

print('ajuste polinomico usando 55 ')

print(round(polyAjuste(55),digits = 3))
print('ajuste LAGRANGE usando 55 ')
print(round(lagrange(x[1:5],y[1:5], 55),digits = 3))
