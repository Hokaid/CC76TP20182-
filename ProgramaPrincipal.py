from lectorgrafo import *
from tkinter import *
from tkinter import messagebox
from AlgoritmoTSP_FuerzaBruta import *

def is_file(value):
  try:
    file = open(value)
    return True
  except:
    return False



def abrir_ventana2():
    ventanap.withdraw()
    ventana = Toplevel()
    ventana.geometry("600x550")
    imagen = PhotoImage(file="fondo1.png")
    ventana.title("TSP_FuerzaBruta_Algorithm")
    fondo = Label(ventana, image=imagen).place(x=0,y=0)
    boton = Button(ventana,text="Iniciar ejecución",command=Ir_A_Algoritmo).place(x=450,y=210)
    etiquetaTitulo = Label(ventana, text="Travel Salesman Problem (Algoritmo de Fuerza Bruta)",bg="#FF4500",fg="#FFF").place(x=150, y= 30)
    etiCamino = Label(ventana, text="Numero de caminos encontrados :",bg="black",fg="#FFF").place(x=50,y=335)
    cCamino =Entry(ventana,textvariable=camino).place(x=250,y=335)
    etiCiudad = Label(ventana, text="Cantidad de ciudades visistadas :",bg="#FFFF00",fg="#000000").place(x=50,y=500)
    cCiudad=Entry(ventana,textvariable=ciudad).place(x=240,y=500)
    etiPeso = Label(ventana, text="Distancia recorrida en el mejor camino (Km):",bg="green",fg="#FFF").place(x=50,y=370)
    cPeso=Entry(ventana,textvariable=peso).place(x=295,y=370)
    MejorWay = Label(ventana, text="Para el mejor camino :",bg="blue",fg="#FFF").place(x=50,y=420)
    etiDistaMin = Label(ventana, text="Distancia del camino mas corto encontrado hasta el momento (Km):",bg="#7FFF00",fg="#000000").place(x=50,y=460)
    cDistaMin=Entry(ventana,textvariable=distamin).place(x=420,y=460)
    etiSoluP = Label(ventana, text="Porcentaje de la solución :",bg="purple",fg="#FFF").place(x=50,y=300)
    cSoluP = Entry(ventana,textvariable=solup).place(x=210,y=300)
    ArchivoT = Label(ventana, text="Por favor Indique el nombre del archivo con los datos correspondientes: ",bg="#00FFFF",fg="#000").place(x=50,y=110)
    ArchivoT = Entry(ventana,textvariable=archivot).place(x=50,y=140)
    origenes = Label(ventana, text="Por favor ingrese el codigo del centro poblado en el que desee iniciar el viaje: ",bg="#DC143C",fg="#FFF").place(x=50,y=170)
    origenes =Spinbox(ventana, from_=0,to=145225,textvariable=originNode).place(x=50,y=200)
    EtiInput = Label(ventana, text="INGRESO DE DATOS",bg="#8B4513",fg="#FFF").place(x=230,y=70)
    EtiOutput = Label(ventana, text="VISUALIZACIÓN DE DATOS",bg="#FFA500",fg="#000").place(x=215,y=260)
    ventana.mainloop()

def Ir_A_Algoritmo():
    if (is_file(archivot.get())):
        messagebox.showwarning
        T = LeeLAP2LAP(archivot.get())
        solucionado = [0]*1
        if (originNode.get() < len(T)):
            TSP_FuerzaBruta(T, ciudad, peso, camino, distamin, solup, solucionado, originNode.get())
            if (solucionado[0] != 1):
                messagebox.showwarning("No se pudo encontrar solución", "No se ha podido encontrar un camino, debido a la falta de capacidad del IDLE de Python. Esto sucede, porque la maxima profundidad de recursión que alcanza este algoritmo coincide con el numero de lugares por visitar. Para este caso, la cantidad de centros poblados supera la maxima profundidad de recursion permitida (960-980)")
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
originNode = IntVar()
archivot.set("archivo.txt")
ventanap.geometry("400x400")
ventanap.title("TSP_Program")
imagen1 = PhotoImage(file="mapita.png")
fondo1 = Label(ventanap, image=imagen1).place(x=0,y=0)
Titulo = Label(ventanap, text="TRAVEL SALESMAN PROBLEM (Posibles soluciones)",
                 bg="#FFFF00",fg="#000").place(x=60,y=110)
Option = Label(ventanap, text="Seleccióne la estrategia a probar :",
                 bg="#7FFF00",fg="#000").place(x=105,y=150)
botonA1 = Button(ventanap,text="Fuerza Bruta",command=abrir_ventana2).place(x=90,y=230)
botonA2 = Button(ventanap,text="BFS").place(x = 260,y = 230)
ventanap.mainloop()
