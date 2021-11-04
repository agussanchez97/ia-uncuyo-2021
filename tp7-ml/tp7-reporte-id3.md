## Resultado sobre dataset TENNIS

![image](https://user-images.githubusercontent.com/82063987/140404578-e929c6a6-424f-45bc-b427-b656a90f7ee3.png)

## Investigar sobre las estrategias de los árboles de decisión para datos de tipo real y elaborar un breve resumen.

Árboles de regresión es cuando el resultado predicho se puede considerar un número real (por ejemplo, el precio de una casa, o el número de días de estancia de un paciente en un hospital).
Los árboles de regresión son el subtipo de árboles de predicción que se aplica cuando la variable respuesta es continua. En términos generales, en el entrenamiento de un árbol de regresión, las observaciones se van distribuyendo por bifurcaciones (nodos) generando la estructura del árbol hasta alcanzar un nodo terminal. Cuando se quiere predecir una nueva observación, se recorre el árbol acorde al valor de sus predictores hasta alcanzar uno de los nodos terminales. La predicción del árbol es la media de la variable respuesta de las observaciones de entrenamiento que están en ese mismo nodo terminal.

##### El proceso de entrenamiento de un árbol de predicción (regresión o clasificación) se divide en dos etapas:

-División sucesiva del espacio de los predictores generando regiones no solapantes (nodos terminales)  R1 ,  R2 ,  R3 , ...,  Rj . Aunque, desde el punto de vista teórico las regiones podrían tener cualquier forma, si se limitan a regiones rectangulares (de múltiples dimensiones), se simplifica en gran medida el proceso de construcción y se facilita la interpretación.

-Predicción de la variable respuesta en cada región.

A pesar de la sencillez con la que se puede resumir el proceso de construcción de un árbol, es necesario establecer una metodología que permita crear las regiones  R1 ,  R2 ,  R3 , ...,  Rj , o lo que es equivalente, decidir donde se introducen las divisiones: en que predictores y en que valores de los mismos. Es en este punto donde se diferencian lo algoritmos de árboles de regresión y clasificación.
