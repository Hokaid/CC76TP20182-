
# Informe 

## 1. Introducción

El problema que se va intentar resolver en este proyecto es El problema del vendedor viajero. Este problema consiste en, dado un conjunto de ciudades y las distancias entre ellas, encontrar el camino mas corto que recorra cada ciudad exactamente una sola vez y que vuelva a la ciudad de partida. Este es un problema de tipo no polinomial dentro de la optimización combinatoria, muy utilizado en la investigación de operaciones y en la ciencia de la computación. La motivación para el desarrollo de este proyecto radica en poner en practica las estrategias de solución vistas en clase tales como fuerza bruta, backtracking, bfs o dfs. Además, tambien se cuenta con la motivación de intentar solucionar un problema dificil e importante, cuya solución no solo podria traer muchos beneficios al mundo de la informatica, sino tambien a la sociedad en general.

## 2. Objetivos del Proyecto

A. Se busca desarrollar la capacidad de analizar datos representados bajo diversas formas tales como tablas y graficos.

B. Mejorar la habilidad para solucionar problemas cuanticos mediante la utilización de números y terminos matematicos.

C. Desarrollar la destreza de utilizar tecnicas y herramientas modernas acorde con el problema planteado. 

D. Aplicar las tecnicas de solución vistas a lo largo del curso en el desarrollo de los algoritmos que resolveran el problema planteado.

E. Elaborar un marco teórico explicando detalladamente cada una de las estrategias usadas para dar solución al problema planteado. 

F. Realizar un análisis de la complejidad algorítmica para cada una de las estrategias utilizadas en la solución del problema dado.

G. Encontrar un porcentaje de la solución del problema planteado (Problema del vendedor viajero).

H. Generar una adecuada visualización de resultados de acuerdo a las posibles soluciones encontradas para el problema dado.

## 3. Marco Teórico

A continuación, se va a desarrollar el marco teórico de cada una de las estrategias aplicadas para las solución del problema.

###      3.1. Marco Teórico del Algoritmo de Fuerza Bruta

El algoritmo planteado se basa en encontrar la mayor cantidad de caminos posibles (posibles soluciones para el problema), y apartir de una comparación de todos estos, determinar el camino mas corto encontrado. Para este algoritmo, se va a representar el mapa de centros poblados con un grafo. Para este caso particular, cada nodo vendria a representar un centro poblado, y las aristas serian los caminos entre los respectivos centros poblados con la distancia entre estos. La estructura usada para representar este grafo corresponde a una lista de adyacencia de pares ordenados. La posición de la lista en la que se encuentre el par ordenado coincide con el codigo del centro poblado de origen, la primera componente del par ordenado hace referencia a la longitud del camino, mientras que la segunda componente representa el nodo (centro poblado) de destino. A continuación, se pasara a explicar paso a paso cada parte de la estrategia utilizada.

- Paso 1: Consiste en apartir de un nodo de origen buscar, de todas las posibles aristas que lo conectan con otros nodos, las dos aristas que cuenten con menor peso. Llegados a este punto, se pasara a mostrar una imagen con el codigo correspondiente a esta parte:

###      3.2. Marco Teórico del Algoritmo de Backtracking
## 4. Analisis de Complejidad Algoritmica
###      4.1. Analisis del Algoritmo de Fuerza Bruta
###      4.2. Analisis del Algoritmo de Backtracking
## 5. Conclusiones
