#ENTRADA
N=[]

def menorArreglo():  
    N1=int(input("Ingrese el numero 1: "))
    N2=int(input("Ingrese el numero 2: "))
    N3=int(input("Ingrese el numero 3: "))
    N4=int(input("Ingrese el numero 4: "))
    N5=int(input("Ingrese el numero 5: "))
    N.append(N1),N.append(N2),N.append(N3),N.append(N4),N.append(N5)
    nummenor=N[0]

    for i in N:
        if nummenor > i:
            nummenor = i       

    print(nummenor)

menorArreglo()
    