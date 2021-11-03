install.packages("readr")
install.packages("dplyr")
install.packages("caret")
install.packages("randomForest")
install.packages("rpart")
library(rpart)
library(randomForest)
library(readr)
library(dplyr)
library(caret)

# Leer los datos
arbolado_train <-read_csv("C:/Users/Agustina/Downloads/arbolado-mza-dataset.csv")
arbolado_test <-read_csv("C:/Users/Agustina/Downloads/arbolado-mza-dataset-test.csv")



#mutar los 1 y 0 por si o no , de la clase inclinacion peligrosa
arbolado_train<-arbolado_train %>% mutate(inclinacion_peligrosa=ifelse(inclinacion_peligrosa=='1','si','no'))

#definir la clase inclinacion peligrosa como factor
arbolado_train$inclinacion_peligrosa <-as.factor(arbolado_train$inclinacion_peligrosa)

arbolado_train %>%  group_by(inclinacion_peligrosa) %>% summarise(total=n())

#agregar una variable mas en base a la variable circ_tronco_cm para tener mas informacion para entrenamiento
arbolado_train <- arbolado_train %>% mutate(circ_tronco_cm_cat= ifelse(`circ_tronco_cm`<=100,'bajo',
                                                                         ifelse(`circ_tronco_cm`>100 & `circ_tronco_cm` <= 200, 'medio',
                                                                                ifelse(`circ_tronco_cm` > 200 & `circ_tronco_cm` <= 300, 'alto','muy alto'))))
arbolado_test <- arbolado_test %>% mutate(circ_tronco_cm_cat= ifelse(`circ_tronco_cm`<=100,'bajo',
                                                                       ifelse(`circ_tronco_cm`>100 & `circ_tronco_cm` <= 200, 'medio',
                                                                              ifelse(`circ_tronco_cm` > 200 & `circ_tronco_cm` <= 300, 'alto','muy alto'))))



#balancer el dataset , eliminando casos de arboles SIN inclinacon peligrosa(clase mayoritaria): peligro perder demasiada informacion
data_train_down<-downSample(arbolado_train,arbolado_train$inclinacion_peligrosa)
data_train_down %>%group_by(inclinacion_peligrosa) %>% summarise(total=n())


set.seed(950)

#entreno con random forest
mod <- randomForest(inclinacion_peligrosa ~ altura+especie+diametro_tronco+circ_tronco_cm_cat,data = data_train_down,importance=TRUE,ntree = 500)
mod

#calculo la prediccion
pred <- predict(mod,arbolado_test,type = "prob")
head(pred)

#guardo el dataset como lo pide kaggle
preds_tree<-ifelse(pred[,2] >=0.4,1,0)
submission<-data.frame(id=arbolado_test$id,inclinacion_peligrosa=pred)
readr::write_csv(submission,"resultsfinal.csv")
results <- read_csv("C:/Users/Agustina/Documents/results.csv")
results<- results %>% mutate(inclinacion_peligrosa=ifelse(inclinacion_peligrosa=='si','1','0'))
readr::write_csv(results,"resultsfinal.csv")

