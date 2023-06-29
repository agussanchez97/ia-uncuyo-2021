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

# Entrenar el modelo GLMNET con validación cruzada
model <- glmnet(xtrain, ytrain, family = "multinomial")

# Obtener el valor óptimo de lambda
lambda_min <- model$lambda.min

# Realizar predicciones en el conjunto de prueba
predictions <- predict(model, newx = xtest, s = lambda_min, type = "class")


# Evaluar la precisión del modelo
accuracy <- mean(predictions == ytest)
print(accuracy)

# Convertir las variables a factores con los mismos niveles
predictions <- factor(predictions, levels = unique(c(predictions, ytest)))
ytest <- factor(ytest, levels = unique(c(predictions, ytest)))

# Calcular la matriz de confusión
confusionMatrix(predictions, ytest)
cm <- confusionMatrix(predictions, ytest)
print(cm)



