### TRABAJO PRACTICO N°6 : CSP

#### 1)Describir en detalle una formulación CSP para el Sudoku.

###### Cada celda del tablero es una variable
{x11  ,x12,x13,x14,x15,x16 ,x17, x18, x19, … , x99}   

###### El dominio de cada una de las celdas es {1,2,3,4,5,6,7,8,9}

###### Reestricciones:

Todos los pares de variables en cada fila deben ser distintos

 ≠{x11  ,x12,x13,x14,x15,x16 ,x17, x18, x19} ,≠ {x21  ,x22,x23,x24,x25,x26 ,x27, x28, x29} ,..., ≠{x91  ,x92,x93,x94,x95,x96 ,x97, x98, x99}

Todos los pares de variable en cada columna deben ser distintos
≠{x11  ,x21,x31,x41,x51,x61 ,x71, x81, x91} ,≠ {x12  ,x22,x32,x42,x52,x62 ,x72, x82, x92} ,..., ≠{x19  ,x29,x39,x49,x59,x69 ,x79, x89, x99}

#### 2) Utilizar el algoritmo AC-3 para demostrar que la arco consistencia puede detectar la inconsistencia de la asignación parcial {WA=red, V=blue} para el problema del colorar el mapa de Australia (Figura 5.1 AIMA 2da edición ).

  El algoritmo recibe un PSR BINARIO con las variables (WA,SA,NT,Q,NSW,V)
	Tiene una variable local que es una pila con todos los posibles arcos 
	Pila = { (WA-SA) , (WA-NT) , (SA-NT),(SA-V),(SA-Q),(SA-NSW)... etc}
	
	En el primer bucle while -> recorre la pila :
		Dentro del bucle extrae uno por uno los arcos , en este caso nuestro primer arco 	
		Seria (WA-SA) . 
		Habiendo asignado a WA = R es decir el dominio de WA = {R} la unica inconsistencia que encontramos es si SA fuera de color rojo tambien por lo tanto asumimos que el dominio de SA = { V, A} y elimina la inconsistencia , luego agrega los valores Vecinos de WA
		Ahora extraemos el próximo arco (WA-NT) 
		Habiendo asignado a WA = R es decir el dominio de WA = {R} la unica inconsistencia que encontramos es si NT fuera de color rojo tambien por lo tanto asumimos que el dominio de NT = { V, A}  elimina la inconsistencia 
		Ahora extraemos el proximo arco (SA-NT)
		Sabiendo que dominio de es SA = { V,A } encontramos que si SA = {V} entonces NT = { A} y viceversa , de no ser asi se presentan inconsistencias por lo tanto elimina inconsistencia y continua analizando arcos . 
Cuando analiza arco (SA-V) si V = A , se detecta inconsistencia ya que uno de los posibles valores de  SA es A . De esta forma el algoritmo identifica esta inconsistencia.

#### 3) Cuál es la complejidad en el peor caso cuando se ejecuta AC-3 en un árbol estructurado CSP. (i.e. Cuando el grafo de restricciones forma un árbol: cualquiera dos variables están relacionadas por a lo sumo un camino).

La complejidad de la comprobación de consistencia de arco puede analizarse como sigue: un PSR binario tiene a lo más O(n2 ) arcos; cada arco (Xk, Xi ) puede insertarse en la agenda sólo d veces, porque Xi tiene a lo más d valores para suprimir; la comprobación de la consistencia de un arco puede hacerse en O(d2 ) veces; entonces el tiempo total, en el caso peor, es O(n2 d3 ).


#### 4) AC-3 coloca de nuevo en la cola todo arco ( Xk, Xi) cuando cualquier valor es removido del dominio de Xi incluso si cada valor de Xk es consistente con los valores restantes de Xi. Si por cada arco ( Xk,Xi) se lleva cuenta del número de valores que quedan de Xi que sean consistentes con Xk . Explicar como actualizar ese número de manera eficiente y demostrar que la arco consistencia puede lograrse en un tiempo total O(n2d2 )

#### 5) Demostrar la correctitud del algoritmo CSP para  árboles estructurados (sección 5.4, p. 172 AIMA 2da edición). Para ello, demostrar: 
#### A)Que para un CSP cuyo grafo de restricciones es un árbol, 2-consistencia (consistencia de arco) implica n-consistencia (siendo n número total de variables)
#### B)Argumentar por qué lo demostrado en a es suficiente. 

#### 6) Implementar una solución al problema de las n-reinas utilizando una formulación CSP (ver carpeta code)

##### a)Implementar una solución utilizando backtracking. 
##### b)Implementar una solución utilizando encadenamiento hacia adelante.
##### c)En cada variante, calcular los tiempos de ejecución para los casos de 4, 8, 10, 12 y 15 reinas.

######  Backtraking cronologico :

######  4-Reinas: 738.058ms
######  8-Reinas: 551.983ms
######  10-Reinas: 617.011ms
######  12-Reinas: 776.045ms
######  15-Reinas:
          
##### d)En cada variante, calcular la cantidad de estados recorridos antes de llegar a la solución para los casos de 4, 8, 10, 12 y 15 reinas.
##### e)Realizar un gráfico de cajas para los puntos c y d.


