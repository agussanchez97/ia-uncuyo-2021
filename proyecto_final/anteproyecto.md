# Trabajo Final Inteligencia Artificial I 

## TITULO : ALGORITMOS DE CLASIFICACIÓN PARA INFORMACIÓN GENETICA.

##### Codigo: ACLASIGEN

###### Alumna: Sanchez Lanza Agustina
###### Legajo: 11549


##### Objetivo: 

El objetivo es probar distintos algoritmos para dado un dataset, encontrar el conjunto de genes mas acertado, que permita clasificar entre 2 grupos: personas que probablemente puedan padecen cancer y personas que no.

##### Estrategia: 

Para cumplir con el objetivo he seleccionado 2 algoritmos distintos:

-Centroide mas cercano: es un modelo de clasificación que asigna a las observaciones la etiqueta de la clase de muestras de entrenamiento cuya media ( centroide ) está más cerca de la observación
-Glmnet: es un algoritmo de regresion lineal , que penaliza variables que considera menos importantes para el entrenamiento.

Para abordar este problema , mi estrategia es entrenar un dataset compuesto por informacion genetica de 65 personas con ambos algoritmos y en base a eso obtener metricas , distinguir similutedes y diferencias y por ultimo con toda esa informaciòn decidir cual estima mejor mi problema y describir porque considero esto. 

Uno de los principales desafios es que el dataset es pequeño , es decir son pocos datos para poder entrenar el modelo y que el mismo encuentre correctamente el conjunto.

##### Justificación : 

Considero que este problema se puede solucionar con inteligencia articial , ya que esta divido en 2 clases muy distintas , como dije anterior personas que pueden llegar a tener cancer y personas que no , lo que remota a un problema de clasificación que se puede abordar con una de las ramas de la IA que es machine learning, la misma contiene una lista larga de algoritmos para entrenar el conjunto de datos y obtener un resultado acertado.

##### Estimación de tiempo:

22 dias 

##### Actividades:

- Actividad 1: Buscar/recolectar bibliografia de los temas a tratar. [2 dias]
- Actividad 2: Leer libro "Introduction to Statistical Learning" capitulos 3.1 y 6.1 y 6.2 para entender regresion lineal y sus algoritmos, ampliar informacion de ser necesario.[3 dias].
- Actividad 3: Leer la bibliografia encontrada(respecto a los algoritmos) , analizar , buscar cada una de las cosas que no alcance a comprender con el material. [7 dias]
- Actividad 4: Ver el algoritmo "GLMNET" , ver ejemplos , ver sus parametros , aprender como funciona,ver librerias, codigo.[2 dias]
- Actividad 5: Ver el funcionamiento del algoritmo "Centroide mas cercano",parametros,librerias , codigo.[2 dias]
- Actividad 6: Evaluar el dataset dado sobre los algoritmos.[4 dias]
- Actividad 7: Recompilar datos.[4 dias]
- Actividad 8: Evaluar los resultados dados , hacer anotaciones, sacar conclusiones.[3 dias]
- Actividad 9: Elaborar el informe final.[6 dias]
- Actividad 10: Entregar el trabajo.[primer o segunda fecha de diciembre]
- Actividad opcional: En el caso de ir mas rapido de lo esperado , evaluar posibles mejoras al algoritmos (ej : centroide mas cercano MEJORADO) 

##### Cronograma:

![image](https://user-images.githubusercontent.com/82063987/139735305-fc26c3b9-7424-4575-8434-e951b6b82cc7.png)

##### Bibliografia:

https://en.wikipedia.org/wiki/Nearest_centroid_classifier
https://www.ncbi.nlm.nih.gov/pmc/articles/PMC124443/
https://www.aprendemachinelearning.com/k-means-en-python-paso-a-paso/
https://glmnet.stanford.edu/articles/glmnet.html
