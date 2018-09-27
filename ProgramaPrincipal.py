from lectogeneragrafo import *
from tkinter import *
from tkinter import messagebox
from AlgoritmoTSP_BackTrackingXUCS import *
from AlgoritmoTSP_DFSXFuerzaBruta import *

def is_file(value):
  try:
    file = open(value)
    return True
  except:
    return False



def abrir_ventana2():
    ventanap.withdraw()
    ventana = Toplevel()
    ventana.geometry("600x600")
    imagen = PhotoImage(file="fondo1.png")
    ventana.title("TSP_Algorithms")
    fondo = Label(ventana, image=imagen).place(x=0,y=0)
    boton = Button(ventana,text="Iniciar ejecución",command=Ir_A_Algoritmo).place(x=450,y=270)
    etiquetaTitulo = Label(ventana, text="Travel Salesman Problem (Algoritmos de solución)",bg="#FF4500",fg="#FFF").place(x=150, y= 30)
    etiCamino = Label(ventana, text="Numero de caminos encontrados :",bg="black",fg="#FFF").place(x=50,y=385)
    cCamino =Entry(ventana,textvariable=camino).place(x=250,y=385)
    etiCiudad = Label(ventana, text="Cantidad de ciudades visistadas :",bg="#FFFF00",fg="#000000").place(x=50,y=550)
    cCiudad=Entry(ventana,textvariable=ciudad).place(x=240,y=550)
    etiPeso = Label(ventana, text="Distancia recorrida en el mejor camino (Km):",bg="green",fg="#FFF").place(x=50,y=420)
    cPeso=Entry(ventana,textvariable=peso).place(x=295,y=420)
    MejorWay = Label(ventana, text="Para el mejor camino :",bg="blue",fg="#FFF").place(x=50,y=470)
    etiDistaMin = Label(ventana, text="Distancia del camino más corto encontrado hasta el momento (Km):",bg="#7FFF00",fg="#000000").place(x=50,y=510)
    cDistaMin=Entry(ventana,textvariable=distamin).place(x=420,y=510)
    etiSoluP = Label(ventana, text="Porcentaje de la solución :",bg="purple",fg="#FFF").place(x=50,y=350)
    cSoluP = Entry(ventana,textvariable=solup).place(x=210,y=350)
    ArchivoT = Label(ventana, text="Por favor Indique el nombre del archivo con los datos correspondientes: ",bg="#00FFFF",fg="#000").place(x=50,y=110)
    ArchivoT = Entry(ventana,textvariable=archivot).place(x=50,y=140)
    origenes = Label(ventana, text="Por favor ingrese el codigo del centro poblado en el que desee iniciar el viaje: ",bg="#DC143C",fg="#FFF").place(x=50,y=170)
    origenes =Spinbox(ventana, from_=0,to=145225,textvariable=originNode).place(x=50,y=200)
    cMetodo = Label(ventana, text="Por favor seleccióne el algoritmo con las estrategias correspondientes a utilizar:  ",bg="#4169E1",fg="#FFF").place(x=50,y=230)
    metodo = Spinbox(ventana, values=("Backtracking y UCS","DFS y FuerzaBruta"), textvariable = estrategia).place(x=50,y=260)
    EtiInput = Label(ventana, text="INGRESO DE DATOS",bg="#8B4513",fg="#FFF").place(x=230,y=70)
    EtiOutput = Label(ventana, text="VISUALIZACIÓN DE RESULTADOS",bg="#FFA500",fg="#000").place(x=200,y=300)
    ventana.mainloop()

def Ir_A_Algoritmo():
    if (is_file(archivot.get())):
        messagebox.showwarning
        T = LeeLAP2LAP(archivot.get())
        solucionado = [0]*1
        if (originNode.get() < len(T)):
            if (estrategia.get() == "Backtracking y UCS"):
              TSP_FuerzaBruta(T, ciudad, peso, camino, distamin, solup, solucionado, originNode.get())
            elif (estrategia.get() == "DFS y FuerzaBruta"):
              salir = [False]*1
              TSP_DFS(T, originNode.get(), salir, ciudad, peso, distamin, solup, camino, solucionado)
            else:
              messagebox.showwarning("Algoritmo Inadecuada","Por favor indique un algoritmo a ejecutar valido")
            if (solucionado[0] != 1):                                                                                                                                                                                                                                                                                                                                                                                                   
                messagebox.showwarning("No se pudo encontrar solución", "No se ha podido encontrar un camino, debido a la falta de capacidad computacional con la que se cuenta. Esto sucede, porque la maxima profundidad de recursión que alcanza este algoritmo coincide con el numero de lugares por visitar. Para este caso, la cantidad de centros poblados supera la maxima profundidad de recursion permitida (960-980)")
        else:
            messagebox.showwarning("Codigo Incorrecto","Por favor indique un codigo de centro poblado valido")
    else:
        messagebox.showwarning("Archivo Incorrecto","Por favor ingrese el nombre de un archivo valido")

ventanap = Tk()
ciudad = StringVar()
peso = StringVar()
camino = StringVar()
distamin = StringVar()
solup = StringVar()
archivot = StringVar()
estrategia = StringVar()
originNode = IntVar()
archivot.set("archivo.txt")
ventanap.geometry("400x400")
ventanap.title("TSP_Program")
imagen1 = PhotoImage(file="mapita.png")
fondo1 = Label(ventanap, image=imagen1).place(x=0,y=0)
Titulo = Label(ventanap, text="TRAVEL SALESMAN PROBLEM (Posibles soluciones)",
                 bg="#FFFF00",fg="#000").place(x=60,y=110)
Option = Label(ventanap, text="Seleccione el siguiente botón para comenzar :",
                 bg="#7FFF00",fg="#000").place(x=90,y=150)
botonA1 = Button(ventanap,text="Iniciar Prueva de los algoritmos",command=abrir_ventana2).place(x=107,y=217)
ventanap.mainloop()
