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
#constructor
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
#agrega los obstaculos

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
#devuelve la posicion del nodo q tiene la f menor
  
  def popPriority(self,linkedlist):
    min=100000
    
    for i in range(0,len(linkedlist)):
      if linkedlist[i].f < min:
        min = linkedlist[i].f
        Nodo=linkedlist[i]
        pos = i

    return pos

  
		
