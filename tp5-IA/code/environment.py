import numpy as np
import random


class Enviroment:
  # 0  caminos disponibles
  # 1  obstaculos
  # 2  posicion incial
  # 3  posicion final
  paso = 0
  point = 0

  def __init__ (self,sizeX,sizeY):
    self.sizeX = sizeX
    self.sizeY = sizeY
    self.matriz = np.zeros((sizeX,sizeY))
    tamaño = sizeX*sizeY
    self.reinas = []


    for i in range (0,self.sizeY):
      j = random.randint(0,sizeX-1)
      if (self.matriz[i][j] == 0):
        self.matriz[i][j] = 1
      self.reinas.append(j)
  
  def recalculo_reinas(self):

    reinasVecinas=[]
    for i in range (0,self.sizeY):
      j = random.randint(0,self.sizeX-1)
      if (self.matriz[i][j] == 0):
        self.matriz[i][j] = 1
      reinasVecinas.append(j)
    return reinasVecinas
    
  def print_environment(self):
    for a in range(0,self.sizeX):
      for b in range(0,self.sizeY):
        print("|",int(self.matriz[a][b]),end=' ')
      print("|")
