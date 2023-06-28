install.packages("git2r")
install.packages("caret")
install.packages("ISLR")
library(git2r)
library(ISLR)
library(caret)
# Cargar el dataset Khan
data(Khan)

# Separar los conjuntos de entrenamiento y prueba
xtrain <- Khan$xtrain
ytrain <- Khan$ytrain
xtest <- Khan$xtest
ytest <- Khan$ytest

#---------------------------Distancia de Mahalanobis-------------------------------------#

  # Calcular la matriz de covarianza del dataset
  cov_matrix <- cov(t(xtrain))
  
  # Calcular la media de cada variable
  means <- colMeans(t(xtrain))
  
  # Calcular la distancia de Mahalanobis para cada observacion
  mahalanobis_dist <- mahalanobis(t(xtrain), center = means, cov = cov_matrix)
  
  # Establecer un umbral para identificar valores atipicos
  threshold <- qchisq(0.95, df = ncol(xtrain))
  
  # Identificar los valores atipicos
  outliers <- which(mahalanobis_dist > threshold)
  
  # Imprimir los Indices de los valores atipicos
  print(outliers)

#------------------------------------------------------------------------------------------#

#-----------------------BUSCAR DESBALANCES-------------------------------------------------#
  
# Calcular el conteo de observaciones por clase
class_counts <- table(ytrain)
  
# Mostrar el conteo de observaciones por clase
print(class_counts)
  
# Calcular la proporción de observaciones por clase
class_proportions <- prop.table(class_counts)
  
# Mostrar la proporción de observaciones por clase
print(class_proportions)
  
# Ajustar el tamaño del área de trazado
pdf("grafico.pdf", width = 10, height = 6)
  
# Ajustar los márgenes de la figura
par(mar = c(5, 5, 4, 2) + 0.1)
  
# Graficar las proporciones de observaciones por clase
barplot(class_proportions, main = "Distribución de Clases en el Dataset Khan", xlab = "Clase", ylab = "Proporción")
  
# Cerrar el archivo PDF
dev.off()


#-------------------------------------------------------------------------------------------------

# Obtener las etiquetas de clase
clases <- unique(ytrain)

# Definir el número de folds para la validación cruzada
k <- 5
distancias <- c("euclidean", "manhattan")

resultados <- list()

for (distancia in distancias) {
  # Realizar validación cruzada
  resultados_distancia <- numeric(k)
  
  for (fold in 1:k) {
    # Dividir los datos en pliegues de entrenamiento y prueba
    fold_indices <- sample(1:length(ytrain), replace = FALSE)
    fold_size <- floor(length(ytrain) / k)
    test_indices <- fold_indices[((fold - 1) * fold_size + 1):(fold * fold_size)]
    train_indices <- fold_indices[!fold_indices %in% test_indices]
    
    # Obtener los conjuntos de entrenamiento y prueba
    xtrain_fold <- xtrain[train_indices, ]
    ytrain_fold <- ytrain[train_indices]
    xtest_fold <- xtrain[test_indices, ]
    ytest_fold <- ytrain[test_indices]
    
    # Obtener las etiquetas de clase únicas en el conjunto de entrenamiento
    clases_train <- unique(ytrain_fold)
    
    # Inicializar una lista para almacenar los centroides
    centroides <- list()
    
    # Calcular los centroides para cada clase en el conjunto de entrenamiento
    for (clase in clases_train) {
      # Filtrar las instancias de la clase actual
      instancias_clase <- xtrain_fold[ytrain_fold == clase, ]
      
      # Calcular el centroide promediando los valores de los atributos
      centroide <- colMeans(instancias_clase)
      
      # Almacenar el centroide en la lista
      centroides[[as.character(clase)]] <- centroide
    }
    
    # Calcular las distancias entre las instancias del conjunto de prueba y los centroides
    distancias <- matrix(NA, nrow = nrow(xtest_fold), ncol = length(clases_train))
    
    for (i in 1:nrow(xtest_fold)) {
      for (j in 1:length(clases_train)) {
        if (distancia == "euclidean") {
          distancias[i, j] <- sqrt(sum((xtest_fold[i, ] - centroides[[as.character(clases_train[j])]])^2))
        } else if (distancia == "manhattan") {
          distancias[i, j] <- sum(abs(xtest_fold[i, ] - centroides[[as.character(clases_train[j])]]))
        }
      }
    }
    
    # Realizar predicciones asignando la clase del centroide más cercano a cada instancia del conjunto de prueba
    clases_predichas <- clases_train[apply(distancias, 1, which.min)]
    
    # Calcular la precisión del modelo en el pliegue actual
    precision_fold <- sum(clases_predichas == ytest_fold) / length(ytest_fold)
    
    # Almacenar los resultados de desempeño en el pliegue actual
    resultados_distancia[fold] <- precision_fold
  }
  
  # Almacenar los resultados de desempeño para la distancia actual en la lista general de resultados
  resultados[[as.character(distancia)]] <- resultados_distancia
}

# Calcular la precisión promedio para cada distancia
precision_promedio <- sapply(resultados, mean)
print(precision_promedio)
# Obtener la mejor distancia (aquella con la precisión promedio más alta)
mejor_distancia <- names(precision_promedio)[which.max(precision_promedio)]
print(mejor_distancia)

#--------------------------------PREDICCIÓN EN CONJUNTO DE TEST------------------------------------------------------
# Obtener los centroides para la mejor distancia utilizando todos los datos de entrenamiento
centroides_nuevos <- list()
clases_train_nuevas <- unique(ytest)

for (clase in clases_train_nuevas) {
  # Filtrar las instancias de la clase actual
  instancias_clase_nuevas <- xtest[ytest == clase, ]
  
  # Calcular el centroide promediando los valores de los atributos
  centroide <- colMeans(instancias_clase_nuevas)
  
  # Almacenar el centroide en la lista
  centroides_nuevos[[as.character(clase)]] <- centroide
}

distancias_nuevos <- matrix(NA, nrow = nrow(xtest), ncol = length(clases_train))

for (i in 1:nrow(xtest)) {
  for (j in 1:length(clases_train_nuevas)) {
    if (mejor_distancia == "euclidean") {
      distancias_nuevos[i, j] <- sqrt(sum((xtest[i, ] - centroides[[as.character(clases_train_nuevas[j])]])^2))
    } else if (mejor_distancia == "manhattan") {
      distancias_nuevos[i, j] <- sum(abs(xtest[i, ] - centroides[[as.character(clases_train_nuevas[j])]]))
    }
  }
}

# Realizar predicciones asignando la clase del centroide más cercano a cada instancia de los datos nuevos
clases_predichas_nuevos <- clases_train_nuevas[apply(distancias_nuevos, 1, which.min)]

# Calcular la precisión en los nuevos datos
precision_nuevos <- sum(clases_predichas_nuevos == ytest) / length(ytest)

# Imprimir la precisión en los nuevos datos
print(precision_nuevos)

# Convertir clases_predichas_nuevos y ytest a factores con los mismos niveles
clases_predichas_nuevos <- factor(clases_predichas_nuevos, levels = unique(c(clases_predichas_nuevos, ytest)))
ytest <- factor(ytest, levels = unique(c(clases_predichas_nuevos, ytest)))


# Calcular la matriz de confusión
confusionMatrix(clases_predichas_nuevos, ytest)
cm <- confusionMatrix(clases_predichas_nuevos, ytest)
print(cm)
