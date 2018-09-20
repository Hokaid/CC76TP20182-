import math
import copy
import heapq as hq



def ucs(G, s, t, pesos, padres):
    n = len(G)
    visited = [False]*n
    weights = [math.inf]*n
    path = [-1]*n
    queue = []
    weights[s] = 0
    hq.heappush(queue, (0, s))
    while len(queue) > 0:
        g, u = hq.heappop(queue)
        if visited[u]: continue
        visited[u] = True
        if (u == t): break
        for h, v in G[u]:
            f = g + h
            if f < weights[v]:
                weights[v] = f
                path[v] = u
                hq.heappush(queue, (f, v))
                
    return pesos, padres, path, weights

def TSP_FuerzaBruta(G, ciudad, peso, camino, distamin, solup, solucionado, cityorigin):
   
    def _TSP_FuerzaBruta(G, s, path,pesos,distancia, padre, visitados, contador, origen, MatriPesos, MatriPaths, ArrDistan, MatPer, MatPar, salir):
        if (contador == 970):
            conti = 0
            for y in visitados:
                if y == True:
                    conti = conti + 1
            ArrDistan.append(distancia)
            ArrDistan.append(conti)
            salir[0] = True
        if (contador == len(G)-1):
            encontrado = False
            for w,v in G[s]:
                if (origen == v):
                    path[s] = padre
                    visitados[s] = True
                    pesos[s] = distancia
                    path[origen] = s
                    distancia = distancia + w
                    pesos[origen] = distancia
                    ArrDistan.append(distancia)
                    MatriPesos.append(pesos)
                    MatriPaths.append(path)
                    MatPar.append(0)
                    MatPer.append(0)
                    solucionado[0] = 1
                    encontrado = True
            if(encontrado == False):
                path[s] = padre
                visitados[s] = True
                pesos[s] = distancia
                pesos, padres, path, weights = ucs(G,s,origen,pesos,path)
                ArrDistan.append(distancia + weights[cityorigin])
                MatriPesos.append(pesos)
                MatriPaths.append(padres)
                MatPar.append(path)
                MatPer.append(weights)
                solucionado[0] = 1
        else:
            visitados[s] = True
            path[s] = padre
            pesos[s] = distancia
            menor1_w = math.inf
            menor1_v = -1
            menor2_v = -1
            menor2_w = math.inf
            i = 0
            for w,v in G[s]:
                if not visitados[v]:
                    if i == 0:
                        if w < menor1_w:
                            menor1_w = w
                            menor1_v = v
                    elif i >= 1:
                        if w < menor1_w:
                            menor2_w = menor1_w
                            menor2_v = menor1_v
                            menor1_v = v
                            menor1_w = w
                        elif w < menor2_w:
                            menor2_w = w
                            menor2_v = v
                i = i + 1
            print(str(contador))
            if (menor1_v != -1):
                path1 = copy.copy(path)
                pesos1 = copy.copy(pesos)
                visitados1 = copy.copy(visitados)
                if (salir[0] == False):
                    _TSP_FuerzaBruta(G,menor1_v,path,pesos,distancia + menor1_w,s,visitados,contador+1, origen, MatriPesos, MatriPaths, ArrDistan, MatPer, MatPar, salir)
                    if (menor2_w != math.inf)and(salir[0] == False):
                        _TSP_FuerzaBruta(G,menor2_v,path1,pesos1,distancia + menor2_w,s,visitados1,contador+1, origen, MatriPesos, MatriPaths, ArrDistan, MatPer,MatPar,salir)

    n = len(G)
    path = [-1]*n
    pesos = [math.inf]*n
    visitados = [False]*n
    waycounter = []
    ArrDistan = []
    MatriPaths = []
    MatriPesos = []
    MatPer = []
    MatPar = []
    salir = [False]*1
    _TSP_FuerzaBruta(G, cityorigin, path, pesos, 0, -1, visitados, 0, cityorigin, MatriPesos, MatriPaths, ArrDistan, MatPer, MatPar, salir)

    
    cant_caminos = 0
    es_camino = True
    for k in range(len(MatriPaths)):
        for b in MatriPaths[k]:
            if b == -1:
                es_camino = False
        if (es_camino == True) or (MatPar[k] != 0):
            cant_caminos = cant_caminos + 1
        es_camino = True
    def Way(path,pesos,k,cont):
        if (k != cityorigin or cont==0) and (k != -1):
            Way(path,pesos,path[k],cont+1)
            print(k, end = "")
            print("("+ str(pesos[k])+")", end = " ")
    def Way2(path,pesos,k,cont,cruz):
        if (k != -1):
            Way2(path,pesos,path[k],cont+1,cruz)
            if (path[k] != -1):
                print(k, end = "")
                print("("+ str(pesos[k]+cruz)+")", end = " ")
    if (solucionado[0] == 1):
        mini = math.inf
        i = 0
        minid = -1
        for v in ArrDistan:
            if v < mini:
                mini = v
                minid = i
            i = i + 1
        if (MatPar[minid] == 0 and MatPer[minid] == 0):
            print("La distancia recorrida en el mejor camino encontrado es (Km): " + str(ArrDistan[minid]))
            print("El mejor camino encontrado sigue la siguiente estructura: ")
            Way(MatriPaths[minid],MatriPesos[minid], cityorigin, 0)
            print("")
            distamin.set(str(ArrDistan[minid]))
            peso.set(str(ArrDistan[minid]))
            ciudad.set(str(len(MatriPaths[minid])))
            camino.set(str(cant_caminos))
            solup.set(str("100%"))
        else:
            print("La distancia recorrida en el mejor camino encontrado es (Km): " + str(ArrDistan[minid]))
            print("El mejor camino encontrado sigue la siguiente estructura: ")
            contador2 = 0
            for x1 in MatriPaths[minid]:
                if x1 != -1:
                    contador2 = contador2+ 1
            ini = MatPar[minid][cityorigin]
            def Findsin_hijo(p, i, rpt):
                posi = 0
                for o in p:
                    if (i==o):
                        break
                    posi = posi + 1
                if (posi == len(p)):
                    rpt.append(i)
                else:
                    Findsin_hijo(p, posi,rpt)
            rpta = []
            Findsin_hijo(MatriPaths[minid], cityorigin, rpta)
            j1 = rpta[0]
            if ini != -1:
                contador2 = contador2+ 1
            def camicont(p, inil, f, contador, c):
                if (inil == f):
                    c.append(contador)
                else:
                    camicont(p, p[inil],f,contador + 1, c)
            c = []
            camicont(MatPar[minid], ini, j1, contador2, c)
            cruz = MatriPesos[minid][j1]
            Way(MatriPaths[minid],MatriPesos[minid], j1, 0)
            Way2(MatPar[minid],MatPer[minid],cityorigin,0,cruz)
            print("")
            distamin.set(str(ArrDistan[minid]))
            peso.set(str(ArrDistan[minid]))
            ciudad.set(str(c[0]))
            camino.set(str(cant_caminos))
            solup.set(str("100%"))
    else:
        distamin.set(str("Error de Recursión"))
        if (ArrDistan[0] != None)and(ArrDistan[1] != None):
            peso.set(str(ArrDistan[0]))
            ciudad.set(str(ArrDistan[1]))
        camino.set(str(cant_caminos))
        solup.set(str(float((100/n)*ArrDistan[1]))+"%")






        
