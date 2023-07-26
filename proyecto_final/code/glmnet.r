# Instalar paquetes
install.packages("git2r")
install.packages("stringi")
install.packages("caret")
install.packages("ISLR")
install.packages("glmnet")
install.packages("MLmetrics")
install.packages("pROC")

# Cargar paquetes
library(git2r)
library(ISLR)
library(caret)
library(glmnet)
library(MLmetrics)
library(pROC)

# Cargar el dataset Khan
data(Khan)

# Separar los conjuntos de entrenamiento y prueba
xtrain <- Khan$xtrain
ytrain <- Khan$ytrain
xtest <- Khan$xtest
ytest <- Khan$ytest
print(xtrain) # matriz num 63x2308. columna: variable, fila: observación
print(ytrain) # vector num 63. contiene las etiquetas de clase
print(xtest) # matriz num 20x2308.
print(ytest) # vector num 20.

# Contar ocurrencias
frecuencias <- table(ytrain)
print(frecuencias)

# Entrenar el modelo GLMNET
model <- glmnet(xtrain, ytrain, family = "multinomial")

# Variacion del parametro standardize -------------------------------------
model <- glmnet(xtrain, ytrain, family = "multinomial", standardize = FALSE)

# Realizar predicciones en el conjunto de prueba
predictions <- predict(model, newx = xtest, type = "class")

# Evaluar la precisión del modelo
accuracy <- mean(predictions == ytest)
print(accuracy)

# Convertir las variables a factores con los mismos niveles
predictions <- factor(predictions, levels = unique(c(predictions, ytest)))
ytest <- factor(ytest, levels = unique(c(predictions, ytest)))
print(predictions)
print(ytest)

# Calcular la matriz de confusión
confusionMatrix(predictions, ytest)
cm <- confusionMatrix(predictions, ytest)
print(cm)