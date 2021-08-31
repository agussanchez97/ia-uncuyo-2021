import queue
import node
import enviroment
import heapq


class Agent:           
  def __init__(self,env): #recibe como parámetro un objeto de la clase Environment
    self.env=env
    self.posX=env.init_posX
    self.posY=env.init_posY
    #self.BFS()
    #self.busqueda_profundida_limitada(9999)
    self.busqueda_uniforme()

#Algoritmo de busqueda en anchura

  def BFS(self):
    self.env.print_environment()
    movimientox=[1,-1,0,0] # movimiento izquierda - derecha
    movimientoy=[0,0,-1,1] # moviento arriba - abajo
    inicial = (self.posX,self.posY) # estado inicial del agente
    cola =[] # frontera
    cola.append(inicial) # es una pila de estados 
    visitados = [] # slots explorados
    
    # mientras la frontera tenga estados por visitar o no se llegue al estado deseado.

    while len(cola) != 0 :
     
      # sacar el estado de la cola
      actual = cola.pop()

      #posicionamos el agente
      self.posX = actual[0]
      self.posY = actual[1]
      
      #parada si llega al estado final
      if actual == (self.env.finalX,self.env.finalY):

        print("Camino encontrado")
        print(len(visitados))
        return print(visitados)
       
      
      visitados.append(actual)

      # bucle para probar todas las accines: arriba , abajo , izquierda , derecha
      for i in range(0,4):
        
        #calcula la nuevas posiciones , si se realizaran las acciones
        nuevox = self.posX + movimientox[i]
        nuevoy = self.posY + movimientoy[i]

        #prueba q las posiciones sean paredes
        if (nuevox >= 0 and nuevox < self.env.sizeX and nuevoy >= 0 and nuevoy < self.env.sizeY):
          nuevo = (nuevox,nuevoy)
          #prueba que el estado al que se va a mover no sea un obstaculo
          if self.env.matriz[nuevox][nuevoy] != 1:
            
            #prueba que el estado no este en los visitados y tampoco en la frontera
            if nuevo not in visitados and nuevo not in cola:
              
              if nuevo == (self.env.finalX,self.env.finalY):
                print(len(visitados))
                print("Camino encontrado")
                print(visitados)
                return 
              else:
                cola.append((nuevox,nuevoy))
    
          
    return print("Camino no encontrado")

  #---------------------------------------------------------------   
  #ALGORITMO : profundidad limitada
  #recibe el limite para saber con que profundidad se puede buscar
  def busqueda_profundida_limitada (self,limite):
    #imprime el entorno
    self.env.print_environment()

    #pila de explorados
    explorado = []
  
    actual = node.Node((self.posX,self.posY),1)
    #acciones : arriba , abajo, izquierda , derecha
    movimientox=[1,-1,0,0]
    movimientoy=[0,0,-1,1]

    #pila LIFO
    frontera = []
    frontera.append(actual)
    #contador para medir la profundidad
    profundidad = 0
    while len(frontera) > 0 :
      
      actual = frontera.pop(len(frontera)-1)
      self.posX = actual.estado[0]
      self.posY = actual.estado[1]
      #condicion de parada si encuentra el camino
      if actual.estado == (self.env.finalX,self.env.finalY):
        print("Camino encontrado")
        return print(explorado)

      #si llega a la profundidad , vuelve a otro nodo de la frontera
      if profundidad > limite :
          if len(frontera) > 0 :
            actual= frontera.pop(len(frontera)-1)
            self.posX = actual.estado[0]
            self.posY = actual.estado[1]
          else:
            return print("camino no encontrado")
      explorado.append(actual)
      profundidad = profundidad + 1

      #bucle para evaluar las acciones 
      for i in range(0,4):

        nuevox = self.posX + movimientox[i]
        nuevoy = self.posY + movimientoy[i] 

        if (nuevox >= 0 and nuevox < self.env.sizeX and nuevoy >= 0 and nuevoy < self.env.sizeY):
        
          nuevo = node.Node((nuevox,nuevoy),1)

          if self.env.matriz[nuevox][nuevoy] != 1:
            
            if self.env.search(explorado,nuevo) == False and self.env.search(frontera,nuevo) == False :
              
              if nuevo.estado == (self.env.finalX,self.env.finalY):
                print("Camino encontrado")
                print(len(explorado))
                return self.env.imprimir(explorado)
              else:
                frontera.append(nuevo)
    return print("camino no encontrado")


  #ALGORITMO : busqueda uniforme

  def busqueda_uniforme(self):
    self.env.print_environment()
    movimientox=[1,-1,0,0]
    movimientoy=[0,0,-1,1]
    explorado= []
    actual=node.Node((self.posX,self.posY),1)
    frontera = []
    frontera.append(actual)
    i=0
    
    while len(frontera) > 0  :
      

      nodo=self.env.popPriority(frontera)
      actual= frontera.pop(nodo)

      self.posX = actual.estado[0]
      self.posY = actual.estado[1]
      
      if actual.estado == (self.env.finalX,self.env.finalY):

        print("Camino encontrado")
        print(len(explorado))
        return self.env.imprimir(explorado)
       
      
      explorado.append(actual)

      for i in range(0,4):

        nuevox = self.posX + movimientox[i]
        nuevoy = self.posY + movimientoy[i]

        if (nuevox >= 0 and nuevox < self.env.sizeX and nuevoy >= 0 and nuevoy < self.env.sizeY):
          
          
          nuevo = node.Node((nuevox,nuevoy),1)

          if self.env.matriz[nuevox][nuevoy] != 1:
            

            if self.env.search(explorado,nuevo) == False and self.env.search(frontera,nuevo) == False:
              if nuevo.estado == (self.env.finalX,self.env.finalY):
                print("Camino encontrado")
                print(self.env.imprimir(explorado))
                print(len(explorado))
                return 
              else:
                frontera.append(nuevo)
    
          
    return print("Camino no encontrado")
    






    



