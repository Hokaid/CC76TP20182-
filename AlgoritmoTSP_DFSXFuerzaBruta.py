import math
import copy
        

def DFS(Grafo, NroNodos, NodoInicial, Nodo, NodosVisitados, Profundidad, ConCaminos, ConNodosRecorridos, ConDistanciaRecorrida, salir):
    # Crear copia de nodos visitidos
    NodosVisitadosAux = copy.copy(NodosVisitados)

    # Marcar Nodo de proceso como visitado
    NodosVisitadosAux[Nodo] = True

    # Iniciar proceso de recorrido de nodos
    Nodos = Grafo[Nodo]    
    # Crear un diccionario para llevar el control de nodos recorridos    
    MenorPeso = math.inf
    MenorCamino = []
    MenorPesos = []
    MenorNodo = []
    
    for u, v in Nodos:
        # Verificar si ya se alcanzó el nodo inicial (Posible solucion)
        if (NodoInicial == v):
            if (Profundidad == NroNodos-1):
                ConCaminos[0] = ConCaminos[0] + 1
                return u, [v], [u]
            
        else: # si no se alcanzó una solución, procesar Nodo        
            if not NodosVisitadosAux[v]:
                if (salir[0] == False):
                    if (Profundidad >= 900):
                        salir[0] = True
                    print(Profundidad)
                    Peso, NodosCamino, Pesos = DFS(Grafo, NroNodos, NodoInicial, v, NodosVisitadosAux, Profundidad + 1, ConCaminos, ConNodosRecorridos, ConDistanciaRecorrida, salir)
                    if (Peso >= 0) and (Peso + u < MenorPeso):
                        MenorCamino = [v] + NodosCamino;
                        MenorPesos = [u] + Pesos;
                        MenorPeso = u + Peso
                        MenorNodo = [u, v]
                    elif (NroNodos >= 900):
                        ConNodosRecorridos[0] = ConNodosRecorridos[0] + 1
                        ConDistanciaRecorrida[0] = ConDistanciaRecorrida[0] + u
            
        

    # Si encontró un menor camino, agregar a NodosCamino el menor camino
    if len(MenorCamino) > 0:
        return MenorPeso , MenorCamino, MenorPesos
    else:
        return -1, [], []


def TSP_DFS(Grafo, NodoInicial, salir, ciudad, peso, distamin, solup, camino, solucionado):

    # Iniciar Contador para numero de Caminos Posibles (simular memoria dinamica - Punteros)
    ConCaminos = [0]*1

    ConNodosRecorridos = [0]*1

    ConDistanciaRecorrida = [0]*1
    
    NroNodos = len(Grafo)
    # Generar lista para llevar el control de nodos visitados
    NodosVisitados = [False]*NroNodos   

    # Efectuar proceso de busqueda     
    Peso, NodosCamino, Pesos = DFS(Grafo, NroNodos, NodoInicial, NodoInicial, NodosVisitados, 0, ConCaminos, ConNodosRecorridos, ConDistanciaRecorrida, salir)
    if Peso != -1:
        solucionado[0] = 1
        print("La distancia recorrida en el mejor camino es: " + str(Peso) + " Km")
        print("El camino más corto encontrado posee la siguiente estructura: ")
        i = 0
        PesoAcumulado = 0
        for o in NodosCamino:
            PesoAcumulado = Pesos[i] + PesoAcumulado
            print(str(o)+ "(" + str(PesoAcumulado) + ")", end=" ")
            i = i + 1
        print("")
        ciudad.set(len(NodosCamino))
        peso.set(Peso)
        distamin.set(Peso)
        solup.set("100%")
        camino.set(ConCaminos[0])
    else:
        ciudad.set(ConNodosRecorridos[0])
        peso.set(ConDistanciaRecorrida[0])
        distamin.set("Error de Recursión")
        n = len(Grafo)
        solup.set(str(float((100/n)*ConNodosRecorridos[0]))+"%")
        camino.set(0)
