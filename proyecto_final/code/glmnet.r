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
str(Khan)

# Separar los conjuntos de entrenamiento y prueba
xtrain <- Khan$xtrain
ytrain <- Khan$ytrain
xtest <- Khan$xtest
ytest <- Khan$ytest
str(xtrain)
str(ytrain)
str(xtest)
str(ytest)

# Definir una secuencia de valores de lambda
lambda_values <- 10^seq(-2, 2, by = 0.5)
print(lambda_values)

# Lista para almacenar los resultados
results <- list()

# Implementar el algoritmo de GLMNET para cada valor de lambda
for (lambda in lambda_values) {
  model <- glmnet(xtrain, ytrain, family = "multinomial", lambda = lambda)
  results[[as.character(lambda)]] <- model
}

# Obtener los resultados y encontrar el mejor valor de lambda
best_accuracy <- -Inf
best_lambda <- NULL
for (lambda in lambda_values) {
  model <- results[[as.character(lambda)]]
  predictions <- predict(model, newx = xtest, type = "class")
  mean_accuracy <- mean(predictions == ytest)
  print(mean_accuracy)
  if (mean_accuracy > best_accuracy) {
    best_accuracy <- mean_accuracy
    best_lambda <- lambda
  }
}
print(best_accuracy)
print(best_lambda)
# Entrenar el modelo GLMNET con el mejor valor de lambda
best_model <- glmnet(xtrain, ytrain, family = "multinomial", lambda = best_lambda)

# Realizar predicciones en el conjunto de prueba
predictions <- predict(best_model, newx = xtest, type = "class")

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

# Otras metricas
tp <- cm$table[2, 2]  # Verdaderos positivos
fn <- cm$table[2, 1]  # Falsos negativos
tn <- cm$table[1, 1]  # Verdaderos negativos
fp <- cm$table[1, 2]  # Falsos positivos
print(tp)
print(fn)
print(tn)
print(fp)

# Calcula la sensibilidad (recall)
sensitivity <- tp / (tp + fn)
print(sensitivity)

# Calcula la especificidad
specificity <- tn / (tn + fp)
print(specificity)

# Calcula la precisión
precision <- tp / (tp + fp)
print(precision)

# Calcula el F1-score
f1_score <- 2 * (precision * sensitivity) / (precision + sensitivity)
print(f1_score)

# Calcula la curva ROC
roc <- roc(ytest, as.numeric(predictions))
print(roc)
plot(roc)
