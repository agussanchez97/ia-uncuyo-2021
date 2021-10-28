##### A partir del archivo arbolado-publico-mendoza-2021-train.csv, responder las siguientes preguntas:
##### a-Cual es la distribución de las clase inclinacion_peligrosa?
![image](https://user-images.githubusercontent.com/82063987/139264918-bfebf065-92aa-4b16-afc4-44e9ac90d6a7.png)
Podemos observar que la clase mayoritaria es la clase que no posee inclinación peligrosa siendo la minoritaria la clase con inclinacion peligrosa, gracias al grafico podemos ver el gran desbalance de clases en el dataset.

##### b-¿Se puede considerar alguna sección más peligrosa que otra?
![image](https://user-images.githubusercontent.com/82063987/139265404-f542aaa1-5f23-4b0c-a70a-d14cef00c09b.png)
Podemos observar que la sección 4 es la mas peligrosa , siendo que hay mayor cantidad de arboles con inclinación peligrosa, otra cosa que observamos es que las secciones 1,2,3 a pesar de tener pocos casos de inclinacion peligrosa , son mas peligrosas que secciones como 7,8 etc.

##### c-¿Se puede considerar alguna especie más peligrosa que otra?
![image](https://user-images.githubusercontent.com/82063987/139272309-ce3ec938-3ae7-46dc-97aa-358d6bdebe77.png)
No hay tanta variacion entre especies pero podemos ver que Morera tiene un gran cantidad de arboles con inclinación peligrosa , respecto a los otros.

##### A partir del archivo arbolado-publico-mendoza-2021-train.csv:

##### a-Generar un histograma de frecuencia para la variable circ_tronco_cm. Probar con diferentes  números de bins.  

![image](https://user-images.githubusercontent.com/82063987/139272797-a6983d52-5962-439d-8317-54c1c6d20a0d.png)
![image](https://user-images.githubusercontent.com/82063987/139273219-f6beaf99-f4c1-40fd-a429-a991ec5422e8.png)
bins = 100

##### b- Repetir los puntos a)  pero separando por la clase de la variable inclinación_peligrosa?
![image](https://user-images.githubusercontent.com/82063987/139273483-0ac3bdc3-e5db-4edf-bf7e-eca37bf3f9a0.png)
![image](https://user-images.githubusercontent.com/82063987/139273693-b0832981-6706-4489-bce1-a9264408b919.png)

##### c-Crear una nueva variable categórica de nombre circ_tronco_cm_cat a partir circ_tronco_cm, en donde puedan asignarse solo  4 posibles valores [ muy alto, alto, medio, bajo ]. Utilizar la información del punto a. para seleccionar los puntos de corte para cada categoría. Guardar el nuevo dataframe bajo el nombre de arbolado-publico-mendoza-2021-circ_tronco_cm-train.csv
`circ_tronco_cm`<=100 entonces'bajo'
circ_tronco_cm`>100 & `circ_tronco_cm` <= 200, entonces 'medio'
circ_tronco_cm` > 200 & `circ_tronco_cm` <= 300 entonces 'alto' si no caso contrario 'muy alto'

##### 3-Colocar un archivo con el nombre tp7-classificadores.md que contenga:
##### a- La matriz de confusión para el clasificador aleatorio y las métricas correspondientes. (tabla)
     Valor Predicho
     SI    NO
 SI  379  336
 NO  2820 2846
