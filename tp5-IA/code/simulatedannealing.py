import environment
from datetime import datetime
import random, time, math
from copy import deepcopy, copy
import decimal
class AgentSimulated:

  def __init__(self,env): #recibe como parámetro un objeto de la clase Environment
    self.env=env
    self.elapsedTime = 0
    self.temperature = 4000
    self.sch = 0.99
    self.startTime = datetime.now()
    self.simulatedAnnealing()

  def calculateCost(self,status):
      num = 0
      for i in range(len(status)):
        for j in range(i + 1,len(status)):
 
          if status[i] == status[j]:
            num += 1
          offset = j - i
          if abs(status[i]-status[j]) == offset:
            num += 1
      return num


  
  def simulatedAnnealing(self):

    status = self.env.reinas
    print(status)
    solutionFound = False
    paso=0
    while self.temperature > 0 and solutionFound == False :
      
      paso = paso + 1
      status = self.env.recalculo_reinas()
      self.temperature *= self.sch
      neighbours = list(status)
      
      de = self.calculateCost(neighbours) - self.calculateCost(status)

      exp = math.exp(-de/self.temperature)

      if de > 0 or random.uniform(0, 1) < exp:
        
        status = neighbours

      if self.calculateCost(status) == 0:
        print("Solucion: ")
        print(status)
        self.elapsedTime = self.getElapsedTime()
        print("Success, Elapsed Time: %sms" % (str(self.elapsedTime)))
        solutionFound = True
        break
    if solutionFound == False:
      print("No se encontro solucion")
      self.elapsedTime = self.getElapsedTime()
      print("Unsuccessful, Elapsed Time: %sms" % (str(self.elapsedTime)))

      return self.elapsedTime

  def getElapsedTime(self):
    endTime = datetime.now()
    elapsedTime = (endTime - self.startTime).microseconds / 1000
    return elapsedTime

  
