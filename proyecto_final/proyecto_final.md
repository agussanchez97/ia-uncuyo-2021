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

....

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

<small>Figura 2: representacion de la regresion lineal. Tomado del libro "An Introduction to Statistical Learning with application in R"( ISLR ). página 62.</small>

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

Figura 3: balance de clases del dataset Khan

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

Imagen 1: porción de codigo tomado de la implementación propuesta

En la imagen 1 línea 20 podemos observar como se  calcula la matriz de covarianza del conjunto de entrenamiento usando la función cov. La función t se utiliza para transponer la matriz xtrain y asegurarse de que las variables estén en las columnas y las observaciones en las filas. Luego en la línea 24 se calcula la media de cada variable utilizando la función colMeans. De nuevo, se transpone la matriz xtrain con la función t para que las variables estén en las columnas.

Utilizamos la función Mahalanobis para calcular la distancia de Mahalanobis para cada observación en el conjunto de entrenamiento esto se visualiza en la línea 27 Se proporcionan los siguientes argumentos:

t(xtrain): La matriz de datos transpuesta.
center = means: El vector de medias calculado anteriormente.
cov = cov_matrix: La matriz de covarianza calculada anteriormente.

Establecemos un umbral para identificar valores atípicos. En este caso, utilizamos el cuantil 0.95 de la distribución chi-cuadrado con grados de libertad igual al número de variables en el conjunto de entrenamiento. Esto se realiza con la función qchisq.

Finalmente, se utiliza la función which para identificar los índices de las observaciones que tienen una distancia de Mahalanobis mayor que el umbral establecido. Estos índices se almacenan en la variable outliers.

Concluimos imprimiendo los datos y los resultados obtenidos fueron que no hay valores anómalos, ni extremos de acuerdo al umbral fijado.

![image](https://github.com/agussanchez97/ia-uncuyo-2021/assets/88351747/2060ac2c-2f6c-48b5-aa3d-aea70bfdcdab)

Imagen 2: resultado de la ejecución del código imagen 1

## Centroide mas cercano

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

|            | Pre | di | cci | ón |
|------------|---|---|---|---|
| Referencia | 1 | 2 | 3 | 4 |
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

###



# Análisis y discusión de resultados
En esta sección se deberá realizar un mínimo análisis sobre los resultados obtenidos. El objetivo es tratar de razonar sobre las causas de los resultados obtenidos en la fase experimental a fin de proveer una posible justificación. Aquí se incluyen posibles limitaciones en los algoritmos elegidos, en la simulación planteada, los datos, etc.

# Conclusiones finales
Observaciones finales sobre el tema y es muy importante indicar aquellas tareas o experimentos que 
