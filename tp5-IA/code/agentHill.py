import random 
import environment
from datetime import datetime
import random, time, math


class Agent:           
  def __init__(self,env): #recibe como parámetro un objeto de la clase Environment
    self.env=env
    self.vecinomejor = True
    self.elapsedTime = 0
    self.startTime = datetime.now()
    
    self.Queens()
    

  def h(self,status):
      num = 0
      for i in range(len(status)):
        for j in range(i + 1,len(status)):
 
          if status[i] == status[j]:
            num += 1
          offset = j - i
          if abs(status[i]-status[j]) == offset:
            num += 1
      return num  

  def hill_climbing(self,status):

    diccionario={}
    for i in range(len(status)): #columnas
      best_vecino = status[i]

      for filas in range(len(status)):
        
        if status[i] == filas : #si el estado actual es la posicion actual de la reina
          continue
        
        status_copia = list(status)
        #movimientos de reinas
        status_copia[i] = filas
        diccionario[(i,filas)] = self.h(status_copia)

    recorrido = []
    amenazas_actuales= self.h(status)
    vecinomejor = 0
    for key,valor in diccionario.items():

      if amenazas_actuales > valor:
        vecinomejor = vecinomejor + 1
        amenazas_actuales = valor 

    if vecinomejor == 0 and amenazas_actuales > 0:
  
      self.vecinomejor = False
      return status

        
    
    for key,valor in diccionario.items():

      if valor == amenazas_actuales:

        recorrido.append(key)

    print(recorrido)

    if len(recorrido) > 0 :

      x = random.randint(0,len(recorrido)-1)
      i = recorrido[x][0]
      filas = recorrido[x][1]
      status[i] = filas
 
    return status

  def Queens(self):
        #status= [0,1,2,3,4,5,6,7]
        status = self.env.reinas # estado inical
        print(status)
 
        # Cuando el número de conflictos es mayor que 0, el mejor sucesor se resuelve cíclicamente hasta que se encuentren las ocho soluciones reina
        paso = 0
        while self.h(status) > 0 and paso < 10000 and self.vecinomejor == True:
                
                status = self.hill_climbing(status)
                print (status)
                print (self.h(status))
                paso = paso +1
        if self.vecinomejor == False:
          print("No se encontro solucion")
          print(status)
          print(self.h(status))
          self.elapsedTime = self.getElapsedTime()
          print("Unsuccessful, Elapsed Time: %sms" % (str(self.elapsedTime)))


        else:
          print ("Se encontro solucion")
          print (status)
          self.elapsedTime = self.getElapsedTime()
          print("Success, Elapsed Time: %sms" % (str(self.elapsedTime)))


  def getElapsedTime(self):
    endTime = datetime.now()
    elapsedTime = (endTime - self.startTime).microseconds / 1000
    return elapsedTime



    
