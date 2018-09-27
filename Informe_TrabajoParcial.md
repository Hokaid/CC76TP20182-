
# Informe 

## 1. Introducción

El problema que se va intentar resolver en este proyecto es El problema del vendedor viajero. Este problema consiste en, dado un conjunto de ciudades y las distancias entre ellas, encontrar el camino más corto que recorra cada ciudad exactamente una sola vez y que vuelva a la ciudad de partida. Este es un problema de tipo no polinomial dentro de la optimización combinatoria, muy utilizado en la investigación de operaciones y en la ciencia de la computación. La motivación para el desarrollo de este proyecto radica en poner en practica las estrategias de solución vistas en clase tales como fuerza bruta, backtracking, bfs o dfs. Además, tambien se cuenta con la motivación de intentar solucionar un problema dificil e importante, cuya solución no solo podria traer muchos beneficios al mundo de la informatica, sino tambien a la sociedad en general.

## 2. Objetivos del Proyecto

A. Generar soluciones que estén acorde con los datos respectivos del problema, a partir de un análisis adecuado de los mismos, los cuales son representados bajo diversas formas tales como tablas y gráficos. 

B. Desarrollar soluciónes para el problema dado basadas en la utilización de números y terminos matematicos.

C. Utilizar tecnicas y herramientas modernas en la elaboración de la solución del problema planteado. 

D. Aplicar las tecnicas de solución vistas a lo largo del curso en el desarrollo de las soluciones para el problema dado.

E. Elaborar un marco teórico explicando detalladamente cada una de las estrategias usadas para dar solución al problema planteado. 

F. Determinar la complejidad algorítmica, haciendo uso de la notación Big O, de cada uno de los algoritmos desarrollados.

G. Encontrar soluciones optimas para el problema planteado (Problema del vendedor viajero).

H. Generar una adecuada visualización de resultados de acuerdo a la solución encontrada, mostrando datos relevantes de la misma. 

## 3. Marco Teórico

A continuación, se va a desarrollar el marco teórico correspondiente a cada uno de los algoritmos planteados para dar solución al problema dado.

###      3.1. Marco Teórico del Algoritmo basado en BackTracking y UCS

El algoritmo planteado se basa en encontrar la mayor cantidad de caminos posibles (posibles soluciones para el problema), y apartir de una comparación de todos estos, determinar el camino más corto encontrado. Para este algoritmo, se va a representar el mapa de centros poblados con un grafo. Para este caso particular, cada nodo vendria a representar un centro poblado, y las aristas serian los caminos entre los respectivos centros poblados con la distancia entre estos. La estructura usada para representar este grafo corresponde a una lista de adyacencia de pares ordenados. La posición de la lista en la que se encuentre el par ordenado coincide con el codigo del centro poblado de origen, la primera componente del par ordenado hace referencia a la longitud del camino, mientras que la segunda componente representa el nodo (centro poblado) de destino. A continuación, se pasara a explicar paso a paso cada parte de la estrategia utilizada.

- **Paso 1:** Esta parte del algoritmo esta basada en lo mencionado por Jacqueline Köhler. Köhler (2010) comenta que si se desea obtener una solución rapida (en un tiempo razonable) al problema, sin necesidad de que esta sea la más optima, se puede utilizar el metodo del vecino más cercano. De acuerdo a lo comentado por Köhler (2010), este metodo consiste en formar el camino solución, eligiendo en cada iteración el nodo más cercano para realizar el recorrido. En este paso, se utilizara una variación se ese metodo, ya que se seleccionaran los dos nodos más cercanos para buscar los caminos correspondientes. Siguiendo en este razonamiento, se pasara a explicar lo que implica este paso del algoritmo. Consiste en apartir de un nodo de origen buscar, de todas las posibles aristas que lo conectan con otros nodos **no visitados**, las dos aristas que cuenten con menor peso. Llegados a este punto, se pasara a mostrar el codigo correspondiente a esta parte:

```python
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
```
- **Paso 2:** Una vez encontradas las dos aristas, se procede a realizar el recorrido atraves de cada una de estas llegando a un nuevo nodo. Esta operación se realiza mediante dos llamadas recursivas, en las cuales el nuevo nodo encontrado pasa a ser el nodo en el cual nos encontramos. Luego de realizar esta operación, se estaria regresando al paso 1, generando una progresión recursiva. El codigo correspondiente a lo explicado anteriormente, se muestra a continuación: 

```python
if (menor1_v != -1):
                path1 = copy.copy(path)
                pesos1 = copy.copy(pesos)
                visitados1 = copy.copy(visitados)
                if (salir[0] == False):
                    _TSP_FuerzaBruta(G,menor1_v,path,pesos,distancia + menor1_w,s,visitados,contador+1, origen, MatriPesos, MatriPaths, ArrDistan, MatPer, MatPar, salir)
                    if (menor2_w != math.inf)and(salir[0] == False):
                        _TSP_FuerzaBruta(G,menor2_v,path1,pesos1,distancia + menor2_w,s,visitados1,contador+1, origen, MatriPesos, MatriPaths, ArrDistan, MatPer,MatPar,salir)

```

Además, tambien es importante tener un registro del camino que se esta recorriendo y los pesos acumulados hasta cada nodo en dicho camino. Esto se logra atraves de dos arreglos llamados camino (**Path**) y pesos respectivamente. En el primero, cada posición del arreglo corresponde al codigo de cierto nodo, mientras que el valor que se encuentra en esa posición hace referencia al codigo del nodo padre o nodo antecesor siguiendo la estructura de un camino. En el arreglo de pesos, de igual forma que en el arreglo anterior, cada posición del arreglo representa el codigo de cierto nodo. No obstante, el valor que se encuentra en esa posición es el peso acumulado hasta el nodo referenciado por dicha posición. Asimismo, existe un arreglo que se encarga de llevar el registro de todos los nodos visitados. Antes de terminar con el Paso 2 y volver al Paso 1, se deben de actualizar las estructuras descritas anteriormente. De esta manera se llevara un registro adecuado del camino recorrido y de los nodos visitados hasta el momento. Avanzando en el tema, se pasara a mostrar el codigo relacionado con lo descrito anteriormente: 

```python
            visitados[s] = True
            path[s] = padre
            pesos[s] = distancia
```
- **Paso 3:** Una vez culminado el paso anterior, se procede a volver al Paso 1. El proceso anterior se repite hasta que todos los nodos del grafo hallan sido visitados o hasta que ya no se pueda seguir formando un camino. Llegados a este punto, se pasara a explicar el procedimiento a seguir para cada uno de los casos.

**En el primer caso**, se busca si existe una arista que conecte de forma directa el ultimo nodo visitado con el nodo de origen. Si se encuentra dicha arista entonces se procede a realizar la conexión respectiva. Se actualizan los arreglos correspondientes a los registros de los nodos visitados, el camino y los pesos acumulados hasta cada nodo. Además, se registra el camino encontrado dentro de una matriz llamada **MatriPaths**, al igual que el arreglo de pesos dentro de la matriz **MatriPesos**. Igualmente, se desea tener un registro de todas las distancias totales correspondientes a cada camino, las cuales se guardan en **ArrDistan**. Avanzando en el tema, se pasar a mostrar el codigo respectivo: 

```python
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
```
Sin embargo, si no existe la arista descrita anteriormente, entonces se debe realizar el uso de una estrategia llamada Busqueda de Costo Uniforme o **UCS** por sus siglas en ingles. Según lo comentado por Rihawi (2009), el algoritmo mencionado se basa en ir explorando todos los caminos más cortos que parten del nodo origen y que tienen como nodo destino a los demás, enumerando cada uno de los nodos del espacio de busqueda por costes crecientes; una vez obtenido el camino más corto desde el nodo de partida, hasta el nodo objetivo de la busqueda, el algoritmo se detiene. Este algoritmo es basicamente una busqueda en anchura, pero considerando pesos. Se utilizara dicha estrategia para encontrar el camino mas corto desde el ultimo nodo visitado hasta el nodo de origen. No obstante, algunos nodos seran recorridos 2 veces, lo cual no concuerda con la solución que se desea encontrar. Sin embargo, como se esta utilizando la estrategia UCS, este camino de regreso sera el más corto posible, y por tanto no se alejaría tanto de la solcuión optima. Luego de aplicar UCS, se guarda el camino encontrado por esta estrategia en una matriz llamada **MatPar**, y el registro de los pesos acumulados para cada nodo en la matriz **MatPer**. Adicionalmente, tambien se guardan todos los demas registros especificados anteriormente. Continuando con el asunto, se procedera a mostrar el codigo correspondiente a esta parte:

```python
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
```
**En el segundo caso**, pues si se llega a un nodo, en el cual todas las aristas que salen de el conectan con nodos que ya han sido visitados, pues se determina que el camino recorrido hasta ese momento no es una solución. Luego de esto, se procede a realizar lo denominado como **BackTrack**, es decir, se regresa en la recursividad buscando otros caminos o soluciones.

- El algoritmo utilizado es un hibrido, ya que se basa en varias estrategias para dar solución al problema. Una de estas estrategias corresponden al **Backtracking**, ya que regresa en la recursividad buscando nuevos caminos cuando detecta que el camino que se esta siguiendo no es una posible solución. Asismismo, utiliza el algoritmo **UCS** cuando llega al ultimo nodo por visitar y este no se conecta de forma directa con el nodo de origen. Esto sucede, porque realiza una **Busqueda de Costo Uniforme** para determinar el camino más corto de regreso al nodo de origen. 

###      3.2. Marco Teórico del Algoritmo basado en DFS y Fuerza Bruta
Los recursos recuperados para la implementación del algoritmo se basan en dos puntos principales:
- Información sobre el problema del vendedor viajero (traveling salesman problem).
- Información sobre algoritmos de tipo backtraking que resuelvan problemas con nodos.  

A continuación, se mostrara parte de la imformación recuperada de cada punto.

Investigación sobre TSP:

            A traveling salesman wishes to go to a certain number of destinations in order to sell objects. He wants to
            travel to each destination exactly once and return home taking the shortest total route.
            Each voyage can be represented as a graph G = (V, E) where each destination, including his home, is a
            vertex, and if there is a direct route that connects two distinct destinations then there is an edge between
            those two vertices. The traveling salesman problem is solved if there exists a shortest route that visits each
            destination once and permits the salesman to return home. 
            The traveling salesman problem can be divided into two types: the problems where there is a path between
            every pair of distinct vertices (no road blocks), and the ones where there are not (with road blocks). Both
            of these types of TSP problems are explained in more detail in Chapter 6.
            Though we are not all traveling salesman, this problem interests those who want to optimize their routes,
            either by considering distance, cost, or time. If one has four people in their car to drop off at their respective
            homes, then one automatically tries to think about the shortest distance possible. In this case, distance
            is minimized. If one is traveling to different parts of the city using the public transportation system, then
            minimizing distance might not be the goal, but rather minimizing cost.
            In the first case, each vertex would be a person’s home, and each edge would be the distance between homes.
            In the second case, each vertex would be a destination of the city and each edge would be the cost to get
            from one part of the city to the next. Thus, the Traveling Salesman Problem optimizes routes.
            
 
Algoritmos que resuelvan el TSP:
 
Algoritmo dijkstra C++:

```c++
struct cmp {
    bool operator() ( const Node &a , const Node &b ) {
        return a.second > b.second;
    }
};

vector< Node > ady[ MAX ]; vector<int> distancia[ MAX ];
bool visitado[ MAX ];
priority_queue< Node , vector<Node> , cmp > Q;
int V;

void init(){
    for( int i = 0 ; i <= V ; ++i ){
        for (int j = 0; j <= V; ++j){
            distancia[i].push_back(INF);
        }
        visitado[ i ] = false;
    }
}

void relajacion( int actual , int adyacente , int peso ,int inicial){
    if( distancia[ inicial ][actual] + peso < distancia[ inicial][adyacente ] ){
        distancia[ inicial][adyacente ] = distancia[ inicial ][actual] + peso;
        Q.push( Node( adyacente , distancia[inicial][ adyacente ] ) );
    }
}

void dijkstra( int inicial ){
    init();
    Q.push( Node( inicial , 0 ) );
    distancia[ inicial ][inicial]=0;
    int actual , adyacente , peso;

    while( !Q.empty() ){
        actual = Q.top().first;
        Q.pop();
        if( visitado[ actual ] ) continue;
        visitado[ actual ] = true;

        for( int i = 0 ; i < ady[ actual ].size() ; ++i ){
            adyacente = ady[ actual ][ i ].first;
            peso = ady[ actual ][ i ].second;
            if( !visitado[ adyacente ] ){
                relajacion( actual , adyacente , peso ,inicial);
            }
        }
    }
}

int main(){
    int origen, destino , peso , inicial;
    int f;

    while(cin>>f>>V){
        vector <int> fire(f);
        for(int i=0;i<f;i++){
            scanf("%d",&fire[i]);

        }

        for (int i = 0; i < V; ++i){
            scanf("%d %d %d" , &origen , &destino , &peso );
            ady[ origen ].push_back( Node( destino , peso ) );
            ady[ destino ].push_back( Node( origen, peso ) );
        }

        for (int i = 1; i <= V; ++i){
            dijkstra(i);
        }

        int consulta=0;
        int cont2=INF;

        for (int i = 1; i <= V; ++i){
            int cont=0;
            int nuevo=INF;
            fire.push_back(i);

            for (int k = 1; k <= V; ++k){
                nuevo=INF;
                vector<int>::iterator it=find(fire.begin(),fire.end(),k);
                if(it!=fire.end())continue;

                for (int j = 0; j < fire.size(); ++j){
                    if(k!=fire[j]){
                        if(nuevo>distancia[k][fire[j]]){
                            nuevo=distancia[k][fire[j]];
                        }
                    }
                }

                if(nuevo==INF){
                    nuevo=0;
                }

                cont+=nuevo;
            }

            if(cont2>cont){
                cont2=cont;
                consulta=i;
            }

            fire.pop_back();
        }

        printf("%d",consulta);
        return 0;
    }
}
```

Algoritmo BackTraking phyton:

```python
import time
class Graphe:
    def __init__(self,graphe):
        self.graphe =graphe
        self.coutMin=None
        self.cheminMin=None
        self.cpt=0
    def arcExist(self,i,j):
        if self.graphe[i][j]!=None:
            return True
        return False
    def dejaVisite(self,chemin,e):
        return self.estElement(chemin,e)
    
    def genererCircuit(self,chemin,n):
        if self.longueur(chemin)==n and self.arcExist(self.queue(chemin),self.tete(chemin)):
            chemin1=self.cloner(chemin)
            chemin1=self.ajouterEnQueue(chemin1,chemin1[0])
            # self.imprimer(chemin1)
            a=self.coutChemin(chemin)
            # print 'cout du chemin'
            # print a
            self.cpt+=1
        else:  
          for s in range(n):
              s=s+1
              if self.arcExist(self.queue(chemin),s) and self.dejaVisite(chemin,s)==False:
                  ch=self.cloner(chemin)
                  self.ajouterEnQueue(ch,s)
                  self.genererCircuit(ch,n)
    def genererTousLesCircuits(self,sommetDepart,n):
        chemin=self.creer()
        self.ajouterEnQueue(chemin,sommetDepart)
        self.genererCircuit(chemin,n)
        
    def creer(self):
        seq=[]
        return seq
    def longueur(self,seq):
        return len(seq)
    def cloner(self,seq):
        s1=[]
        for i in seq:
            s1.append(i)            
        return s1
    def ajouterEnQueue(self,seq,sommet):
        seq.append(sommet)
        return seq
    def tete(self,seq):
        if seq:
            return seq[0]
    def queue(self,seq):
        if seq:
            return seq[-1]
    def element(self,seq,i):
        if seq[i]:
            return seq[i]
    def estElement(self,seq,s):
        if s in seq:
            return True
        return False
    def imprimer(self,seq):
        print seq
    def coutChemin(self,seq):
        if self.longueur(seq)>1:
            cout=0
            for i in range(self.longueur(seq)-1):
                if self.arcExist(seq[i],seq[i+1]):
                    cout+=self.graphe[seq[i]][seq[i+1]]
            return cout
        else:
            return None
    def explorerCircuits(self,chemin,n):
        if self.longueur(chemin)==n and self.arcExist(self.queue(chemin),self.tete(chemin)):
            cout=self.coutChemin(chemin)+self.graphe[self.queue(chemin)][self.tete(chemin)]
            chemin1=self.cloner(chemin)
            chemin1=self.ajouterEnQueue(chemin1,chemin1[0])
            # self.imprimer(chemin1)
            # print 'cout du chemin'
            # print cout
            self.cpt+=1
            if self.coutMin==None:
                self.coutMin=cout
            if cout<self.coutMin:
                self.cheminMin=chemin
                self.ajouterEnQueue(self.cheminMin,self.cheminMin[0])
                self.coutMin=cout
        else:
            for s in range(n):
              s=s+1
              if self.arcExist(self.queue(chemin),s) and self.dejaVisite(chemin,s)==False:
                  ch=self.cloner(chemin)
                  self.ajouterEnQueue(ch,s)
                  self.explorerCircuits(ch,n)
    def trouverCircuitMin(self,sommetDepart,n):
        chemin=self.creer()
        self.ajouterEnQueue(chemin,sommetDepart)
        self.explorerCircuits(chemin,n)
            
                
        
tps1 = time.clock() 
#w=[None,[None,None,2,9,None],[None,1,None,6,4],[None,None,7,None,8],[None,6,3,None,None]]
#villes=[None,[None,None,27,43,16,30,26],[None,7,None,16,1,30,25],[None,20,13,None,35,5,0],[None,21,16,25,None,18,18],[None,12,46,27,48,None,5],[None,23,5,5,9,5,None]]
#villes1=[None,[None,None,27,43,16,30,26],[None,7,None,16,1,30,25],[None,20,13,None,35,5,0],[None,21,16,25,None,18,18],[None,12,46,27,48,None,5],[None,23,5,5,9,5,None]]
#villes2=[None,[None,None,27,43,16,30,26,75,28,29,90],[None,7,None,16,1,30,25,60,0,41,80],[None,20,13,None,35,5,0,80,90,100,70],[None,21,16,25,None,18,18,55,25,21,60],[None,12,46,27,48,None,5,56,28,15,50],[None,23,5,5,9,5,None,19,18,21,40],[None,23,5,5,9,5,None,19,18,21,40],[None,23,5,5,9,5,None,19,18,21,40],[None,23,5,5,9,5,None,19,18,21,40],[None,23,5,5,9,5,None,19,18,21,40]]
#villes3=[None,[None,None,5,43,16,30,26,75,28,29,90,26,75,28,29,90],[None,5,None,43,16,30,26,75,28,29,90,26,75,28,29,90],[None,8,27,None,16,30,26,75,28,29,90,26,75,28,29,90],[None,1,27,43,None,30,26,75,28,29,90,26,75,28,29,90],[None,1,27,43,16,None,26,75,28,29,90,26,75,28,29,90],[None,5,27,43,16,30,None,75,28,29,90,26,75,28,29,90],[None,1,27,43,16,30,26,None,28,29,90,26,75,28,29,90],[None,2,27,43,16,30,26,75,None,29,90,26,75,28,29,90],[None,1,27,43,16,30,26,75,28,None,90,26,75,28,29,90],[None,1,27,43,16,30,26,75,28,29,None,26,75,28,29,90],[None,1,27,43,16,30,26,75,28,29,90,None,75,28,29,90],[None,1,27,43,16,30,26,75,28,29,90,26,None,28,29,90],[None,1,27,43,16,30,26,75,28,29,90,26,75,None,29,90],[None,1,27,43,16,30,26,75,28,29,90,26,75,28,None,90],[None,1,27,43,16,30,26,75,28,29,90,26,75,28,29,None]]
villes2 = [None, [None, None, 2, 12, 6, 15, 16, 20, 13, 14, 16, 23, 23, 29, 25, 26, 27],
           [None, 2, None, 10, 8, 17, 18, 18, 15, 16, 18, 25, 25, 27, 27, 28, 29],
           [None, 12, 10, None, 14, 15, 14, 10, 25, 26, 26, 19, 23, 17, 29, 28, 27],
           [None, 6, 8, 14, None, 17, 18, 16, 15, 16, 18, 25, 26, 23, 27, 28, 29],
           [None, 15, 17, 15, 17, None, 1, 5, 16, 17, 19, 16, 20, 14, 26, 25, 24],
           [None, 16, 18, 14, 18, 1, None, 4, 17, 18, 20, 15, 19, 13, 25, 24, 23],
           [None, 20, 18, 10, 16, 5, 4, None, 21, 20, 18, 11, 15, 9, 21, 20, 19],
           [None, 13, 15, 25, 15, 16, 17, 21, None, 1, 3, 10, 12, 16, 14, 15, 16],
           [None, 14, 16, 26, 16, 17, 18, 20, 1, None, 2, 9, 13, 15, 15, 16, 17],
           [None, 16, 18, 26, 18, 19, 20, 18, 3, 2, None, 7, 15, 13, 17, 18, 19],
           [None, 23, 25, 19, 25, 16, 15, 11, 10, 9, 7, None, 12, 6, 18, 17, 16],
           [None, 23, 25, 23, 26, 20, 19, 15, 12, 13, 15, 12, None, 6, 18, 17, 16],
           [None, 29, 27, 17, 23, 14, 13, 9, 16, 15, 13, 6, 6, None, 12, 11, 10],
           [None, 25, 27, 29, 27, 26, 25, 21, 14, 15, 17, 18, 18, 12, None, 1, 2],
           [None, 26, 28, 28, 28, 25, 24, 20, 15, 16, 18, 17, 17, 11, 1, None, 1],
           [None, 27, 29, 27, 29, 24, 23, 23, 19, 16, 17, 19, 16, 16, 10, 2, 1, None]]

w=[None,[None,None,76,43,38,51,42,19,80],
   [None,42,None,49,26,78,52,39,87],
   [None,48,28,None,40,63,44,68,61],
   [None,72,31,29,None,42,49,50,38],
   [None,30,52,38,47,None,64,72,82],
   [None,66,51,83,51,22,None,37,71],
   [None,77,62,93,54,69,38,None,26],
   [None,42,58,66,76,41,52,83,None]]
g=Graphe(villes2)
print "Tous les ciruits visites pour calculer le chemin min"
#g.genererTousLesCircuits(1,4)
g.trouverCircuitMin(1,16)
print "nombre de chemins"
print g.cpt
print "chemin min"
print g.cheminMin
print "Cout min"
print g.coutMin
tps2 = time.clock()
print "temps d'execution"
print(tps2 - tps1)

```

## 4. Analisis de Complejidad Algoritmica
-A continuación, se pasará a definir el concepto de complejidad algorítmica:
 “La complejidad algorítmica representa la cantidad de recursos (temporales) que necesita un algoritmo para resolver un problema y por     tanto permite determinar la eficiencia de dicho algoritmo.”                   (Departamento de Informática Universidad de Valladolid). Llegados a este punto, se procederá a analizar la complejidad algorítmica de cada uno de los algoritmos planteados. 
###      4.1. Analisis del Algoritmo basado en BackTracking y UCS

Para realizar este analisis, se procedera a representar el tiempo de ejecución de nuestro algoritmo mediante una función **T(n)**, la cual es una función que depende de **n**. Además, se debe tener en cuenta que, para este caso particular, **n** representa el numero de nodos o lugares por visitar en el algoritmo planteado. 

- El algoritmo a analizar es un algoritmo recursivo, cuyo tiempo de ejcución posee la siguiente forma:

                                                T(n) = a*T(n-1) + O(n^k)
          
          a: este valor representa el numero de llamadas recursivas que se van realizar dentro de una llamada de la función.
          k: este valor determina la complejidad de los procedimientos realizados en la función aparte de las llamadas recursivas.
 
 Es importante resaltar que en la llamada recursiva, **n** se reduce en una unidad, debido a que en cada llamada recursiva se visita un nodo. Esto causa que cada vez queden menos nodos o lugares por visitar, lo que implica que se reduzca el tamaño del problema en una unidad por cada llamada recursiva.
 
- Para el caso de este algoritmo, **a** adquiere el valor de 2, ya que en cada llamada de la función se realizan 2 llamadas recursivas correspondientes a los 2 nodos más cercanos. Del mismo modo, **k** toma el valor de 0, debido a que la complejidad de las operaciones ejecutadas en la función sin considerar las llamadas recursivas es independiente del valor de **n**, y posee tiempo constante. Reanudando el tema, se pasara a representar lo dicho anteriormente:

                                                T(n) = 2*T(n-1) + O(1)
                                                
- En las expresones que se determinaran a continuación se hace referencia a la expresión **O(n)** con **1**. Si se lleva a cabo un analisis un poco exaustivo, aplicando la recursividad unas cuantas veces y siguiendo la formula anterior, se pueden obtener las siguiente expresiones:

                                (1)................T(n) = 2*T(n-1)+1
                                (2)................T(n) = 2*(2*T(n-2)+1)+1
                                (3)................T(n) = 2*(2*(2*T(n-3)+1)+1)+1
                                (4)................T(n) = 2*(2*(2*(2*T(n-4)+1)+1)+1)+1
                                (5)................T(n) = 2*(2*(2*(2*(2*T(n-5)+1)+1)+1)+1)+1
                                
- Como se puede apreciar, mientras más se va siguiendo la recursividad, se puede notar que se va formando un patron. Analizando nuevamente y simplificando cada espresión, se determina el siguiente patron: 

                                (i)................T(n) = (2^i)*T(n-i)+(2^i)-1
                                
              i: este valor corresponde al nivel de profundidad alacanzado en la recursividad.
                                
- De esta forma, si se desea obtener la complejidad del algoritmo planteado, basta con remplazar el valor de **i** con el valor de **n**. Esto es así, ya que se debe tener en cuenta que la maxima profundidad recursiva alcanzada por el algoritmo coincide con el valor de **n**. Si se realiza la operación descrita anteriormente, se obtiene lo siguiente:

                                (n)................T(n) = (2^n)*T(n-n)+(2^n)-1
                                
- Se va a considerar que **T(n-n)**, es decir, **T(0)** adquiere el valor de 1. Esto es así, debido a que se detectaría que en el grafo ya no hay más nodos por visitar y finalizaría el algoritmo sin realizar ninguna operación. Avanzando en el tema, se pasara a representar el resultado obtenido aplicando lo dicho anteriormente:

                                                T(n) = (2^n)*1+(2^n)-1
                                                T(n) = 2*(2^n)-1

- Aplicando la notación Big O, se obtendria la siguiente expresión para representar la complejidad del algoritmo en el caso optimo de que nunca sea necesario utilizar la estrategia **UCS**:

                                             Notación Big O: O(2^n)
                                             
- No obstante, como ya se menciono, la notación utilizada anteriormente representa la complejidad del algoritmo solo en el caso ideal de que nunca haya sido necesario recurrir al uso de la estrategia **UCS**. En el algoritmo planteado, si se terminan de recorrer todos los nodos y no existe una arista que conecte derectamente el ultimo nodo visitado con el nodo de origen, entonces se procede a aplicar la estrategia de la **Búsqueda de Costo Uniforme** (**UCS**). Se procede a buscar a partir del ultimo nodo visitado, el camino más corto hacia el nodo de origen. Esta operación se realiza atraves de una busqueda **UCS**. Si en el grafo sobre el cual se aplica este algoritmo, todos los nodos estan conectados entre si atraves de solo una arista, entonces nunca sera necesario el uso de la estrategia **UCS**. Por lo tanto, para ese caso, se podria considerar la expresión determinada anteriormente para representar la complejidad del algoritmo. Ahora bien, se debe analizar la complejidad algoritmica a partir del peor caso. En ese sentido, el peor caso para este algoritmo consistiría en haber utilizado la **Búsqueda de Costo Uniforme** para construir todos y cada uno de los caminos (soluciones) encontrados. Por lo tanto, si se desea conocer la complejidad algoritmica para este caso, sería conveniente determinar primero la complejidad del algoritmo **UCS**. Este algoritmo recorre cada nodo una sola vez. El procedmiento que sigue consiste en agregar los nodos hijos de cada nodo padre a una cola de prioridad, asignadoles a cada uno un valor de prioridad correpondiente al peso de la arista que se debe recorrer para llegar a dicho nodo. De esta manera, un nodo más cercano tiene mayor prioridad que uno más lejano. En la cola de prioridad, los nodos de mayor prioridad deben salir de la cola primero que los de menor. De acuerdo a lo dicho anteriormente, en el algoritmo **UCS** se va liberando cada nodo de la cola de prioridad, agregando sus nodos hijos con su valor de prioridad debidamente asignado. El algoritmo se detiene cuando se encuentra el nodo objetivo. En consecuencia, al finalizar el algoritmo, se termina realizando una busqueda en anchura (**BFS**), pero considerando costos, de tal forma que primero se busca en los nodos más cercanos. De acuerdo a lo investigado, es sumamente complicado determinar la complejidad exacta de este algoritmo, ya que depende mucho de la forma en la que estan distribuidas las aristas, los pesos de las aristas y los nodos del grafo respectivo. Por esta razón, se ha decidido basarse en algunas fuentes para poder dar una expresión que estime dicha complejidad. De acuerdo a lo argumentado por Fernando (2017), se puede realizar una aproximación a la complejidad del algoritmo **UCS** en el peor de los casos, asumiendo que cada uno de los arcos del arbol tiene un coste mínimo **p** y que el tiempo de la solución optima viene dado por **C**. Por lo tanto, y siguiendo lo mencionado por Fernando (2017), se puede verificar que la complejidad basada en tiempo y espacio para **UCS** es:

                                             Notación Big O: O(h^(1+(C/p)))
                                             
                  h: este valor corresponde al número promedio de descendientes por nodo.
                                             
En este sentido, para el peor caso, el cual consiste en que para todos los caminos encontrados haya sido necesario el uso del algoritmo **UCS**, la complejidad algoritmica o el tiempo de ejecución **T(n)** se podria aproximar con la siguiente expresión:

                                             T(n) = 2^n + X*(h^(1+(C/p)))
                                        
                  n: representa el numero de nodos o lugares por visitar en el algoritmo planteado.
                  h: este valor corresponde al número promedio de descendientes por nodo.
                  p: peso mínimo de los arcos en el grafo.
                  C: representa el tiempo de la solución optima para el algoritmo UCS.
                  X: numero de caminos (soluciones) encontrados.
                 
- Sin embargo, la expresión dada anteriormente no representa la complejidad real del algoritmo, ya que para la mayoria de los casos, se va a utilizar en muy pocas ocasiones el algoritmo **UCS**. Por lo tanto, se podria estimar la complejidad del algoritmo como una expresión que varia entre la primera Notación Big O dada (**(2^n)**) y la ultima expresión representada, dependiendo de las condiciones del grafo. 
                 

###      4.2. Analisis del Algoritmo basado en DFS y Fuerza Bruta

Para determinar la complejidad del algoritmo propuesto se hará uso de la siguiente formula, es importante resaltar que la formula propuesta nos ayudara a determinar la complejidad de la parte recursiva de este. 

                                                T(n) = a*T(n-1) + O(n^k)
                                                
            a: este valor representa el numero de llamadas recursivas que se van realizar dentro de una llamada de la función.
            k: este valor determina la complejidad de los procedimientos realizados en la función aparte de las llamadas recursivas.

El resultado de la complejidad del algoritmo se presentará mediante la notación big(o). Esta notación es la más adecuada para satisfacer uno de los objetivos del proyecto, determinar la complejidad de un algoritmo en el peor escenario posible que este pueda presentar. 
Teniendo en cuenta lo mencionado anteriormente, se mostrará una imagen de la función recursiva del algoritmo. En ella se hallará la complejidad big(o), ya que en dicha función se presenta el núcleo del algoritmo.

```python
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
```
Al analizar el algoritmo, se evidencia los valores de ‘a’ y ‘k’. Al remplazar los valores encontrados en la fórmula se obtendrá la siguiente igualdad.

                                                   T(n) = 2*T(n-1) + O(1)
                                                            
Cuando seguimos el recorrido de la recursividad en el algoritmo vemos que la igualdad cambiara, ya que para cada llamada el T(n-1) ira aumentado hasta llegar la condición de parada. Es por ello que la identidad, definida anteriormente, permutara en cada llamada recursiva de la siguiente forma:    


                                      Primera entrada recursiva  T(n) = 2*T(n-1)+1
                                      Segunda entrada recursiva  T(n) = 2*(2*T(n-2)+1)+1
                                      Tercera entrada recursiva  T(n) = 2*(2*(2*T(n-3)+1)+1)+1
                                      Cuarta entrada recursiva  T(n) = 2*(2*(2*(2*T(n-4)+1)+1)+1)+1
                                      Quinta entrada recursiva  T(n) = 2*(2*(2*(2*(2*T(n-5)+1)+1)+1)+1)+1
		                                    .	.
			                        .
			                        .

La permutación de la identidad toma una forma que asemeja la de una progresión, gracias ello podemos hacer uso de la ‘inducción matemática’ para generalizar la progresión:
                                      
                                                    (2^n)*T(n-n)+(2^n)-1
                                                    
                                                    
Resolviendo por concemtos matematicos nos queda la complejidad final del algoritmo:
                                                   
                                                     Big(o): O(2^n)
                                                     
En concecuencia, concluimos que el algoritmo basado en DFS y Fuerza Bruta es inmanejable, ya que la complejidad del algoritmo es exponencial.                                                   

## 5. Conclusiones
- En conclusión, se cumplieron los objetivos propuestos satisfactoriamente. Se desarrollo soluciones basadas en el problema dado haciendo uso de herramientas y técnicas (Algoritmos) aprendidas a lo largo del curso. Los algoritmos usados para dicha solución son: Backtraking-UCS y DFS. De la misma forma, se evidencio la aplicación de las competencias generales y específicas, siendo estas las de Razonamiento Cuantitativo y, Planificación y Conducción de Experimentos respectivamente. Esto se ve reflejado en el uso de técnicas matemáticas (Teorema Maestro) para hallar la complejidad de los algoritmos implementados y la exhaustiva investigación de algoritmos que den una solución adecuada al problema planteado. Para finalizar, el presente trabajo satisface los objetivos planteados.
## 6. Bibliografía 

- Köhler, J. [jkohlerc]. (17 de enero de 2010). Problema del vendedor viajero [Archivo de video]. Recuperado de https://www.youtube.com/watch?v=EutHYzkSo5Y&t=5s 

- Rihawi, I. (6 de diciembre de 2009). Búsqueda no informada: Algoritmo de Coste Uniforme. Recuperado de https://poiritem.wordpress.com/2009/12/06/6-5-1-busqueda-no-informada-algoritmo-de-coste-uniforme/ 

- Fernando, P. (18 de diciembre de 2017). Algoritmo para búsqueda con coste uniforme. Recuperado de https://www.revolucionia.com/2017/12/Algoritmo_para_busqueda_con_coste_uniforme.html
