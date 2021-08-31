## Trabajo Practico n°3

#### B) Ejecutar un total de 30 veces cada algoritmo en un escenario aleatorio, calcular la media y la desviación estándar de la cantidad de estados explorados para llegar al destino
#### (si es que fue posible). Presentar los resultados en un gráfico de barras.

Los resultados fueron evaluados con un 40% de obstaculos.

##### BFS
Media : 3251.133333
Desviacion estandar: 1254.748436

##### DFS
Media : 3087.2
Desviacion estandar: 1161.949948

##### Busqueda uniforme

Media:3164.466667
Desviacion estandar: 1105.259331


#### Graficos

![image](https://user-images.githubusercontent.com/82063987/131420851-4ce4e37c-f2b4-41b2-b9e7-bcace3f53214.png)

![image](https://user-images.githubusercontent.com/82063987/131420873-36f51eff-d29d-49d4-9da7-9c35eb9c4f20.png)

#### C)  Cuál de los 3 algoritmos considera más adecuado para resolver el problema planteado en A)?. Justificar la respuesta.

Elegiria BFS porque a pesar de que no siempre es optimo , es completo , si los slots tuvieran costos elegiria Busqueda uniforme , ya que primeramente es el algoritmo que me permite 
medir la ruta con menor costo y a demas segun su desviacion estandar siempre los resultados dan cerca de la media. Con respecto al DFS no lo eligiria porque a pesar de sus 
valores son mejores que los otros dos , no siempre encuentra el camino y no es completo, depende mucho del limite que le pasemos.


