import math
import copy
from tkinter import *
from tkinter import messagebox
from lectorgrafo import *

def DeterminarCamino(ArrVisitados, Resto):

    Contador = 0
    
    for K in range(len(ArrVisitados)):
        if ArrVisitados[K]:
            Contador += 1

    if Contador == len(ArrVisitados) - Resto:
        return True
    else:
        return False
        

def TSP_BackTraking(Grafo, PN, contador, salir):

    NroNodos = len(Grafo)
    NodosVisitados = [False]*NroNodos

    # Crear Arreglo de pesos de los grafos
    Pesos = [math.inf]*NroNodos

    # Crear Arreglo de Caminos posibles
    Caminos = []
    Camino = []
    Pesos = []
    Peso = []
    
    def BackTraking(Grafo, PE, NI, NodosVisitados, Camino, Peso, contador, salir):
        
        NodosVisitados = copy.copy(NodosVisitados)
        Camino = copy.copy(Camino)
        Peso = copy.copy(Peso)
        
        if not NodosVisitados[NI]:
            
            NodosVisitados[NI] = True
            Camino.append(NI)
            Peso.append(PE)

            if DeterminarCamino(NodosVisitados, 0):
                Caminos.append(Camino)
                Pesos.append(Peso)
                
            elif DeterminarCamino(NodosVisitados, 2):
                NodosVisitados[PN] = False
            
            for P, N in Grafo[NI]:
                print(contador)
                if contador >= 900:
                    salir[0] = True
                    Pesos.append(Peso)
                    Caminos.append(Camino)
                    break
                if (salir[0] == False):
                    BackTraking(Grafo, P, N, NodosVisitados, Camino, Peso, contador+1, salir)
                
                   
    BackTraking(Grafo, 0, PN, NodosVisitados, Camino, Peso,contador, salir)  
    
    return Caminos, Pesos


def SeleccionarCamino(Grafo, NodoInicio, contador, salir, camino, distamin, solup, ciudad, peso, solucionado):

    ArrCaminos, ArrPesos = TSP_BackTraking(Grafo, NodoInicio, contador, salir)
    if salir[0] == False:
        solucionado[0] = True
        solup.set("100%")
        Nro = len(ArrPesos)
        Cam = len(ArrCaminos)
        camino.set(Cam)
        AP = [0]*Nro
        for K in range(Nro):
            for C in ArrPesos[K]:
                AP[K] += C
        Aux = AP[0]
        M = 0
        for I in range(Cam):
            if Aux > AP[I]:
                Aux = AP[I]
                M = I
        DistanciaMin = 0
        for o in ArrPesos[M]:
            DistanciaMin = DistanciaMin + o
        print("La distancia recorrida en el mejor camino es: " + str(DistanciaMin) + " Km")
        distamin.set(DistanciaMin)
        ciudad.set(len(ArrCaminos[M]) - 1)
        peso.set(DistanciaMin)
        print("El camino más corto encontrado posee la siguiente estructura: ")
        i = 0
        PesoAcumulado = 0
        for o in ArrCaminos[M]:
            PesoAcumulado = ArrPesos[M][i] + PesoAcumulado
            print(str(o) + "(" + str(PesoAcumulado) + ")", end=" ")
            i = i + 1
    else:
        DistanciaMin = 0
        for o in ArrPesos[0]:
            DistanciaMin = DistanciaMin + o
        camino.set(0)
        peso.set(float(DistanciaMin))
        n = len(Grafo)
        nodosVisit = len(ArrPesos[0])
        ciudad.set(nodosVisit)
        distamin.set("Error de Recursión")
        solup.set(str(float((100/n)*nodosVisit))+"%")
        

"""        

#G = [[(2,1),(1,2)],[(2,0),(3,2)],[(1,0),(3,1)]]
#G = [[1,2,3,4],[0,3],[0,3,4],[0,1,2],[0,2]]
#G = [[(3,1), (4,2), (8,5)],[(3,0), (6,2), (4,3)],[(4,0) ,(6,1), (5,3), (7,4), (4,5)],[(3,1) ,(5,2), (3,4)],[(7,2), (3,3), (4,5)],[(8,0), (4,2), (2,4)]]
solucionado = [False]*1
G = LeeLAP2LAP("GrafoCompleto.txt")
ventanap = Tk()
salir = [False]*1
ciudad = StringVar()
peso = StringVar()
camino = StringVar()
distamin = StringVar()
solup = StringVar()

ventanap.mainloop()
"""
