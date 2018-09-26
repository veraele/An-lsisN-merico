calcularArea = function(base,altura){
    return  (base*altura)}

formulaNormal = function(x,sigma, u){
    evaluado <- (1/(sigma * sqrt(2*pi))) * exp((-0.5*((x-u)/sigma)**2))
    return (evaluado)}

reinman = function(comienzo, fin, baseFrag, sigma, u){
    aproximacion <- 0
    while (comienzo < fin){
        aproximacion <- aproximacion + calcularArea(baseFrag,formulaNormal(comienzo + (baseFrag/2), sigma, u))
        comienzo <- comienzo + baseFrag}
    return (aproximacion)}
    
print(reinman(-30,0,1,1,0))
