import math

#Entrada
x=int(input("Ingrese la coordenada x: "))
y=int(input("Ingrese la coordenada y: "))

#Proceso
distancia=math.sqrt(math.pow((0-x),2)+math.pow((0-y),2))

print ("La distancia entre el punto ( ",x,"; ",y," ) es de ",distancia)