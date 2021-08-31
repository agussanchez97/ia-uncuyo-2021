import agent
import environment
import node



obstaculos = int(input("Ingrese cantidad de obstaculos"))
entorno=environment.Enviroment(100,100,0,3,93,79,obstaculos)

ag=agent.Agent(entorno)
