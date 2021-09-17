import numpy as np
import random
import operator
from datetime import datetime
import random, time, math
from itertools import islice


  

def genera_cromosomas(poblacion,n):
  #reinas = np.zeros((poblacion,n))
  
  reinas = []
  
  for i in range(0,poblacion):
    reina=[]
    for j in range(0,n):
      x = random.randint(0,n-1)
      
      while (x in reina):
        
        
        x=random.randint(0,n-1)
      reina.append(x)
    reinas.append(reina)  
  #for i in range(0,poblacion):
    #for j in range(0,n):
      #x =   random.randint(0,n)
      #reinas[i][j]= x

  return reinas



def h(status):
      num = 0
      for i in range(len(status)):
        for j in range(i + 1,len(status)):
          if status[i] == status[j]:
            num += 1
          offset = j - i
          if abs(status[i]-status[j]) == offset:
            num += 1
      return num 

def fitness(reinas,n,poblacion):
    max_ataques= n * (n-1)/2
    diccionario = {}
    fitnesstotal=0
    for i in range(len(reinas)):
      num = 0
      arr=reinas[i]
      num = h(arr)

    #for i in range(0,poblacion):
      #num = 0
      #for j in range(0,n):
        #for k in range(j+1,n):
          #if reinas[i][j] == reinas[i][j]:
            #num += 1
          #if abs(reinas[i][j]-reinas[i][k]) == k - j:
            #num += 1

      
      fitnesstotal= fitnesstotal + (max_ataques-num)
      diccionario[(i)] = max_ataques-num

    return diccionario
    
    

def seleccion(diccionario):
  seleccionado = sorted(diccionario.items(),key=operator.itemgetter(1),reverse = False)


  mitad = len(diccionario) //2
  seleccionado =seleccionado[mitad:]

  return seleccionado




def crossover(reinas,n,poblacion,seleccionado,diccionario):
  cruze = random.randint(1,n-1)

  eliminar=[]
  for key,value in diccionario.items():

    if ((key,value) in seleccionado) == False:
      eliminar.append(key)
      
  eliminar.sort(reverse=True)

  for i in range(len(eliminar)):
    reinas.pop(eliminar[i])



  
  for i in range(0,len(reinas)-1,2):

    arr=reinas[i]
    arr2=reinas[i+1]
    agrego = arr[0:cruze]
    arr[0:cruze]=arr2[0:cruze]
    arr2[0:cruze]= agrego
    
  #for i in range(0,poblacion,2):
    #arr=np.array(reinas)
    #agrego= arr[i,0:cruze]
    #arr[i,0:cruze] = arr[i+1,0:cruze]
    #arr[i+1,0:cruze] = agrego
  return reinas

def mutacion (reinas,n):
  muta = random.randint(0,len(reinas)-1)
  x=random.randint(0,n-1)
  for i in range(0,len(reinas)//2):
    arr=reinas[i]
  
    arr[x] = x
  return reinas

def principal(poblacion,n):
  elapsedTime = 0
  startTime = datetime.now()
  solution = False
  print("Poblacion")
 
  reinas = genera_cromosomas(poblacion,n)
  print(reinas)
  
  paso = 0
  for i in range(0,1000):
    diccionario = fitness(reinas,n,poblacion)

    if 28 in diccionario.values():
      
      print("Encontro la solucion")
      for key,value in diccionario.items():
        if value == 28:
          print(reinas[key])
          elapsedTime = getElapsedTime(startTime)
          print("Success, Elapsed Time: %sms" % (str(elapsedTime)))
          print(paso)
          solution = True
          return
    seleccionados =seleccion(diccionario)

    reinas=crossover(reinas,n,poblacion,seleccionados,diccionario)

    reinas = mutacion(reinas,n)
  if solution == False :
    print("No se encontro solucion")
    elapsedTime = getElapsedTime(startTime)
    print("Unsuccessful, Elapsed Time: %sms" % (str(elapsedTime)))
    
def getElapsedTime(startTime):
    endTime = datetime.now()
    elapsedTime = (endTime - startTime).microseconds / 1000
    return elapsedTime




    

    



