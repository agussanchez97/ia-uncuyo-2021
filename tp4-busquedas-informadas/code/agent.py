import queue
import node
import environment
import heapq


class Agent:           
  def __init__(self,env): #recibe como parámetro un objeto de la clase Environment
    self.env=env
    self.posX=env.init_posX
    self.posY=env.init_posY
    self.a_estrella()

  # esta funcion no contempla los obstaculos , solo mide distancias entre las posicion actual y el objetivo
  def h(self,Node,x,y):

    filas = abs(self.env.finalX-x)  #cantidad de pasos en x
    columnas = abs(self.env.finalY-y)  #cantidad de pasos en y

    pasos = filas + columnas #cantidad de pasos totales 
    return pasos

  #funcion que calcula f como g (coste) + h (heuristica)
  def f(self,Node):

    f = Node.g + Node.h
    return f


  def a_estrella(self):

    self.env.print_environment()
    #acciones
    movimientox=[1,-1,0,0] #movimiento agente :arriba abajo
    movimientoy=[0,0,-1,1] #movimiento agente: derecha izquierda
    
    explorado= []
    
    inicial=node.Node((self.posX,self.posY),1,None,None) #nodo inicial
    inicial.h= self.h(inicial,self.posX,self.posY) #calculo heuristica
    inicial.f = self.f(inicial) #calculo f
    frontera = []
    frontera.append(inicial)

    while len(frontera) != 0:
      
      posicion = self.env.popPriority(frontera) #devuelve la posicion del nodo que tiene la menor f
      actual = frontera.pop(posicion) #saca el nodo

      self.posX = actual.estado[0]
      self.posY = actual.estado[1]

      explorado.append(actual)
  #evalua acciones y calcula h y f para todos los nodos frontera (vecinos del nodo actual)
      for i in range(0,4):
       
        nuevox = self.posX + movimientox[i]
        nuevoy = self.posY + movimientoy[i]

        if (nuevox >= 0 and nuevox < self.env.sizeX and nuevoy >= 0 and nuevoy < self.env.sizeY):
 
          
          if self.env.matriz[nuevox][nuevoy] != 1:
     
            nuevo=node.Node((nuevox,nuevoy),1,None,None)
            nuevo.h= self.h(nuevo,nuevox,nuevoy)
            nuevo.f = self.f(nuevo)

            if self.env.search(explorado,nuevo) == False and self.env.search(frontera,nuevo) == False:
             
              if nuevo.estado == (self.env.finalX,self.env.finalY):
                print("Camino encontrado")
                print(self.env.imprimir(explorado))
                print(len(explorado))
                return 
            
              else:
                frontera.append(nuevo)

    return print("camino no encontrado")
