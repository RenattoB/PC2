#Entrada
N=[[8,2,4],[8,9,5],[6,9,2]]

#Creamos
x=0
suma=0
for i in range(len(N)):
    suma=suma+N[x][x]
    x=x+1


print ("La suma de los elemntos de la diagonal principal es ",suma)