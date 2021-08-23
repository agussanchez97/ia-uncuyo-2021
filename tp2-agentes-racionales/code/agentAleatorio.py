import enviroment
import random

class Agent:           
  def __init__(self,env): #recibe como parámetro un objeto de la clase Environment
    self.env=env
    self.posX=env.init_posX
    self.posY=env.init_posY
    self.think(env)


  def arriba(self):
    pos = self.env.accept_actions("arriba",self.posX,self.posY)
    if pos == True :
      self.env.matrizP[self.posX][self.posY]= 0
      self.posX = self.posX - 1
      self.env.matrizP[self.posX][self.posY]= 2
      return True
    return False

  def abajo(self):
    pos = self.env.accept_actions("abajo",self.posX,self.posY)
    if pos == True :
      self.env.matrizP[self.posX][self.posY]= 0
      self.posX = self.posX + 1
      self.env.matrizP[self.posX][self.posY]= 2
      return True
    return False

  def derecha(self):
    pos = self.env.accept_actions("derecha",self.posX,self.posY)
    if pos == True :
      self.env.matrizP[self.posX][self.posY]= 0
      self.posY = self.posY + 1
      self.env.matrizP[self.posX][self.posY]= 2
      return True
    return False

  def izquierda(self):
    pos = self.env.accept_actions("izquierda",self.posX,self.posY)
    if pos == True :
      self.env.matrizP[self.posX][self.posY]= 0
      self.posY = self.posY - 1
      self.env.matrizP[self.posX][self.posY]= 2
      return True
    return False
  
  def aspira (self):
    self.env.accept_actions("Limpiar",self.posX,self.posY)

  def idle(self): # no hace nada
    self.env.accept_actions("nada",self.posX,self.posY)

  def think(self,env): # implementa las acciones a seguir por el agente
    print("Comienzo: ")
    print("Entorno creado: ")
    print(" ")
    print("Slot Sucios: 1 - Slot limpio: 0 ")
    print(" ")
    self.env.print_environment()
    print("Aspiradora: ")
    self.env.print_environmentM()

    print("............................................")
    while (self.env.paso < 1000):
      print("Aspiradora esta en la posicion X=", self.posX , "Y=", self.posY,".")

      accion=random.randint(1,6)
      if (accion == 1):
          movimiento = self.idle()
          print("La siguiente accion es : ")
          print ("Aspiradora no hace nada.")
          print("Posición de la aspiradora")
          self.env.print_environmentM()
      elif (accion ==2):
          
        movimiento = self.arriba()
        if movimiento == True:
            print("La siguiente accion es : ")
            print("Aspiradora se mueve hacia arriba.")
            print("Posición de la aspiradora")
            self.env.print_environmentM()
        else:
            print("Movimiento invalido- No se puede ir hacia arriba desde la posicion X=",self.posX,"Y=",self.posY)
      elif (accion ==3):
          
        movimiento = self.abajo()
        if movimiento == True:
            print("La siguiente accion es : ")
            
            print("Aspiradora se mueve hacia abajo.")
            print("Posición de la aspiradora")
            self.env.print_environmentM()
            print("------------------------------")
        else:
            print("Movimiento invalido- No se puede ir hacia abajo desde la posicion X=",self.posX,"Y=",self.posY)
            print("------------------------------")
      elif (accion== 4):
          
        movimiento = self.derecha()
        if movimiento == True:
            print("La siguiente accion es : ")
            
            print("Aspiradora se mueve hacia derecha.")
            print("Posición de la aspiradora")
            self.env.print_environmentM()
            print("------------------------------")
            
        else:
            print("Movimiento invalido- No se puede ir a la derecha desde la posicion X=",self.posX,"Y=",self.posY)
            print("------------------------------")
      elif (accion== 5):
          
        movimiento =self.izquierda()
        if movimiento == True:
          print("La siguiente accion es : ")
            
          print("Aspiradora se mueve hacia izquierda.")
          self.env.print_environmentM()
          print("------------------------------")  
        else:
          print("Movimiento invalido- No se puede ir a izquierda desde la posicion X=",self.posX,"Y=",self.posY)
          print("------------------------------")
      elif (accion == 6):

        movimiento= self.aspira()
        
        print("La siguiente accion es: ")
        print("Aspiradora Limpia.")
        self.env.print_environmentM()
        print("------------------------------")
        
    print("la CANTIDAD DE PUNTO DE LA ASPIRADORA ES: ",self.env.point)
    print("El desempeño de la aspiradora en entorno de ",self.env.sizeX,"x",self.env.sizeY," con porcentaje de suciedad en el ambiente de ",self.env.dirt_rate ,"% es:" , self.env.get_performance())   


      
