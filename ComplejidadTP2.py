import random
import math

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

def LeerPosiciones(filename, numero_nodos):
    Posiciones = [0]*2*numero_nodos
    pr = 0
    file = open(filename)
    i = 0
    for line in file:
        for j in line.split('-'):
            if (is_float(j)):
                pr = float(j)
                Posiciones[i] = pr
                i = i + 1
        print(i)
    return Posiciones

def Isin(Arr, k):
  for x in Arr:
    if(k==x):
      return True
  return False

def CrearGrafo(Posiciones, numero_nodos):
  G = [[]]*numero_nodos
  Y = [0]*6
  for i in range(numero_nodos):
    A = [(0,0)]*6
    for j in range(6):
      u = random.randint(0,numero_nodos)
      while Isin(Y,u):
        u = random.randint(0,numero_nodos)
      w = math.sqrt(((Posiciones[2*u+1]-Posiciones[2*i+1])**2)+((Posiciones[2*u]-Posiciones[2*i])**2))
      if (u != i):
          Y[j] = u
          A[j] = (w,u)
    G[i] = A
    print(i)
  return G

def ISin(Arr, b):
    (w,u) = b
    for k in range(len(Arr)):
        (x,y) = Arr[k]
        if(w==x)and(u==y):
            return False
        elif(u==y)and(x!=0):
            Arr.pop(k)
    return True

def Convertir_A_Grafo_No_Dirigido(G):
  u = 0
  for V in G:
    for w, v in V:
        if ((w,v) != (0,0)) and ISin(G[v],(w,u)):
            G[v].append((w,u))
    u += 1
    print(u)
  return G

numero_nodos = 145225
T = Convertir_A_Grafo_No_Dirigido(CrearGrafo(LeerPosiciones("Datos_TSP.txt", numero_nodos), numero_nodos))


