import numpy as np
import random
import node
import queue

class Enviroment:
  # 0  caminos disponibles
  # 1  obstaculos
  # 2  posicion incial
  # 3  posicion final
  paso = 0
  point = 0
  #constructor del entorno
  def __init__ (self,sizeX,sizeY,init_posX,init_posY,finalX,finalY,obstaculos):
    self.sizeX = sizeX
    self.sizeY = sizeY
    self.matriz = np.zeros((sizeX,sizeY))
    tamaño = sizeX*sizeY
    self.init_posX = init_posX
    self.init_posY = init_posY
    self.finalX=finalX
    self.finalY=finalY
    self.obstaculos = obstaculos

#bucle q genera el los obstaculos del entorno de forma aleatoria
    cleanAmountSlot=0
    while (cleanAmountSlot < self.obstaculos):
      i = random.randint(0,sizeX-1)
      j = random.randint(0,sizeY-1)
      if (self.matriz[i][j] == 0):
        self.matriz[i][j] = 1
      cleanAmountSlot=cleanAmountSlot+1

    self.matriz[init_posX][init_posY] = 2
    self.matriz[finalX][finalY] = 3


  def print_environment(self):
    for a in range(0,self.sizeX):
      for b in range(0,self.sizeY):
        print("|",int(self.matriz[a][b]),end=' ')
      print("|")

  #busca un nodo en una lista
  def search(self,LinkedList,Node):

    for i in range(0,len(LinkedList)):

      if LinkedList[i].estado == Node.estado:
        return True
    return False
  def imprimir (self,LinkedList):
    z=[]
    if LinkedList == None:
      print("None")
    else:
      i=0
      print("La lista es:")
      print("[",end="")
      for i in range(0,len(LinkedList)):
        print(LinkedList[i].estado,end=",")
      print("]")

  def searchQ(self,LinkedList,Node):
    i=0  
    while len(LinkedList) != 0:
      print("QUEDAAAAAAAA")
      tupla= LinkedList[i]
      if tupla[1].estado == Node.estado:
        return True
      i=i+1
    return False
  def imprimirQ (self,LinkedList):
    z=[]
    if LinkedList == None:
      print("None")
    else:
      i=0
      print("La lista es:")
      print("[",end="")
      print(LinkedList.qsize())
      for i in range(0,LinkedList.qsize()):
        node = LinkedList[i]
        print(nodo.estado,end=",")
        i= i+1     
      print("]")
  
  #busca el nodo de mayor prioridad
  def popPriority(self,linkedlist):
    max=0

    for i in range(0,len(linkedlist)):
      
      if linkedlist[i].costo > max:
        max = linkedlist[i].costo
        Nodo=linkedlist[i]
        pos = i
    


    return i
