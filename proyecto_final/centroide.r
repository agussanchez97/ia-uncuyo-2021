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


# Obtener las etiquetas de clase
clases <- unique(ytrain)


# Inicializar una lista para almacenar los centroides
centroides <- list()

# Calcular los centroides para cada clase
for (clase in clases) {
  # Filtrar las instancias de la clase actual
  instancias_clase <- xtrain[ytrain == clase, ]
  
  # Calcular el centroide promediando los valores de los atributos
  centroide <- colMeans(instancias_clase)
  print(centroide)
  # Almacenar el centroide en la lista
  centroides[[as.character(clase)]] <- centroide
}
print(centroides)

distancias <- matrix(NA, nrow = nrow(xtest), ncol = length(clases))

for (i in 1:nrow(xtest)) {
  for (j in 1:length(clases)) {
    # Calcular la distancia euclidiana entre la observación y el centroide
    distancias[i, j] <- sqrt(sum((xtest[i, ] - centroides[[as.character(clases[j])]])^2))
  }
}

clases_predichas <- clases[apply(distancias, 1, which.min)]

# Convertir las variables a factores con los mismos niveles
clases_predichas <- factor(clases_predichas, levels = unique(c(clases_predichas, ytest)))
ytest <- factor(ytest, levels = unique(c(clases_predichas, ytest)))

# Calcular la matriz de confusión
confusionMatrix(clases_predichas, ytest)
cm <- confusionMatrix(clases_predichas, ytest)
print(cm)
