#esta libreria permite trabajar con matrices.
import numpy as np
import random

class Enviroment:
  # 0  limpio
  # 1  sucio
  # 2  aspirador
  paso = 0
  point = 0

  def __init__ (self,sizeX,sizeY,init_posX,init_posY,dirt_rate):
    self.sizeX = sizeX
    self.sizeY = sizeY
    self.matriz = np.zeros((sizeX,sizeY))
    self.matrizP= np.zeros((sizeX,sizeY))
    tamaño = sizeX*sizeY
    self.init_posX = init_posX
    self.init_posY = init_posY
    self.dirt_rate= dirt_rate
    self.dirtSlotsAmount = (dirt_rate * tamaño)/100
    self.matrizP[init_posX][init_posY] = 2

    for i in range (0,sizeX):
      for j in range(0,sizeY):
        self.matriz[i][j] = 0

    cleanAmountSlot=0
    while (cleanAmountSlot < self.dirtSlotsAmount):
      i = random.randint(0,sizeX-1)
      j = random.randint(0,sizeY-1)
      if (self.matriz[i][j] == 0):
        self.matriz[i][j] = 1
      cleanAmountSlot=cleanAmountSlot+1

  def accept_actions(self,action,posX,posY):
    if (action == "izquierda"):
      if ( posY-1 >= 0 ):
        self.paso = self.paso + 1
        return True
      return False
    elif (action == "derecha"):
      if (posY+1 < self.sizeY):
        self.paso = self.paso + 1
        return True
      return False
    elif (action == "arriba"):
      if (posX-1 >= 0):
        self.paso = self.paso + 1
        return True
      return False
    elif (action == "abajo"):
      if (posX+1 < self.sizeX ):
        self.paso = self.paso + 1
        return True
      return False

    elif (action == "Limpiar"):
      if (self.matriz[posX][posY] == 1):
        self.paso = self.paso + 1
        self.point= self.point + 1
        self.matriz[posX][posY] = 0

    else:
      self.paso = self.paso + 1

  def get_performance(self):
    return self.point/self.paso

  def print_environment(self):
    for a in range(0,self.sizeX):
      for b in range(0,self.sizeY):
        print("|",int(self.matriz[a][b]),end=' ')
      print("|")

  def print_environmentM(self):
    for a in range(0,self.sizeX):
      for b in range(0,self.sizeY):
        print("|",int(self.matrizP[a][b]),end=' ')
      print("|")
  


