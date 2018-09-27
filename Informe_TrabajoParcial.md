# Informe 

## 1. Introducción

El problema que se va intentar resolver en este proyecto es El problema del vendedor viajero. Este problema consiste en, dado un conjunto de ciudades y las distancias entre ellas, encontrar el camino más corto que recorra cada ciudad exactamente una sola vez y que vuelva a la ciudad de partida. Este es un problema de tipo no polinomial dentro de la optimización combinatoria, muy utilizado en la investigación de operaciones y en la ciencia de la computación. La motivación para el desarrollo de este proyecto radica en poner en práctica las estrategias de solución vistas en clase tales como fuerza bruta, backtracking, bfs o dfs. Asimismo, también se cuenta con la motivación de intentar solucionar un problema difícil e importante, cuya solución no solo podría traer muchos beneficios al mundo de la informática, sino también a la sociedad en general.

## 2. Objetivos del Proyecto

A. Generar soluciones que estén acorde con los datos respectivos del problema, a partir de un análisis adecuado de los mismos, los cuales son representados bajo diversas formas tales como tablas y gráficos. 

B. Desarrollar soluciones para el problema dado basadas en la utilización de números y términos matemáticos.

C. Utilizar técnicas y herramientas modernas en la elaboración de la solución del problema planteado. 

D. Aplicar las técnicas de solución vistas a lo largo del curso en el desarrollo de las soluciones para el problema dado.

E. Elaborar un marco teórico explicando detalladamente cada una de las estrategias usadas para dar solución al problema planteado. 

F. Determinar la complejidad algorítmica, haciendo uso de la notación Big O, de cada uno de los algoritmos desarrollados.

G. Encontrar soluciones óptimas para el problema planteado (Problema del vendedor viajero).

H. Generar una adecuada visualización de resultados de acuerdo a la solución encontrada, mostrando datos relevantes de la misma. 

## 3. Marco Teórico

A continuación, se va a desarrollar el marco teórico correspondiente a cada uno de los algoritmos planteados para dar solución al problema dado.

###      3.1. Marco Teórico del Algoritmo basado en BackTracking y UCS

El algoritmo planteado se basa en encontrar la mayor cantidad de caminos posibles (posibles soluciones para el problema), y a partir de una comparación de todos estos, determinar el camino más corto encontrado. Para este algoritmo, se va a representar el mapa de centros poblados con un grafo. Para este caso particular, cada nodo vendría a representar un centro poblado, y las aristas serían los caminos entre los respectivos centros poblados con la distancia entre estos. La estructura usada para representar este grafo corresponde a una lista de adyacencia de pares ordenados. La posición de la lista en la que se encuentre el par ordenado coincide con el código del centro poblado de origen, la primera componente del par ordenado hace referencia a la longitud del camino, mientras que la segunda componente representa el nodo (centro poblado) de destino. A continuación, se pasara a explicar paso a paso cada parte de la estrategia utilizada.

- **Paso 1:** Esta parte del algoritmo está basada en lo mencionado por Jacqueline Köhler. Köhler (2010) comenta que si se desea obtener una solución rápida (en un tiempo razonable) al problema, sin necesidad de que esta sea la más óptima, se puede utilizar el método del vecino más cercano. De acuerdo a lo comentado por Köhler (2010), este método consiste en formar el camino solución, eligiendo en cada iteración el nodo más cercano para realizar el recorrido. En este paso, se utilizara una variación se ese método, ya que se seleccionaran los dos nodos más cercanos para buscar los caminos correspondientes. Siguiendo en este razonamiento, se pasara a explicar lo que implica este paso del algoritmo. Consiste en a partir de un nodo de origen buscar, de todas las posibles aristas que lo conectan con otros nodos **no visitados**, las dos aristas que cuenten con menor peso. Llegados a este punto, se pasara a mostrar el código correspondiente a esta parte:

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
- **Pasó 2:** Una vez encontradas las dos aristas, se procede a realizar el recorrido a través de cada una de estas llegando a un nuevo nodo. Esta operación se realiza mediante dos llamadas recursivas, en las cuales el nuevo nodo encontrado pasa a ser el nodo en el cual nos encontramos. Luego de realizar esta operación, se estaría regresando al paso 1, generando una progresión recursiva. El código correspondiente a lo explicado anteriormente, se muestra a continuación: 

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

Además, también es importante tener un registro del camino que se está recorriendo y los pesos acumulados hasta cada nodo en dicho camino. Esto se logra a través de dos arreglos llamados camino (**Path**) y pesos respectivamente. En el primero, cada posición del arreglo corresponde al código de cierto nodo, mientras que el valor que se encuentra en esa posición hace referencia al código del nodo padre o nodo antecesor siguiendo la estructura de un camino. En el arreglo de pesos, de igual forma que en el arreglo anterior, cada posición del arreglo representa el código de cierto nodo. No obstante, el valor que se encuentra en esa posición es el peso acumulado hasta el nodo referenciado por dicha posición. Asimismo, existe un arreglo que se encarga de llevar el registro de todos los nodos visitados. Antes de terminar con el Paso 2 y volver al Paso 1, se deben de actualizar las estructuras descritas anteriormente. De esta manera se llevara un registro adecuado del camino recorrido y de los nodos visitados hasta el momento. Avanzando en el tema, se pasara a mostrar el código relacionado con lo descrito anteriormente: 

```python
            visitados[s] = True
            path[s] = padre
            pesos[s] = distancia
```
- **Pasó 3:** Una vez culminado el paso anterior, se procede a volver al Paso 1. El proceso anterior se repite hasta que todos los nodos del grafo hayan sido visitados o hasta que ya no se pueda seguir formando un camino. Llegados a este punto, se pasara a explicar el procedimiento a seguir para cada uno de los casos.

**En el primer caso**, se busca si existe una arista que conecte de forma directa el ultimo nodo visitado con el nodo de origen. Si se encuentra dicha arista entonces se procede a realizar la conexión respectiva. Se actualizan los arreglos correspondientes a los registros de los nodos visitados, el camino y los pesos acumulados hasta cada nodo. Además, se registra el camino encontrado dentro de una matriz llamada **MatriPaths**, al igual que el arreglo de pesos dentro de la matriz **MatriPesos**. Igualmente, se desea tener un registro de todas las distancias totales correspondientes a cada camino, las cuales se guardan en **ArrDistan**. Avanzando en el tema, se pasar a mostrar el código respectivo: 

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
Sin embargo, si no existe la arista descrita anteriormente, entonces se debe realizar el uso de una estrategia llamada Búsqueda de Costo Uniforme o **UCS** por sus siglas en ingles. Según lo comentado por Rihawi (2009), el algoritmo mencionado se basa en ir explorando todos los caminos más cortos que parten del nodo origen y que tienen como nodo destino a los demás, enumerando cada uno de los nodos del espacio de búsqueda por costes crecientes; una vez obtenido el camino más corto desde el nodo de partida, hasta el nodo objetivo de la búsqueda, el algoritmo se detiene. Este algoritmo es básicamente una búsqueda en anchura, pero considerando pesos. Se utilizara dicha estrategia para encontrar el camino más corto desde el último nodo visitado hasta el nodo de origen. No obstante, algunos nodos serán recorridos 2 veces, lo cual no concuerda con la solución que se desea encontrar. Sin embargo, como se está utilizando la estrategia UCS, este camino de regreso será el más corto posible, y por tanto no se alejaría tanto de la solución óptima. Luego de aplicar UCS, se guarda el camino encontrado por esta estrategia en una matriz llamada **MatPar**, y el registro de los pesos acumulados para cada nodo en la matriz **MatPer**. Adicionalmente, también se guardan todos los demás registros especificados anteriormente. Continuando con el asunto, se procederá a mostrar el código correspondiente a esta parte:

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

- El algoritmo utilizado es un hibrido, ya que se basa en varias estrategias para dar solución al problema. Una de estas estrategias corresponden al **Backtracking**, ya que regresa en la recursividad buscando nuevos caminos cuando detecta que el camino que se está siguiendo no es una posible solución. Asimismo, utiliza el algoritmo **UCS** cuando llega al último nodo por visitar y este no se conecta de forma directa con el nodo de origen. Esto sucede, porque realiza una **Búsqueda de Costo Uniforme** para determinar el camino más corto de regreso al nodo de origen. 

###      3.2. Marco Teórico del Algoritmo basado en DFS y Fuerza Bruta
## 4. Análisis de Complejidad Algorítmica
###      4.1. Análisis del Algoritmo basado en BackTracking y UCS

Para realizar este análisis, se procederá a representar el tiempo de ejecución de nuestro algoritmo mediante una función **T(n)**, la cual es una función que depende de **n**. Además, se debe tener en cuenta que, para este caso particular, **n** representa el número de nodos o lugares por visitar en el algoritmo planteado. 

- El algoritmo a analizar es un algoritmo recursivo, cuyo tiempo de ejecución posee la siguiente forma:

                                                T(n) = a*T(n-1) + O(n^k)
          
          a: este valor representa el número de llamadas recursivas que se van realizar dentro de una llamada de la función.
          k: este valor determina la complejidad de los procedimientos realizados en la función aparte de las llamadas recursivas.
 
 Es importante resaltar que en la llamada recursiva, **n** se reduce en una unidad, debido a que en cada llamada recursiva se visita un nodo. Esto causa que cada vez queden menos nodos o lugares por visitar, lo que implica que se reduzca el tamaño del problema en una unidad por cada llamada recursiva.
 
- Para el caso de este algoritmo, **a** adquiere el valor de 2, ya que en cada llamada de la función se realizan 2 llamadas recursivas correspondientes a los 2 nodos más cercanos. Del mismo modo, **k** toma el valor de 0, debido a que la complejidad de las operaciones ejecutadas en la función sin considerar las llamadas recursivas es independiente del valor de **n**, y posee tiempo constante. Reanudando el tema, se pasara a representar lo dicho anteriormente:

                                                T(n) = 2*T(n-1) + O(1)
                                                
- En las expresiones que se determinaran a continuación se hace referencia a la expresión **O(n)** con **1**. Si se lleva a cabo un análisis un poco exhaustivo, aplicando la recursividad unas cuantas veces y siguiendo la formula anterior, se pueden obtener las siguientes expresiones:

                                (1)................T(n) = 2*T(n-1)+1
                                (2)................T(n) = 2*(2*T(n-2)+1)+1
                                (3)................T(n) = 2*(2*(2*T(n-3)+1)+1)+1
                                (4)................T(n) = 2*(2*(2*(2*T(n-4)+1)+1)+1)+1
                                (5)................T(n) = 2*(2*(2*(2*(2*T(n-5)+1)+1)+1)+1)+1
                                
- Como se puede apreciar, mientras más se va siguiendo la recursividad, se puede notar que se va formando un patrón. Analizando nuevamente y simplificando cada expresión, se determina el siguiente patrón: 

                                (i)................T(n) = (2^i)*T(n-i)+(2^i)-1
                                
              i: este valor corresponde al nivel de profundidad alcanzado en la recursividad.
                                
- De esta forma, si se desea obtener la complejidad del algoritmo planteado, basta con remplazar el valor de **i** con el valor de **n**. Esto es así, ya que se debe tener en cuenta que la máxima profundidad recursiva alcanzada por el algoritmo coincide con el valor de **n**. Si se realiza la operación descrita anteriormente, se obtiene lo siguiente:

                                (n)................T(n) = (2^n)*T(n-n)+(2^n)-1
                                
- Se va a considerar que **T(n-n)**, es decir, **T(0)** adquiere el valor de 1. Esto es así, debido a que se detectaría que en el grafo ya no hay más nodos por visitar y finalizaría el algoritmo sin realizar ninguna operación. Avanzando en el tema, se pasara a representar el resultado obtenido aplicando lo dicho anteriormente:

                                                T(n) = (2^n)*1+(2^n)-1
                                                T(n) = 2*(2^n)-1

- Aplicando la notación Big O, se obtendría la siguiente expresión para representar la complejidad del algoritmo en el caso óptimo de que nunca sea necesario utilizar la estrategia **UCS**:

                                             Notación Big O: O(2^n)
                                             
- No obstante, como ya se mencionó, la notación utilizada anteriormente representa la complejidad del algoritmo solo en el caso ideal de que nunca haya sido necesario recurrir al uso de la estrategia **UCS**. En el algoritmo planteado, si se terminan de recorrer todos los nodos y no existe una arista que conecte directamente el ultimo nodo visitado con el nodo de origen, entonces se procede a aplicar la estrategia de la **Búsqueda de Costo Uniforme** (**UCS**). Se procede a buscar a partir del último nodo visitado, el camino más corto hacia el nodo de origen. Esta operación se realiza a través de una búsqueda **UCS**. Si en el grafo sobre el cual se aplica este algoritmo, todos los nodos están conectados entre sí a través de solo una arista, entonces nunca será necesario el uso de la estrategia **UCS**. Por lo tanto, para ese caso, se podría considerar la expresión determinada anteriormente para representar la complejidad del algoritmo. Ahora bien, se debe analizar la complejidad algorítmica a partir del peor caso. En ese sentido, el peor caso para este algoritmo consistiría en haber utilizado la **Búsqueda de Costo Uniforme** para construir todos y cada uno de los caminos (soluciones) encontrados. Por lo tanto, si se desea conocer la complejidad algorítmica para este caso, sería conveniente determinar primero la complejidad del algoritmo **UCS**. Este algoritmo recorre cada nodo una sola vez. El procedimiento que sigue consiste en agregar los nodos hijos de cada nodo padre a una cola de prioridad, asignándole a cada uno un valor de prioridad correspondiente al peso de la arista que se debe recorrer para llegar a dicho nodo. De esta manera, un nodo más cercano tiene mayor prioridad que uno más lejano. En la cola de prioridad, los nodos de mayor prioridad deben salir de la cola primero que los de menor. De acuerdo a lo dicho anteriormente, en el algoritmo **UCS** se va liberando cada nodo de la cola de prioridad, agregando sus nodos hijos con su valor de prioridad debidamente asignado. El algoritmo se detiene cuando se encuentra el nodo objetivo. En consecuencia, al finalizar el algoritmo, se termina realizando una búsqueda en anchura (**BFS**), pero considerando costos, de tal forma que primero se busca en los nodos más cercanos. De acuerdo a lo investigado, es sumamente complicado determinar la complejidad exacta de este algoritmo, ya que depende mucho de la forma en la que están distribuidas las aristas, los pesos de las aristas y los nodos del grafo respectivo. Por esta razón, se ha decidido basarse en algunas fuentes para poder dar una expresión que estime dicha complejidad. De acuerdo a lo argumentado por Fernando (2017), se puede realizar una aproximación a la complejidad del algoritmo **UCS** en el peor de los casos, asumiendo que cada uno de los arcos del árbol tiene un coste mínimo **p** y que el tiempo de la solución óptima viene dado por **C**. Por lo tanto, y siguiendo lo mencionado por Fernando (2017), se puede verificar que la complejidad basada en tiempo y espacio para **UCS** es:

                                             Notación Big O: O(h^(1+(C/p)))
                                             
                  h: este valor corresponde al número promedio de descendientes por nodo.
                                             
En este sentido, para el peor caso, el cual consiste en que para todos los caminos encontrados haya sido necesario el uso del algoritmo **UCS**, la complejidad algorítmica o el tiempo de ejecución **T(n)** se podría aproximar con la siguiente expresión:

                                             T(n) = O(2^n) + X*O(h^(1+(C/p)))
                                        
                  n: representa el número de nodos o lugares por visitar en el algoritmo planteado.
                  h: este valor corresponde al número promedio de descendientes por nodo.
                  p: peso mínimo de los arcos en el grafo.
                  C: representa el tiempo de la solución óptima para el algoritmo UCS.
                  X: número de caminos (soluciones) encontrados.
                 
- Sin embargo, la expresión dada anteriormente no representa la complejidad real del algoritmo, ya que para la mayoría de los casos, se va a utilizar en muy pocas ocasiones el algoritmo **UCS**. Esto sucede porque no siempre va a ser necesario hacer uso de dicho algoritmo para encontrar un camino (solución). Por lo tanto, se podría estimar la complejidad del algoritmo como una expresión que varía entre la primera Notación Big O dada (**(2^n)**) y la última expresión representada, dependiendo de las condiciones del grafo. 
                 

###      4.2. Análisis del Algoritmo basado en DFS y Fuerza Bruta
## 5. Conclusiones
## 6. Bibliografía 

- Köhler, J. [jkohlerc]. (17 de enero de 2010). Problema del vendedor viajero [Archivo de video]. Recuperado de https://www.youtube.com/watch?v=EutHYzkSo5Y&t=5s 

- Rihawi, I. (6 de diciembre de 2009). Búsqueda no informada: Algoritmo de Coste Uniforme. Recuperado de https://poiritem.wordpress.com/2009/12/06/6-5-1-busqueda-no-informada-algoritmo-de-coste-uniforme/ 

- Fernando, P. (18 de diciembre de 2017). Algoritmo para búsqueda con coste uniforme. Recuperado de https://www.revolucionia.com/2017/12/Algoritmo_para_busqueda_con_coste_uniforme.html
