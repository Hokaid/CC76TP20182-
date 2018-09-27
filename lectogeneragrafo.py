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
  Y = [0]*2
  for i in range(numero_nodos):
    A = [(0,0)]*2
    for j in range(2):
      u = random.randint(0,numero_nodos-1)
      while Isin(Y,u):
        u = random.randint(0,numero_nodos-1)
      w = math.sqrt(((Posiciones[2*u+1]-Posiciones[2*i+1])**2)+((Posiciones[2*u]-Posiciones[2*i])**2))
      if (u != i):
          Y[j] = u
          A[j] = (w,u)
    T = []
    for e in range(len(A)):
        if (A[e] != (0,0)):
            T.append(A[e])
    G[i] = T
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

def EscribirGrafo(G):
    f = open("GrafoPrueva4.txt", "w")
    for V in G:
        i = 0
        for v,w in V:
            if (i == len(V)-1):
                f.write(str(v) + "," + str(w))
            else:
                f.write(str(v) + "," + str(w) + " ")
            i = i + 1
        f.write("\n")
def str2pair(x):
    """
    Recibe una cadena como '4,5' y retorna una tupla (4, 5)
    """
    nums = x.split(',')
    if (is_float(nums[0])):
        peso = float(nums[0])
        llegada = int(nums[1])
        return peso, llegada

def LeeLAP2LAP(filename):
    """
    Funcion lee un archivo que contiene un grafo en formato de lista de adyacencia
    con pesos y retorna una lista de adyacencia con pesos
    """
    G = []
    file = open(filename)
    for line in file:
        G.append([str2pair(x) for x in line.split(' ')])
        
    return G


