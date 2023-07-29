# Trabajo Final Inteligencia Artificial I 

## TITULO : ALGORITMOS DE CLASIFICACIÓN PARA INFORMACIÓN GENETICA.

##### Codigo: ACLASIGEN

###### Alumnas: Sanchez Lanza Agustina // Lucia Cairo
###### Legajo: 11549 // Legajo: 13030

# Introducción 

En el presente informe se aborda un problema de inteligencia artificial, específicamente en el campo del aprendizaje automático y ciencia de datos. Nuestro objetivo es probar dos algoritmos (GLMNET y Centroide más cercano) y crear un modelo de clasificación, para que dado un dataset y de acuerdo con las características genéticas que tenga el mismo, se pueda predecir el tipo de cáncer que puede llegar a desarrollar un individuo.

Los inconvenientes se encuentran en la dificultad de clasificar los datos correctamente, dado que los dataset genéticos se caracterizan por ser escasos de observaciones, lo que limita la capacidad de los modelos para generalizar. La falta de información suficiente puede afectar la precisión y la capacidad predictiva de los algoritmos y generar, por ejemplo, falsos positivos o falsos negativos.

Para abordar el problema, utilizamos dos algoritmos de aprendizaje supervisado que como mencionamos anteriormente son "Centroide más cercano", que es un modelo de clasificación que asigna etiquetas de clase en función de la distancia al centroide más cercano en el conjunto de entrenamiento; y el algoritmo "Glmnet", que es un método de regresión lineal o logística que penaliza variables menos relevantes durante el entrenamiento, lo cual nos permite encontrar el conjunto de genes más importantes a la hora de clasificar.

La aplicación de técnicas de inteligencia artificial se considera una solución viable ya que el problema puede ser abordado con machine learning, una rama de la inteligencia artificial que cuenta con una amplia variedad de algoritmos adecuados para el entrenamiento de conjuntos de datos. Al emplear estas técnicas, esperamos obtener resultados precisos y relevantes que nos permitan distinguir similitudes y diferencias entre los algoritmos evaluados y encontrar el mejor modelo ajustable para nuestro problema.

A lo largo de este informe iremos explicando un marco teórico de cada uno de los conceptos mencionados y a continuación el experimento práctico con las métricas de desempeño obtenidas y las conclusiones resultantes, a fin de que al final podamos realizar una comparativa de ambos modelos, teniendo en cuenta los pros y los contras de cada uno.

# Marco teórico
El aprendizaje automático es un campo de la inteligencia artificial que se ocupa de desarrollar algoritmos y modelos que puedan aprender patrones y realizar predicciones o toma de decisiones a partir de datos. La clasificación es una tarea fundamental en el aprendizaje automático, donde se asigna una etiqueta o categoría a un objeto o instancia en función de sus características. 

Como se menciona anteriormente, abordamos un problema de clasificación en el campo del aprendizaje automático, donde el objetivo es predecir el tipo de cáncer que un individuo puede desarrollar utilizando información genética. Se proponen dos algoritmos de aprendizaje supervisado: "Centroide más cercano" y "GLMNET".

## Centroide más cercano

El clasificador de centroide más cercano (Nearest Centroid) es uno de los clasificadores más infravalorados y utilizado en el aprendizaje automático. Sin embargo, es bastante potente y muy eficiente para ciertas tareas de clasificación de Machine Learning. El clasificador Nearest Centroid es algo similar al clasificador K-Nearest Neighbors, la diferencia principal es que centroide más cercano se concentra en encontrar el centro de cada clase/etiqueta y clasificar nuevos puntos basándose en la distancia al centroide, mientras que KNN clasifica los puntos basándose en la mayoría de las "K" instancias más cercanas en el espacio de características sin un paso explícito de entrenamiento. 

El clasificador de centroide más cercano se puede explicar simplemente en 3 pasos: 
 
1. Calcular el centroide para cada clase objetivo con el conjunto de entrenamiento.
2. Después del entrenamiento, dado cualquier punto, llámese 'X'. Se calculan las distancias entre el punto X y el centroide de cada clase, calculado en el punto 1.
3. De todas las distancias calculadas, se selecciona la distancia mínima. La clase del centroide al que la distancia del punto dado es mínima, es la que se le asigna a la observación.

A continuación dejamos un gráfico bidimensional a modo representativo del funcionamiento y teniendo en cuenta que el mismo solo sirve para describir un dataset que contenga 2 variables.

![image](https://github.com/agussanchez97/ia-uncuyo-2021/assets/88351747/d67a771e-7ddb-4881-9d10-72035659cbf5)

Imagen 1: bidimensional explicativo de Centroide más cercano.

Como podemos visualizar en la imagen 1, tenemos 3 centroides de 2 puntos (x,y) que representarian las variables de un dataset y una observación. Luego calculamos las distancias de la observación a los centroides (d1,d2,d3) y gráficamente podemos ver que d1 es la menor distancia por lo tanto esa observación será clasificada según la clase que corresponda a C1.

El algoritmo del centroide más cercano puede ser computacionalmente costoso para grandes conjuntos de datos, ya que implica calcular las distancias entre cada punto de datos y todos los centroides en cada iteración. Sin embargo, con implementaciones eficientes y técnicas de reducción de dimensionalidad, se puede aplicar a conjuntos de datos más grandes. A continuación mencionaremos algunas ventajas y desventajas del mismo.

### Hiperparametros

Los hiperparametros controlan aspectos fundamentales de los algoritmos y la arquitectura del modelo, y pueden tener un impacto significativo en el rendimiento y la generalización del modelo.Son aquellos parámetros del modelo que no se aprenden directamente durante el entrenamiento, sino que deben ser configurados antes del proceso de entrenamiento.

A pesar de que el centroide más cercano, no posee muchos hiperparametros que se pueden modificar para mejorar el modelo en sí, podemos destacar algunos puntos que sí pueden llegar a ser significativos en el rendimiento del mismo, como lo son:

**Distancia**

Existen varias fórmulas para calcular la distancia entre dos puntos en diferentes espacios (como el espacio unidimensional, bidimensional, tridimensional, etc.) o para diferentes tipos de datos (como datos numéricos, datos categóricos, datos textuales, etc.). A continuación, se presentan algunas de las fórmulas de distancia más comunes.

* Distancia Euclidiana (para espacios de dimensión n): La distancia euclidiana es la distancia "recta" entre dos puntos en un espacio euclidiano y se define como la longitud del segmento de línea que conecta los dos puntos.
Para dos puntos en un espacio de dimensión n: *Distancia = sqrt((x2 - x1)^2 + (y2 - y1)^2 + ... + (zn - z1)^2)*

* Distancia Manhattan: La distancia de Manhattan mide la distancia "rectangular" entre dos puntos en un espacio euclidiano y se define como la suma de las diferencias absolutas de las coordenadas entre los dos puntos.
Para dos puntos en un espacio de dimensión n: *Distancia = |x2 - x1| + |y2 - y1| + ... + |zn - z1|*

* Distancia Minkowski: La distancia Minkowski es una generalización de la distancia euclidiana y la distancia de Manhattan, y está definida como: Para dos puntos en un espacio de dimensión n: *Distancia = (|x2 - x1|^p + |y2 - y1|^p + ... + |zn - z1|^p)^(1/p)* Cuando p = 1, es equivalente a la distancia de Manhattan, y cuando p = 2, es equivalente a la distancia euclidiana.

**Cálculo del Centroide**

El método más común es el cálculo de la media de las instancias pertenecientes a la clase, pero también se puede realizar el cálculo de la mediana.
* Media: también conocida como promedio, se calcula sumando todos los valores en un conjunto de datos y dividiendo el resultado por el número de observaciones: *media = (x1 + x2 + x3 + ... + xn) / n* . Donde x1, x2, ..., xn son los valores individuales en el conjunto de datos, y n es el número total de observaciones.

* Mediana: es el valor central en un conjunto de datos ordenados. Se debe ordenar los valores en orden ascendente o descendente. Luego, si el número total de observaciones es impar, la mediana es el valor que se encuentra en el centro de la lista ordenada. Si el número total de observaciones es par, la mediana es el promedio de los dos valores centrales.

**Número de centroides** 

Por lo general el número de centroides idealmente coincide con la cantidad de clases/etiquetas que hay.

### Ventajas del algoritmo centroide

* Fácil implementación: El algoritmo del centroide más cercano es relativamente sencillo de implementar y entender. No requiere de configuraciones complicadas ni de parámetros sensibles.
* Eficiente computacionalmente: El algoritmo es computacionalmente eficiente, ya que su principal operación es el cálculo de distancias entre puntos y centroides.
* Interpretabilidad: El resultado del algoritmo del centroide más cercano es fácil de interpretar. Los centroides representan los puntos centrales de cada clase y se puede utilizar la distancia al centroide más cercano como medida de similitud.

### Desventajas del algoritmo centroide

* Sensible a datos atípicos: El algoritmo del centroide más cercano puede ser sensible a datos atípicos o valores extremos en el conjunto de datos. Un solo valor atípico puede afectar significativamente la posición del centroide y, por lo tanto, la clasificación de nuevas instancias.
* Sensible a distribuciones desbalanceadas: Si el número de muestras en cada clase es muy desbalanceado, el algoritmo puede verse sesgado hacia las clases con mayor número de muestras. Esto puede resultar en una clasificación incorrecta de las clases minoritarias.
* Suposición de igual varianza: El algoritmo del centroide más cercano asume que las características de cada clase tienen una varianza similar. Si las varianzas difieren significativamente entre las clases, el algoritmo puede no funcionar de manera óptima.
* No considera interacciones entre características: El algoritmo del centroide más cercano trata cada característica de forma independiente y no considera las posibles interacciones o relaciones entre ellas. Esto puede ser problemático en conjuntos de datos donde las características están correlacionadas.

### Precisión del Centroide mas Cercano

El algoritmo del centroide más cercano, al igual que cualquier otro algoritmo de clasificación, puede no acertar al 100% debido a varias razones:
* Solapamiento de clases: si hay instancias de clases muy cercanas entre sí, el algoritmo puede tener dificultades para asignar correctamente las instancias a sus respectivas clases. En estos casos, no hay una separación clara entre las clases y es difícil lograr una clasificación perfecta.
* Datos ruidosos o incorrectamente etiquetados: al tener instancias mal etiquetadas con su clase, el algoritmo puede cometer errores de clasificación. Estos errores pueden ser inherentes a los datos y no pueden ser corregidos por el algoritmo.
* Falta de representatividad de los centroides: si los centroides no son representativos de sus respectivas clases o si no capturan adecuadamente la variabilidad de las instancias, es posible que el algoritmo no logre una clasificación precisa.
* Limitaciones de la métrica de distancia: la elección de la métrica de distancia también puede influir en el rendimiento del algoritmo. Hya que calcularla dependiendo de la estructura y naturaleza de los datos.
* Falta de características relevantes: si los datos carecen de características discriminativas o si las características disponibles no son suficientes para separar adecuadamente las clases, el algoritmo puede tener dificultades para realizar una clasificación precisa.

## Algoritmo GLMNET

GLMNET es un algoritmo de aprendizaje supervisado utilizado en estadística y ciencias de datos para resolver problemas de regresión y clasificación. Fue propuesto por Friedman, Hastie, y Tibshirani en 2010. 
Para comprender el funcionamiento del algoritmo, es fundamental entender la regresión lineal.

### Regresión lineal

La regresión lineal es un método que modela la relación lineal entre una variable de salida y una o más variables predictoras. Es un método que nos permite encontrar una línea recta que mejor se ajuste a un conjunto de datos. 
Imagina que tienes una serie de puntos dispersos en un gráfico, y quieres encontrar una línea que pase cerca de esos puntos, tal como se muestra en la Figura N. En la regresión lineal, buscamos esa línea recta que se acerque lo más posible a los datos. Esta línea se representa mediante una ecuación de la forma: *Y = mX + b*. Donde:

* Y es la variable que queremos predecir o explicar.
* X es la variable independiente que utilizamos para predecir Y.
* m es la pendiente de la línea, que representa cómo Y cambia en relación con X.
* b es el punto de corte con el eje Y, que indica el valor de Y cuando X es igual a cero.

El objetivo de la regresión lineal es encontrar los valores de m y b que minimicen la distancia entre la línea y los puntos de datos. 
Una vez obtenido la línea de regresión, podemos utilizarla para hacer predicciones. Dado un valor de X, podemos calcular el correspondiente valor de Y utilizando la ecuación de la línea.

![image](https://github.com/agussanchez97/ia-uncuyo-2021/assets/88351747/64c1a40e-68fb-49f0-941b-8fe5e304717c)

<small>Imagen 2: representacion de la regresion lineal. Tomado del libro "An Introduction to Statistical Learning with application in R"( ISLR ). página 62.</small>

El algoritmo GLMNET, es una implementación de regresión lineal. Permite entrenar un modelo de regresión lineal penalizando las variables que considera menos importantes, lo que ayuda a seleccionar las características genéticas más relevantes para la clasificación. Para esto, ell algoritmo combina la regresión lineal generalizada con la regularización Elastic Net. 

### Regresión lineal generalizada (GLM) 

El GLM es una generalización de la regresión lineal que permite modelar variables de respuesta que no necesariamente siguen una distribución normal. El modelo incluye una función de enlace que relaciona la media de la variable respuesta con una combinación lineal de las variables predictoras.

### Regularización Elastic Net 

La regularización es una técnica que se aplica para evitar el sobreajuste (overfitting) en modelos de aprendizaje automático. El sobreajuste sucede cuando un modelo se ajusta demasiado a los datos de entrenamiento y captura ruido o variaciones aleatorias en lugar de patrones genuinos. 

La regularización consiste en agregar términos de penalización a la función objetivo del modelo, lo que limita el tamaño de los coeficientes de las variables predictora, con el propósito de restringir la complejidad y limitar la magnitud de los coeficientes de las variables predictoras.

La regularización Elastic Net combina las penalizaciones LASSO y Ridge, controladas por dos parámetros de regularización (lambda y alpha). Esto permite mantener la estabilidad del modelo y realizar selección automática de variables, evitando el sobreajuste y mejorando la capacidad de generalización.

**Regularización L2 (Ridge Regression):** 

La regresión ridge es una técnica que se utiliza para ajustar modelos de regresión lineal cuando hay muchos predictores o cuando estos están altamente correlacionados entre sí. En lugar de buscar el mejor subconjunto de predictores, ajusta todos los predictores y reduce los coeficientes hacia cero, pero sin eliminarlos por completo.
Esto se logra al agregar una penalización a la función objetivo del modelo, que hace que los coeficientes sean más pequeños a medida que aumenta el valor de un parámetro llamado λ. Al reducir los coeficientes, la regresión ridge disminuye la varianza de las estimaciones, lo que significa que los resultados son más estables y menos sensibles a pequeñas variaciones en los datos de entrada.
A diferencia de otros métodos que seleccionan solo un subconjunto de variables, la regresión ridge incluye todas las variables predictoras en el modelo final. Esto puede dificultar la interpretación cuando hay muchas variables.

**Regularización L1 (LASSO):** 

Agrega la suma de los valores absolutos de los coeficientes a la función. Esto puede llevar a algunos coeficientes exactamente iguales a cero, lo que tiene un efecto de selección de características y puede llevar a un modelo más simple con menos variables predictoras.

En resumen, el lasso y la regresión ridge reducen los coeficientes hacia cero, pero el lasso puede establecer algunos coeficientes en cero, lo que hace el modelo más fácil de interpretar y selecciona solo un subconjunto de variables importantes. La regresión ridge siempre incluye todas las variables, aunque sus coeficientes serán más pequeños a medida que se aumente el parámetro de ajuste.

### Ventajas del algoritmo GLMNET 

* Permite la selección automática de características relevantes al utilizar la regularización L1.
* Es adecuado para conjuntos de datos con un gran número de características.
* Proporciona una solución eficiente utilizando métodos de optimización.

### Desventajas del algoritmo GLMNET

* La interpretación de los coeficientes del modelo puede ser más compleja debido a la regularización.
* La selección de los parámetros de regularización (lambda y alpha) puede requerir técnicas de validación cruzada para encontrar los mejores valores.
* No es adecuado para problemas no lineales, ya que se basa en modelos lineales generalizados.

### Precisión de GLMNET

El algoritmo GLMNET puede no acertar al 100% debido a varias razones:
* Datos ruidosos o incorrectamente etiquetados: al tener instancias mal etiquetadas con su clase, el algoritmo puede cometer errores de clasificación. Estos errores pueden ser inherentes a los datos y no pueden ser corregidos por el algoritmo.
* Complejidad del problema: hay factores desconocidos o interacciones entre variables que no se pueden capturar con un modelo lineal o incluso con una combinación de regularizaciones.
* Tamaño del conjunto de datos: si es pequeño el modelo puede no generalizar adecuadamente a nuevos datos y, por lo tanto, no alcanzar un rendimiento del 100%.
* Subajuste o sobreajuste: si el modelo es muy simple, no podrá capturar patrones complejos en los datos. Por otro lado, si es demasiado complejo, se ajustará demasiado a los datos de entrenamiento, lo que resultará en un mal rendimiento en datos no vistos.
* Características no representativas: si las variables utilizadas no son representativas, el modelo no podrá realizar predicciones precisas.

### Justificación

El uso de GLMNET es adecuado para el problema de clasificación de cáncer basado en características genéticas debido a su capacidad para lidiar con datasets escasos de observaciones y variables predictoras. La combinación de regularización L1 y L2 ayuda a reducir la dimensionalidad del modelo y seleccionar las características más relevantes, lo que es crucial cuando se trabaja con datos genéticos que pueden contener una gran cantidad de características.

En resumen, GLMNET es un algoritmo importante en el campo de la regresión y clasificación que combina la regresión lineal generalizada con la regularización Elastic Net. Esto permite obtener modelos más estables, con selección automática de variables y mejor capacidad de generalización en comparación con la regresión lineal estándar. Su aplicabilidad se extiende a diversas áreas de ciencia de datos y estadística donde se manejan conjuntos de datos complejos con múltiples variables predictoras.

# Diseño Experimental

## Dataset

Para comenzar con el desarrollo, cabe destacar que el lenguaje de programación principal que utilizamos es R, ya que consideramos que es muy utilizado en el campo de la inteligencia artificial y fue provisto por la cátedra. 

Para adentrarnos en los temas, comenzaremos explicando el dataset utilizado a lo largo del experimento, el mismo se llama Khan y fue tomado del libro "An Introduction to Statistical Learning with application in R"( ISLR ). Este libro brinda una introducción a los conceptos fundamentales de aprendizaje estadístico y su implementación en R.

El conjunto de datos Khan, está disponible en el paquete ISLR de R, el cual contiene varios conjuntos de datos utilizados en el libro. Para poder utilizar el mismo, fue necesario importar la librería en nuestro modelo.

Como primer paso, consideramos que entender los datos y realizar un correcto preprocesamiento de los mismos es fundamental para poder tratarlos y encontrar un patrón de comportamiento adecuado. Por lo tanto, es necesario explicar el conjunto de datos, dado que esto nos ayudará a entender más adelante los resultados obtenidos. 

Entonces, Khan es un dataset pequeño, en cuanto a número de observaciones, ya que solo cuenta con 63, sin embargo, tiene 2308 variables, lo cual es un número muy grande de características para analizar, como mencionamos anteriormente esto es una característica muy común en información genética. Además, el dataset cuenta con un vector de 63 etiquetas que corresponden a los 4 tipos de cánceres. 

En cuanto al preprocesamiento, estudiamos uno de los puntos críticos que es el balanceo de clases, para esto analizamos la proporción de las mismas. Por otra parte, buscamos si el dataset tenía valores anómalos o extremos que nos pudieran generar algún problema a la hora de predecir. A continuación, pasamos a detallar ambos procedimientos y los resultados obtenidos.

### Balanceo de clases
   
Para determinar si las clases del dataset Khan están balanceadas, analizamos las proporciones de observaciones por clase. En este caso, las proporciones son las siguientes:

* Clase 1: 0.1269841
* Clase 2: 0.3650794
* Clase 3: 0.1904762
* Clase 4: 0.3174603

![image](https://github.com/agussanchez97/ia-uncuyo-2021/assets/88351747/a1703134-5f95-40e6-b407-e256379c8b6b)

Imagen 3: balance de clases del dataset Khan

Pudimos notar que la Clase 2 tiene la proporción más alta (0.3650794), mientras que la Clase 1 tiene la proporción más baja (0.1269841). Esto sugiere cierto desbalance en las clases.

### Valores anómalos o extremos.

Para realizar este procedimiento decidimos utilizar el método de Mahalanobis, donde el objetivo en si, es calcular la distancia de Mahalanobis de cada uno de los puntos e ir clasificando, primeramente explicaremos el método de manera teórica y luego la implementación. 

**Método de Mahalanobis**

La distancia de Mahalanobis es una medida de la distancia entre un punto y un conjunto de puntos, teniendo en cuenta la estructura de covarianza de los datos. Esta distancia se utiliza para evaluar la similitud o la discrepancia entre un punto y una distribución multivariada.

La misma utiliza la matriz de covarianza para tener en cuenta las correlaciones entre las variables y la varianza de cada variable en un conjunto de datos. Esto permite tener en cuenta la estructura de covarianza de los datos al calcular la distancia.

Se define como: *D(x) = √((x - μ)' Σ^(-1) (x - μ))*

Donde:
* x es el punto para el cual se calcula la distancia.
* μ es el vector de medias de las variables en el conjunto de datos.
* Σ es la matriz de covarianza.

![image](https://github.com/agussanchez97/ia-uncuyo-2021/assets/88351747/f2519e8b-ef61-4bbe-b1a7-d553aa243181)

Imagen 4: porción de codigo tomado de la implementación propuesta

En la imagen 4 línea 20 podemos observar como se  calcula la matriz de covarianza del conjunto de entrenamiento usando la función cov. La función t se utiliza para transponer la matriz xtrain y asegurarse de que las variables estén en las columnas y las observaciones en las filas. Luego en la línea 24 se calcula la media de cada variable utilizando la función colMeans. De nuevo, se transpone la matriz xtrain con la función t para que las variables estén en las columnas.

Utilizamos la función Mahalanobis para calcular la distancia de Mahalanobis para cada observación en el conjunto de entrenamiento esto se visualiza en la línea 27 Se proporcionan los siguientes argumentos:

t(xtrain): La matriz de datos transpuesta.
center = means: El vector de medias calculado anteriormente.
cov = cov_matrix: La matriz de covarianza calculada anteriormente.

Establecemos un umbral para identificar valores atípicos. En este caso, utilizamos el cuantil 0.95 de la distribución chi-cuadrado con grados de libertad igual al número de variables en el conjunto de entrenamiento. Esto se realiza con la función qchisq.

Finalmente, se utiliza la función which para identificar los índices de las observaciones que tienen una distancia de Mahalanobis mayor que el umbral establecido. Estos índices se almacenan en la variable outliers.

Concluimos imprimiendo los datos y los resultados obtenidos fueron que no hay valores anómalos, ni extremos de acuerdo al umbral fijado.

![image](https://github.com/agussanchez97/ia-uncuyo-2021/assets/88351747/2060ac2c-2f6c-48b5-aa3d-aea70bfdcdab)

Imagen 5: resultado de la ejecución del código imagen 1

## Centroide mas cercano

Para comenzar a generar nuestro modelo, fue necesario como paso principal dividir el conjunto de datos en entrenamiento y prueba (proporción de 70/30). El 30% de los datos lo dejamos de lado y no se tocó, hasta que llegó el momento de probar el modelo. Por otro lado, el 70% de los datos lo utilizamos para entrenar el modelo y realizar una búsqueda de hiperparámetros para ajustarlo.

![image](https://github.com/agussanchez97/ia-uncuyo-2021/assets/88351747/7daaf1c9-e17c-4350-8972-3cec66f12a76)

Imagen 6. Diseño experimental estándar para evaluar el rendimiento de un modelo de aprendizaje automático tomado de Machine Learning Experimental Design 101
by Harpo MAxx

Debido a que no existe ninguna librería que tenga el algoritmo del centroide más cercano implementado y se pueda utilizar de manera automática, fue necesario desarrollar nuestro propio algoritmo en base a las definiciones mencionadas en la teoría.

Para esto luego de realizar la división del dataset, trabajamos con el conjunto de prueba, como podemos visualizar en la imagen 5, en la línea 15 obtenemos las clases del vector ytrain que contiene 4 etiquetas que corresponden a los 4 tipos de cáncer. Luego en la línea 20 definimos el vector centroides que guardara los 4 centroides que se calculan en el bucle for de la línea 23, en esta primera instancia fue calculado con la fórmula de la media o promedio de las variables. En la línea 37 comienza el bucle anidado para calcular la matriz distancias con el conjunto de pruebas, para finalmente asignarle una clase de acuerdo a la distancia al centroide más cercano.

![image](https://github.com/agussanchez97/ia-uncuyo-2021/assets/88351747/f1757aae-cdee-47cd-8746-d4057818ce04)

Imagen 7: porción de código del algoritmo del centroide más cercano sin mejoras

Por último se calculan las predicciones, evaluando la clase calculada con el vector ytest que es la clase real. Esto se puede visualizar en la linea 44, la variable clases_predichas, con la que luego en la linea 50 de la imagen 6, se calcula la matriz de confusión.

![image](https://github.com/agussanchez97/ia-uncuyo-2021/assets/88351747/df1e8416-5702-47c1-9936-ebe6983082fe)

Imagen 8: porción de código del calculo de metricas

De este primer experimento obtuvimos resultados muy satisfactorios que se pueden visualizar en la Tabla 1, teniendo en cuenta que al algoritmo no se le realizó ningún ajuste de hiperparametros y aun asi se obtuvo una exactitud del 70%, lo que posiciona al modelo en un lugar mucho mejor que la resolución por algoritmos como random o fuerza bruta.

Tenemos que tener en cuenta, que es un dataset pequeño y muy desbalanceado por lo tanto, depende como se dividan los datos y que cantidad de observaciones del conjunto de prueba pertenecen a las clases desbalanceadas, eso nos da una idea del rendimiento del mismo, ya que por razones obvias, el modelo va a tener problemas para predecir clases con pocas observaciones en el entrenamiento.

Realizamos anotaciones de todas las métricas obtenidas, para luego poder sacar conclusiones sobre las mejoras del algoritmo e incluso realizar una comparativa con el algoritmo GLMNET, a continuación explicamos cada una de las métricas.

**Matriz de confusión**

|            | Re | fe | ren | cia |
|------------|---|---|---|---|
| Predicción | 1 | 2 | 3 | 4 |
| 1          | 3 | 0 | 0 | 0 |
| 2          | 0 | 4 | 1 | 0 |
| 3          | 0 | 0 | 2 | 0 |
| 4          | 0 | 2 | 3 | 5 |

La matriz de confusión nos muestra lo siguiente:
* La “Clase 1” tiene 3 instancias que fueron clasificadas correctamente
* La “Clase 2” tiene 4 instancias que fueron clasificadas correctamente
* Hubo 1 falso positivo  “Clase 2” (fue clasificada erróneamente como clase "4").
* La “Clase 3” tiene 2 instancias que fueron clasificadas correctamente
* La “Clase 4” tiene 5 instancias que fueron clasificadas correctamente.
* Hubo 5 falsos negativos en la “Clase 4” (fueron clasificadas erróneamente como clase "2" y “3”).

**Accuracy (Exactitud)**

Representa la proporción de predicciones correctas sobre el total de predicciones. En este caso, el valor de Accuracy es 0.7, lo que significa que el 70% de las predicciones fueron correctas. 

**Estadísticas generales**

|            | Clase 3 | Clase 2 | Clase 4 | Clase 1 |
|------------|---|---|---|---|
| Sensitivy | 0.3333 | 0.6667 | 1.0000 | 1.0000 |
| Specificity | 1.0000 | 0.9286 | 0.6667 | 1.0000 | 
| Pos Pred Value | 1.0000 | 0.8000 | 0.5000 | 1.0000 |
| Neg Pred Value | 0.7778 | 0.8667 | 1.0000 | 1.0000 |
| Prevalence | 0.3000 | 0.3000 | 0.2500 | 0.1500 |
| Detection Rate | 0.1000 | 0.2000 | 0.2500 | 0.1500 |
| Detection Prevalence | 0.1000 | 0.2500 | 0.5000 | 0.1500 |
| Balanced Accuracy | 0.6667 | 0.7976 | 0.8333 | 0.1000 |

Sensitivity (Sensibilidad): conocida como tasa de verdaderos positivos, es la proporción de instancias positivas (verdaderos) que fueron correctamente identificadas por el modelo para la clase en cuestión. 

Specificity (Especificidad): conocida como tasa de verdaderos negativos, es la proporción de instancias negativas que fueron correctamente identificadas por el modelo para la clase en cuestión. Un valor de especificidad de 1.0000 significa que el modelo identificó correctamente todas las instancias negativas de la clase, mientras que valores menores a 1.0000 indican que hubo algunos falsos positivos.Como podemos visualizar la clase 3 y la clase 1 identificaron correctamente todas las instancias negativas de la clase.

Pos Pred Value (Valor Predictivo Positivo): Es la proporción de instancias clasificadas como positivas que realmente pertenecen a la clase en cuestión. Por ejemplo, un valor de 1.0000 significa que todas las instancias clasificadas como positivas para la clase 3 realmente pertenecen a la clase 3.

Neg Pred Value (Valor Predictivo Negativo): Es la proporción de instancias clasificadas como negativas que realmente no pertenecen a la clase en cuestión.

Prevalence (Prevalencia): Es la proporción de instancias en el conjunto de datos que pertenecen a la clase en cuestión. Por ejemplo, para la clase 3, el 30% de las instancias en el conjunto de datos pertenecen a esta clase.

Detection Rate (Tasa de Detección): Es la proporción de instancias correctamente identificadas por el modelo para la clase en cuestión. Por ejemplo, para la clase 3, el 10% de las instancias positivas fueron correctamente identificadas.

Detection Prevalence (Prevalencia de Detección): Es la proporción de instancias clasificadas como positivas para la clase en cuestión.

Balanced Accuracy (Exactitud Equilibrada): Es la media aritmética de la sensibilidad y la especificidad, y proporciona una medida general del rendimiento del modelo para la clase en cuestión.

El recall promedio 0.82 es decir 82% de las observaciones positivas fueron predichas correctamente. A continuacion se muestra la tabla de recall por clase:

|Clase 3 | Clase 2 | Clase 4 | Clase 1 |
|---|---|---|---|
| 1.0000000 | 1.0000000 | 1.0000000 | 0.5555556 |

### Validación Cruzada

Como podemos ver, uno de los mayores problema del conjunto de datos elegido es que es muy pequeño en cuanto a cantidad de observaciones, por lo tanto, utilizamos la técnica de validación cruzada, para poder evaluar los hiperparametros mencionados anteriormente y así poder proponer mejoras en el modelo. 

Para comenzar, explicaremos brevemente, que es. La validación cruzada es una técnica estadística utilizada para evaluar el rendimiento y la generalización de un modelo de machine learning. También se utiliza para obtener los hiperparámetros óptimos de un modelo, en nuestro caso, la utilizaremos para esto. El proceso típico para obtener los hiperparámetros mediante validación cruzada es el siguiente:

1. División del conjunto de datos: Se divide el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba. El conjunto de entrenamiento se usará para entrenar el modelo y el conjunto de prueba se utilizará para evaluar su rendimiento final.
2. Búsqueda de hiperparámetros: Se elige un conjunto de posibles valores para los hiperparámetros que se desean ajustar.
3. Validación cruzada: Se realiza la validación cruzada utilizando el conjunto de entrenamiento. Para cada combinación de hiperparámetros, se divide el conjunto de entrenamiento en k folds y se realiza la validación cruzada para obtener una estimación del rendimiento del modelo.
4. Selección de hiperparámetros: Se seleccionan aquellos valores de hiperparámetros que dieron lugar al mejor rendimiento promedio durante la validación cruzada.
5. Entrenamiento final: Una vez que se han seleccionado los mejores hiperparámetros, el modelo se entrena nuevamente utilizando todo el conjunto de entrenamiento, esta vez con los hiperparámetros óptimos.
6. Evaluación final: Finalmente, se evalúa el rendimiento del modelo utilizando el conjunto de prueba que no ha sido utilizado durante la validación cruzada.

Este enfoque permite evitar el sobreajuste y obtener hiperparámetros que produzcan un rendimiento más generalizable para datos no vistos. La validación cruzada es una herramienta poderosa para la selección de hiperparámetros y es ampliamente utilizada en el desarrollo de modelos de machine learning robustos y precisos.

### Variación de la distancia

Como primera variación, luego de definir 5 folds y comenzar con la validación cruzada, decidimos probar distancia euclidiana y manhattan para evaluar cual de los dos comportamientos era mejor a la hora de predecir, para esto guardamos ambos accuracy por cada fold y al final del bucle, luego de recorrer los 5 folds, se calculo un accuracy promedio para Manhattan y para Euclidiana y toma la que tenga un mejor rendimiento, que en nuestro caso fue Euclidiana, luego se utiliza esa distancia para predecir el conjunto prueba definido al comienzo, con esto mejoramos mucho el rendimiento del modelo. Las matriz de confusión y demas metricas se pueden visualizar en la tabla 2, tabla 3 y tabla 4; no hay que olvidar que el rendimiento depende mucho de la división en conjunto train y test que se hace en un comienzo, ya que al tener un conjunto de datos desbalanceados, el modelo baja su rendimiento cuando en el conjunto prueba contiene muchas instancias de las clases desbalanceadas.

**Matriz de confusión**

|            | Re | fe | ren | cia |
|------------|---|---|---|---|
| Predicción | 1 | 2 | 3 | 4 |
| 1          | 5 | 0 | 0 | 4 |
| 2          | 0 | 6 | 0 | 0 |
| 3          | 0 | 0 | 3 | 0 |
| 4          | 0 | 0 | 0 | 2 |

**Accuracy (Exactitud)**

En este caso, el valor de Accuracy es 0.8, lo que significa que el 80% de las predicciones fueron correctas. 

**Estadísticas generales**

|            | Clase 1 | Clase 2 | Clase 3 | Clase 4 |
|------------|---|---|---|---|
| Sensitivy | 1.0000 | 1.0000 | 0.3333 | 1.0000 |
| Specificity | 1.0000 | 1.0000 | 1.0000 | 0.7333 | 
| Pos Pred Value | 1.0000 | 1.0000 | 1.0000 | 0.5556 |
| Neg Pred Value | 1.0000 | 0.7778 | 1.0000 | 1.0000 |
| Prevalence | 0.1500 | 0.3000 | 0.3000 | 0.2500 |
| Detection Rate | 0.1500 | 0.3000 | 0.1000 | 0.2500 |
| Detection Prevalence | 0.1500 | 0.3000 | 0.1000 | 0.4500 |
| Balanced Accuracy | 1.0000 | 1.0000 |  0.6667 | 0.8667 |

El modelo ha alcanzado un recall del 100% en las clases 3, 2 y 4, lo que indica que pudo detectar correctamente todas las instancias positivas para esas clases. Sin embargo, en la clase 1, el recall fue del 55.56%, lo que sugiere que el modelo no pudo detectar todas las instancias positivas de esa clase. El recall promedio 0.89 es decir 89% de las observaciones positivas fueron predichas correctamente.

|Clase 3 | Clase 2 | Clase 4 | Clase 1 |
|---|---|---|---|
| 1.0000000 | 1.0000000 | 1.0000000 | 0.5555556 |

### Variación del cálculo del centroide
Otra variación que se podía realizar para intentar mejorar las métricas, era variar la forma de calcular el vector centroide para cada una de las clases, es decir, en vez de calcularlo con el promedio o media, calcularlo con la fórmula de mediana, que trae algunos beneficios como se mencionó en el marco teórico. Sin embargo para nuestro modelo, esto no nos benefició ya que no aumentó el rendimiento, simplemente quedo en 0.8, a demas el recall disminuyo un poco. A continuación, dejamos los datos obtenidos.

**Matriz de confusión**

|            | Re | fe | ren | cia |
|------------|---|---|---|---|
| Predicción | 1 | 2 | 3 | 4 |
| 1          | 3 | 0 | 0 | 0 |
| 2          | 0 | 6 | 1 | 0 |
| 3          | 0 | 0 | 2 | 0 |
| 4          | 0 | 0 | 3 | 5 |

**Accuracy (Exactitud)**

En este caso, el valor de Accuracy es 0.8, lo que significa que el 80% de las predicciones fueron correctas. 

**Estadísticas generales**

|            | Clase 1 | Clase 2 | Clase 3 | Clase 4 |
|------------|---|---|---|---|
| Sensitivy | 1.0000 | 1.0000 | 0.3333 | 1.0000 |
| Specificity | 1.0000 | 0.9286 | 1.0000 | 0.8000 | 
| Pos Pred Value | 1.0000 | 0.8571 | 1.0000 | 0.625 |
| Neg Pred Value | 1.0000 | 1.0000 | 0.7778 | 1.0000 |
| Prevalence | 0.1500 | 0.3000 | 0.3000 | 0.2500 |
| Detection Rate | 0.1500 | 0.3000 | 0.1000 | 0.2500 |
| Detection Prevalence | 0.1500 | 0.3500 | 0.1000 | 0.4000 |
| Balanced Accuracy | 1.0000 | 0.9643 |  0.6667 | 0.9000 |

La clase 3 y 4 alcanzaron un recall del 100%, mientras que la clase 4 disminuyo y la clase 1 aumento un poco su porcentaje de aciertos.

|Clase 3 | Clase 2 | Clase 4 | Clase 1 |
|---|---|---|---|
| 1.0000000 | 0.8571429 | 1.0000000 |0.6250000 |


### Balanceo de Clases con Pesos

Entendiendo el problema de nuestro dataset, una solución que podía mejorar nuestro modelo era balancear las clases de modo tal que todas tuvieran la misma incumbencia a la hora de realizar predicciones. Sin embargo, esto no solucionó nuestro problema, dado que el dataset sigue siendo muy pequeño en cuanto a observaciones, por lo tanto  la clase desbalanceada tiene muy pocas muestras en comparación con las otras clases, incluso si se le asigna un peso mayor, las muestras no fueron suficientes para proporcionar información significativa para aprender patrones y relaciones en los datos; también había falta de representatividad, entonces las muestras de la clase desbalanceada no son representativas del problema real por lo tanto los pesos no ayudan a mejorar el rendimiento.

El rendimiento continuó siendo el mismo del algoritmo sin mejoras 0.7 e incluso cuando los pesos eran muy grandes respecto a las otras clases, el algoritmo empezaba a fallar en las clases que si estaban balanceadas. A continuación adjuntamos algunos gráficos que ayudan a explicar la situación


...

## Algoritmo GLMNET

Implementamos el algoritmo GLMNET en R, con el dataset Khan, sin ajustar el modelo, es decir, sin variar los posibles parámetros, utilizando los predeterminados. 

Para esto, en el código en R primero se instalan los paquetes necesarios y luego se cargan. También se carga el conjunto de datos "Khan" el cual se separa en conjuntos de entrenamiento (xtrain y ytrain) y de prueba (xtest y ytest). Luego para el entrenamiento del modelo GLMNET tenemos la línea:

`model <- glmnet(xtrain, ytrain, family = "multinomial")`

Donde función glmnet es parte del paquete "glmnet" en R, y se utiliza para ajustar modelos de regresión logística o modelos lineales generalizados con regularización. A continuación, una descripción de los parámetros de la función:
* *xtrain:* Es la matriz de características del conjunto de entrenamiento. Estas serán utilizadas para entrenar el modelo y predecir las clases.
* *ytrain:* Es el vector que contiene las etiquetas de clase correspondientes a las observaciones del conjunto de entrenamiento. En otras palabras, es el vector de clases conocidas asociadas a cada fila en xtrain. El modelo usará esta información para aprender a realizar las predicciones correctamente.
* *family = "multinomial":* Este argumento especifica el tipo de modelo de regresión logística que se va a ajustar. En este caso, se selecciona "multinomial" para indicar que estamos tratando con un problema de clasificación multiclase. Esto es importante porque permite que el modelo maneje más de dos categorías de clases en lugar de solo dos (como en el caso de clasificación binaria).

En este caso para los valores de alpha, lambda y standardize utilizamos los valores predeterminados en la función glmnet.

El resultado del entrenamiento del modelo se almacena en la variable *model*, que contendrá toda la información necesaria para hacer predicciones posteriores sobre nuevos datos. Para estas predicciones utilizamos el conjunto de prueba (xtest) y el modelo entrenado. 

Finalmente, para calcular la precisión del modelo comparamos las predicciones con el conjunto de prueba (ytest), obteniendo las siguientes métricas:

**Matriz de confusión**

|            | Re | fe | ren | cia |
|------------|---|---|---|---|
| Predicción | 1 | 2 | 3 | 4 |
| 1          | 3 | 0 | 0 | 0 |
| 2          | 0 | 4 | 1 | 0 |
| 3          | 0 | 0 | 2 | 0 |
| 4          | 0 | 0 | 3 | 5 |

La matriz de confusión nos muestra lo siguiente:
* La “Clase 1” tiene 3 instancias que fueron clasificadas correctamente
* La “Clase 2” tiene 4 instancias que fueron clasificadas correctamente
* La “Clase 3” tiene 2 instancias que fueron clasificadas correctamente
* La “Clase 4” tiene 5 instancias que fueron clasificadas correctamente.
* Se predijo 1 instancia de la “Clase 3” que en realidad pertenecía a la “Clase 2”
* Se predijo 3 instancias de la “Clase 4” que en realidad pertenecía a la “Clase 4”

**Accuracy (Exactitud)**

Representa la proporción de predicciones correctas sobre el total de predicciones. En este caso, el valor de Accuracy es *0.935*, lo que significa que el 93.5% de las predicciones fueron corectas.   

**Estadísticas generales**

|            | Clase 1 | Clase 2 | Clase 3 | Clase 4 |
|------------|---|---|---|---|
| Sensitivy | 1.0000 | 0.6667 | 0.3333 | 1.0000 |
| Specificity | 1.0000 | 0.9286 | 1.0000 | 0.6667 |
| Pos Pred Value | 1.0000 | 0.8000 | 1.0000 | 0.5000 |
| Neg Pred Value | 1.0000 | 0.8667 | 0.7778 | 1.0000 |
| Prevalence | 0.1500 | 0.3000 | 0.3000 | 0.2500 |
| Detection Rate | 0.1500 | 0.2000 | 0.2000 | 0.2500 |
| Detection Prevalence | 0.1500 | 0.2500 | 0.1000 | 0.5000 |
| Balanced Accuracy | 1.0000 | 0.7976 | 0.6667 | 0.8333 |

A pesar de que con el algoritmo GLMNET, con sus parametros por defecto, obtenemos mejores métricas que con el algoritmo del centroide más cercano, consideramos que podiamos afinar aún más el rendimiento del modelo. Mediante investigación, encontramos que para dicho algoritmo podíamos hacer más pruebas variando los siguientes parametros: standardize, alpha y lambda

Por lo tanto, con esta información, procedemos a realizar pruebas modificando los valores de los parametros por defecto. Buscando mejorar las métricas obtenidas hasta el momento.

### Variación del parámetro standarize

Este parámetro indica si se deben estandarizar las variables predictoras antes de ajustar el modelo. Si se establece en TRUE, las variables se estandarizan de modo que tengan media cero y desviación estándar uno. Si se establece en FALSE, las variables no se estandarizan. El valor predeterminado es TRUE.

Modificamos la línea en donde se aplica la función glmnet para que ya se no estandaricen las variables predictoras:

`model <- glmnet(xtrain, ytrain, family = "multinomial", standardize = FALSE)`

Pudimos observar que, en todas las iteraciones, los resultados de precisión fueron más bajos cuando no usamos estandarización (standardize = FALSE) con precisión de 0.89, comparados con la aplicación del modelo con estandarización (standardize = TRUE) que obtuvo precisión de 0.93.
Esto puede deberse a que en este caso la estandarización es beneficiosa ya que las variables tienen diferentes escalas y se desea evitar que una variable con valores grandes domine el modelo en comparación con las variables con valores más pequeños.

Al momento de evaluar el modelo obtuvimos las siguientes métricas:

**Matriz de confusión**

|            | Re | fe | ren | cia |
|------------|---|---|---|---|
| Predicción | 1 | 2 | 3 | 4 |
| 1          | 3 | 0 | 0 | 0 |
| 2          | 0 | 5 | 1 | 0 |
| 3          | 0 | 1 | 4 | 0 |
| 4          | 0 | 0 | 1 | 5 |

La matriz de confusión nos muestra lo siguiente:
* La “Clase 1” tiene 3 instancias que fueron clasificadas correctamente
* La “Clase 2” tiene 5 instancias que fueron clasificadas correctamente
* La “Clase 3” tiene 4 instancias que fueron clasificadas correctamente
* La “Clase 4” tiene 5 instancias que fueron clasificadas correctamente.
* Se predijo 1 instancia de la “Clase 3” que en realidad pertenecía a la “Clase 2”
* Se predijo 1 instancia de la “Clase 3” que en realidad pertenecía a la “Clase 4”
* Se predijo 1 instancias de la “Clase 2” que en realidad pertenecía a la “Clase 4”

**Accuracy (Exactitud)**

Representa la proporción de predicciones correctas sobre el total de predicciones. En este caso, el valor de Accuracy es 0.89, lo que significa que el 89% de las predicciones fueron corectas.  

**Estadísticas generales**

|            | Clase 1 | Clase 2 | Clase 3 | Clase 4 |
|------------|---|---|---|---|
| Sensitivy | 1.0000 | 0.6667 | 0.3333 | 1.0000 |
| Specificity | 1.0000 | 0.9286 | 1.0000 | 0.6667 |
| Pos Pred Value | 1.0000 | 0.8000 | 1.0000 | 0.5000 |
| Neg Pred Value | 1.0000 | 0.8667 | 0.7778 | 1.0000 |
| Prevalence | 0.1500 | 0.3000 | 0.3000 | 0.2500 |
| Detection Rate | 0.1500 | 0.2000 | 0.2000 | 0.2500 |
| Detection Prevalence | 0.1500 | 0.2500 | 0.1000 | 0.5000 |
| Balanced Accuracy | 1.0000 | 0.7976 | 0.6667 | 0.8333 |

### Variación del parámetro alpha

Este parámetro controla la mezcla entre la penalización L1 y L2. Toma valores entre 0 y 1. Un valor de 1 corresponde a la penalización LASSO (L1) y un valor de 0 corresponde a la penalización Ridge (L2). Los valores intermedios permiten combinaciones de ambas penalizaciones. El valor predeterminado es 1.

Para variar alpha en el código y encontrar el más óptimo para el modelo, primero definimos una secuencia de valores de alpha en el rango de 0 a 1 con incrementos de 0.1

![image](https://github.com/agussanchez97/ia-uncuyo-2021/assets/88351747/503213fd-a51d-4006-8d4b-f13e6b3785d6)

Se implementa el algoritmo de GLMNET para cada valor de alpha utilizando los datos de entrenamiento. Mientras almacenamos estos datos en una lista results, para luego calcular la precicion de cada modelo, obteniendo los siguientes datos:

| Valor de alpha | Precisión |
|---|---|
| 0 | 0.666 |
| 0.1 | 0.905 |
| 0.2 | 0.9245 |
| 0.3 | 0.931 |
| 0.4 | 0.933 |
| 0.5 | 0.936 |
| 0.6 | 0.9375 |
| 0.7 | 0.9385 |
| 0.8 | 0.938 |
| 0.9 | 0.9375 |
| 1 | 0.935 |

![image](https://github.com/agussanchez97/ia-uncuyo-2021/assets/88351747/e83c60a4-9232-4fc3-bd69-be416e9ce79a)

Imagen 9: grafico de la precicion del modelo a medida que varia alpha

Luego en el código buscamos el mejor valor de alpha al comparar la precisión promedio en el conjunto de prueba para cada modelo ajustado. Se inicializan las variables best_accuracy y best_alpha que se actualizan si se encuentra un modelo con una precisión mayor.

Asi, entrenamos el modelo glmnet utilizando el mejor valor de alpha obtenido, el cual es de 0.7. Y luego lo ejecutamos con los datos de test, obteniendo las siguientes métricas:

**Matriz de confusión**

|            | Re | fe | ren | cia |
|------------|---|---|---|---|
| Predicción | 1 | 2 | 3 | 4 |
| 1          | 3 | 0 | 0 | 0 |
| 2          | 0 | 4 | 1 | 0 |
| 3          | 0 | 0 | 2 | 0 |
| 4          | 0 | 0 | 3 | 5 |

La matriz de confusión nos muestra lo siguiente:
* La “Clase 1” tiene 3 instancias que fueron clasificadas correctamente
* La “Clase 2” tiene 4 instancias que fueron clasificadas correctamente
* La “Clase 3” tiene 2 instancias que fueron clasificadas correctamente
* La “Clase 4” tiene 5 instancias que fueron clasificadas correctamente.
* Se predijo 1 instancia de la “Clase 3” que en realidad pertenecía a la “Clase 2”
* Se predijo 3 instancias de la “Clase 4” que en realidad pertenecía a la “Clase 4”

**Accuracy (Exactitud)**

En este caso, el valor de Accuracy es 0.938, lo que significa que el 93.8% de las predicciones fueron corectas.   

**Estadísticas generales**

|            | Clase 1 | Clase 2 | Clase 3 | Clase 4 |
|------------|---|---|---|---|
| Sensitivy | 1.0000 | 0.6667 | 0.3333 | 1.0000 |
| Specificity | 1.0000 | 0.9286 | 1.0000 | 0.6667 |
| Pos Pred Value | 1.0000 | 0.8000 | 1.0000 | 0.5000 |
| Neg Pred Value | 1.0000 | 0.8667 | 0.7778 | 1.0000 |
| Prevalence | 0.1500 | 0.3000 | 0.3000 | 0.2500 |
| Detection Rate | 0.1500 | 0.2000 | 0.2000 | 0.2500 |
| Detection Prevalence | 0.1500 | 0.2500 | 0.1000 | 0.5000 |
| Balanced Accuracy | 1.0000 | 0.7976 | 0.6667 | 0.8333 |

Entonces se encontró que el valor óptimo de "alpha" para el modelo fue de 0.7, lo que indica una combinación de penalización LASSO (L1) y penalización Ridge (L2). Esto sugiere que una combinación de ambas penalizaciones es beneficiosa para el rendimiento del modelo.

### Variación del parámetro lambda

Este parámetro controla la fuerza de la penalización y regula el grado de regularización del modelo. Un valor más alto de lambda da como resultado una mayor regularización y reducción en los coeficientes. Por el contrario, un valor más bajo de lambda permite que los coeficientes sean menos restringidos. El valor predeterminado es un rango de valores que se determina automáticamente a través de un proceso de selección.

Para variar lambda en el código y encontrar el más óptimo para el modelo, primero definimos una secuencia de valores de lambda en un vector de valores que sigue una escala logarítmica:

![image](https://github.com/agussanchez97/ia-uncuyo-2021/assets/88351747/b6ffd88e-5216-49a9-8f9b-355c9ce89568)

Estos valores de lambda cubren un rango amplio y permiten probar diferentes magnitudes de regularización en el modelo.

Se implementa el algoritmo de GLMNET para cada valor de lambda utilizando los datos de entrenamiento. Mientras almacenamos estos datos en una lista results, para luego calcular la precicion de cada modelo, obteniendo los siguientes datos:

| Valor de lambda | Precisión |
|-----------------|-----------|
| 0.01000000 | 1 |
| 0.03162278 | 1 |
| 0.10000000 | 1 |
| 0.31622777 | 0.55 |
| 1.00000000 | 1 |
| 3.16227766 | 0.3 |
| 10.00000000 | 0.3 |
| 31.62277660 | 0.3 |
| 100.00000000 | 0.3 |

![image](https://github.com/agussanchez97/ia-uncuyo-2021/assets/88351747/148cf26a-1db3-4a00-83fb-1179db9bce0e)

Imagen 10: grafico de la precicion del modelo a medida que varia lambda

Luego en el código buscamos el mejor valor de lambda al comparar la precisión promedio en el conjunto de prueba para cada modelo ajustado. Se inicializan las variables best_accuracy y best_lambda que se actualizan si se encuentra un modelo con una precisión mayor.
Así, entrenamos el modelo glmnet utilizando el mejor valor de lambda obtenido, el cual es de 0.01. Y luego lo ejecutamos con los datos de test, obteniendo las siguientes métricas:

**Matriz de confusión**

|            | Re | fe | ren | cia |
|------------|---|---|---|---|
| Predicción | 1 | 2 | 3 | 4 |
| 1          | 3 | 0 | 0 | 0 |
| 2          | 0 | 6 | 0 | 0 |
| 3          | 0 | 0 | 6 | 0 |
| 4          | 0 | 0 | 0 | 5 |

La matriz de confusión nos muestra lo siguiente:
* La “Clase 1” tiene 3 instancias que fueron clasificadas correctamente
* La “Clase 2” tiene 6 instancias que fueron clasificadas correctamente
* La “Clase 3” tiene 6 instancias que fueron clasificadas correctamente
* La “Clase 4” tiene 5 instancias que fueron clasificadas correctamente.
* No se predijeron instancias incorrectamente

**Accuracy (Exactitud)**

En este caso, el valor de Accuracy es 1, lo que significa que el 100% de las predicciones fueron corectas.   

**Estadísticas generales**

|            | Clase 1 | Clase 2 | Clase 3 | Clase 4 |
|------------|---|---|---|---|
| Sensitivy | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Specificity | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Pos Pred Value | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Neg Pred Value | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Prevalence | 0.1500 | 0.3000 | 0.3000 | 0.2500 |
| Detection Rate | 0.1500 | 0.3000 | 0.3000 | 0.2500 |
| Detection Prevalence | 0.1500 | 0.3000 | 0.3000 | 0.25000 |
| Balanced Accuracy | 1.0000 | 1.0000 | 1.0000 | 1.0000 |

Entonces se encontró que el mejor valor de "lambda" para el modelo fue de 0.01. Un valor más bajo de lambda permite que los coeficientes sean menos restringidos, lo que lleva a un mejor rendimiento del modelo en este caso.

# Análisis y discusión de resultados

Al interpretar las métricas de precisión, sensibilidad, especificidad, etc., es importante considerar el contexto del problema. En este caso, observamos que con el conjunto de datos "Khan", el modelo muestra una alta sensibilidad para la "Clase 1" y "Clase 4", lo que significa que identifica correctamente la mayoría de las instancias de estas clases. Sin embargo, la sensibilidad para la "Clase 3" es baja, lo que indica que el modelo tiene dificultades para identificar correctamente las instancias de esta clase.

### Algoritmo centroide mas cercano

....

### Algoritmo GLMNET

Uno de los objetivos del diseño experimental fue ajustar el modelo de clasificación multiclase utilizando el algoritmo GLMNET en R con el conjunto de datos "Khan". Para esto, realizamos pruebas para encontrar los mejores valores de los parámetros standardize, alpha, y lambda, con el fin de mejorar la precisión del modelo. Utilizamos las métricas de precisión, matriz de confusión, sensibilidad, especificidad, valor predictivo positivo y valor predictivo negativo para evaluar el rendimiento del modelo en la clasificación de las clases.

En la primera ejecución del algoritmo GLMNET con los parámetros por defecto, obtuvimos  una precisión de 93.5%, lo que indico que el modelo predijo correctamente la clase de la mayoría de las instancias en el conjunto de prueba. Sin embargo, hubo algunas instancias mal clasificadas

Luego, realizamos una variación del parámetro standardize para decidir si estandarizar las variables predictoras antes de ajustar el modelo. Encontramos que la estandarización mejoraba el rendimiento del modelo, ya que sin ella la precicion del modelo bajaba a 89%. Esto nos sugirió que la estandarización de las variables predictoras es beneficiosa y ayuda al modelo a tener un mejor rendimiento al evitar que las variables con escalas más grandes dominen las variables con escalas más pequeñas.

Posteriormente, variamos el parámetro alpha, que controla la mezcla entre la penalización L1 (LASSO) y L2 (Ridge). Observamos que el mejor valor de `alpha` para este problema de clasificación multiclase fue 0.7 ya que el modelo alcanzó una precisión del 93.8%. Esto indica que la combinación de las penalizaciones L1 y L2 en una proporción determinada (0.7 de L1 y 0.3 de L2) fue la más adecuada para el conjunto de datos. Que el modelo funcione mejor con una mayor proporción de penalización L1 nos suguiere que se beneficia de la selección de características y la reducción del número de coeficientes utilizados, ya que la penalización L1 hace que el modelo tienda a seleccionar un menor número de características más relevantes y descartar aquellas que contribuyen menos a la predicción. También se debe a que es mejor L1 cuando hay escasez de datos ya que reduce el riesgo de sobreajuste y puede simplificar el modelo, evitando el uso excesivo de características.

Finalmente, variamos el parámetro lambda, que regula la fuerza de la penalización y controla el grado de regularización del modelo. Encontramos que el mejor valor de lambda fue 0.01, lo que resultó en una precisión del 100%. Esto significa que este valor de lambda proporcionó la cantidad justa de regularización para que el modelo generalizara bien a nuevos datos. Un valor más alto penalizaba demasiado los coeficientes, reduciendo la capacidad del modelo para ajustarse a los datos de entrenamiento.

| Modelo    | Precicion     |
|------------|-------------|
| standardize = FALSE, alpha= defecto, lambda= defecto | 0,89  |
| standardize = TUE, alpha= defecto, lambda= defecto | 0,935 |
| standardize = TRUE, alpha= 0.7, lambda= defecto | 0,938  |
| standardize = TRUE, alpha= 0.7, lambda= 0.01  | 1 |

La precisión general del modelo GLMNET para el conjunto de datos Khan se presenta siempre con un valor cercano a 0.9, lo que significa que el 90% de las predicciones son correctas. Este valor es bastante alto y nos sugiere que el modelo tiene un buen desempeño general en la clasificación de las instancias. Ademas, mediante la variación de los parámetros mejoramos el rendimiento del modelo. La estandarización es beneficiosa debido a la presencia de variables con diferentes escalas y una combinación de penalizaciones L1 y L2 (alpha = 0.7) junto con una regularización (lambda = 0.01) procen el mejor modelo.

### Comparacion de ambos algoritmos

...

# Conclusiones finales
Observaciones finales sobre el tema y es muy importante indicar aquellas tareas o experimentos que 
