### Descripción del proceso de preprocesamiento (si es que lo hubiera) Como por ejemplo:

Para el preprocesamento de datos , como el dataset estaba desbalanceado lo primero que hice fue balancearlo reduciendo los casos da la clase mayoritaria
(arboles que no tiene inclinación peligrosa) a la misma cantidad de la clase minoritaria(arboles que si tienen inclinación peligrosa), esto lo realice con
la funcion data_train_down(). Luego cree otra columna( nuevas varuable) con la información de circ_tronco_cm , catalogando en bajo , medio , alto y muy alto. 
Una vez listo el conjunto de datos pude comenzar a entrenarlo, para lo que solo tuve en cuenta las variables:altura, especie, diametro_tronco y circ_tronco_cm_cat, 
utilice algoritmo de Random Forest con 600 arboles.

### Resultados obtenidos sobre el conjunto de validación


### Resultados obtenidos en Kaggle

0.685

### Descripción detallada del algoritmo propuesto

Lo primero que realizamos es el 



