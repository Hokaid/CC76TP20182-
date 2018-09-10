import random
import math

def is_float(value):
  try:
    float(value)
    return True
  except:
    return False

def LeerPosiciones(filename):
    Posiciones = [0]*32
    pr = 0
    file = open(filename)
    i = 0
    for line in file:
        for j in line.split('-'):
            if (is_float(j)):
                pr = float(j)
                Posiciones[i] = pr
                i = i + 1
    return Posiciones
        
def EscribirGrafo(Posiciones):
  archivo = open("grafo.txt","a")
  for i in range(16):
    for j in range(3):
      u = random.randint(0,15)
      w = math.sqrt(((Posiciones[2*u+1]-Posiciones[2*i+1])**2)+((Posiciones[2*u]-Posiciones[2*i])**2))
      if (j == 2):
        if (u != i):
          archivo.write('%f-%d\n'%(w, u))
        else:
          archivo.write('\n')
      else:
        if (u != i):
          archivo.write('%f-%d-'%(w, u))
  archivo.close()

def str2pair(x):
    nums = x.split(',')
    return float(nums[0]), int(nums[1])     

#G.append([str2pair(x) for x in line.split(' ')])
def LeerGrafo(filename):
    G = [[]]*16
    file = open(filename)
    i = 0
    for line in file:
      datos = line.split('-')
      for x in range(len(datos)):
        G[i].append((float(datos[2*x]), int(datos[2*x+1])))
      i = i + 1
    return G
def Convertir_A_Grafo_No_Dirigido(G):
  u = 0
  for V in G:
    for w, v in V:
        G[v].append((w,u))
    u += 1
  return G

EscribirGrafo(LeerPosiciones("Prueva.txt"))
print(LeerGrafo("grafo.txt"))


