#install.packages("pracma")
options(digits=8)
library(pracma)
exact <- function(x)
{
  return(exp(x)*(((x^2)*exp(-x))+(x*exp(-x))+1))
}
f <- function(x,y) 
{
  return((2*x)-((x^3)/3)+((x^2)/2)+1)
}
pT = taylor(f, 0, n = 2)
print("Valores con aproximacion de Taylor: ")
x <- seq(0, 1, length.out=5)
print(data.frame(X = x, Y = polyval(pT,x)))

x <- seq(-2, 2, length.out=100)
pTa <- polyval(pT, x)
plot(x, pTa, type = "l", col = "gray",main="Comparación",xlab="X",ylab="Y", lwd = 3)
lines(x, exact(x), col = "orange" ,lwd = 3)
legend(-2,6,c('Taylor','Exacta'),lty=c(1,1),lwd=c(2.5,2.5),col=c('gray','orange'))
cat("\n")
print("con h= 0.1:")
cat("valor real       valor con taylor     error\n")
cat(exact(0.1),"      ",polyval(pT,0.1),"             ",(exact(0.1)-polyval(pT,0.1))/exact(0.1))
