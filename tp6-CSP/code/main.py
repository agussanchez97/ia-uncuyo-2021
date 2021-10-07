
import backtraking

from datetime import datetime
import time

#calcular el tiempo
def getElapsedTime(startTime):
    endTime = datetime.now()
    elapsedTime = (endTime - startTime).microseconds / 1000
    return elapsedTime
    
elapsedTime = 0
startTime = datetime.now()
n=input("Ingrese numero de reinas: ")
 # Definir la capacidad máxima de la pila
queen = [None] * int(n) #Almacenar la posición de fila de 8 reinas
csp.decide_position(0,queen,0)
elapsedTime = getElapsedTime(startTime)
print("Success, Elapsed Time: %sms" % (str(elapsedTime)))
