import agent
import enviroment
import node


#m=input("Ingrese la posicion en X del agente ")
#n=input("Ingrese la posicion en Y del agente")

#p=input("Ingrese posición final X del agente")
#q=input("Ingrese posicion final Y del agente")

obstaculos = int(input("Ingrese cantidad de obstaculos"))
entorno=enviroment.Enviroment(100,100,0,0,89,91,obstaculos)

ag=agent.Agent(entorno)
