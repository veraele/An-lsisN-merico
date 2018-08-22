def sumarSubMatriz(A):
    M = list(list(A))
    lenV = len(M)
    h=0
    for i in range(0,lenV):
        for j in range(i,lenV):
            h+=M[i][j]
    
    print(h)
    
a=[[1,2,3,5],[2,1,8,7],[4,6,8,9],[4,7,4,2]]
sumarSubMatriz(a)
