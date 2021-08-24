### Considere una versión modificada del entorno de la aspiradora del Ejercicio 2.7, en el que se penalice al agente con un punto en cada movimiento.

#### A) ¿Puede un agente reactivo simple ser perfectamente racional en este medio? Explíquese

No puede ser racional ya q considerando cuando el entorno este completamente limpio , el agente seguirá oscilando por los casilleros hasta que se terminen 
la cantidad de pasos que le hemos dado , si a esto le agregamos que en cada paso se lo penalizara la performance sera bastante pobre y no cumplira el 
concepto de racionalizacion. 

#### B) ¿Qué sucedería con un agente reactivo con estado? 

No sería racional , ya que aunque al entorno le agregamos un atributo para saber el estado (dirty-clean) de la casilla donde está parado el agente o para 
contabilizar las casillas por las que ha pasado el agente , si no conocemos nada más del entorno o la cantidad de casillas sucias que quedan el agente seguirá 
moviéndose por lo que seguirán contabilizando las penalizaciones.

#### C) ¿¿Cómo se responderían las preguntas a y b si las percepciones proporcionan al agente información sobre el nivel de suciedad/limpieza de todas las cuadrículas del entorno?

Serían agentes racionales, ya que podrían parar cuando todos los cuadros estén limpios, sin embargo el b sería más eficiente que el a , es decir sería perfectamente 
racional ya que tambien lleva el estado interno de las acciones del agente.

### Considere una versión modificada del entorno de la aspiradora del Ejercicio 2.7, en el que la geografía del entorno (su extensión, límites, y obstáculos) sea desconocida,
### así como, la disposición inicial de la suciedad. (El agente puede ir hacia arriba, abajo, así como, hacia la derecha y a la izquierda.)

#### A) ¿Puede un agente reactivo simple ser perfectamente racional en este medio? Explíquese.

El agente no puede ser racional si no se conoce la geografía del entorno ya que definimos racionalidad como la capacidad de que el agente maximice su capacidad de rendimiento , 
si el mismo no puede reconocer donde tiene que limpiar y donde no o hasta donde puede moverse entonces su desempeño va a ser muy pobre y no sería racional.

#### B) ¿Se puede diseñar un entorno en el que el agente con la función aleatoria obtenga una actuación muy pobre?

 Si , si diseñamos un entorno con muy poca suciedad y muchos pasos el agente va a tener un desempeño bastante malo ya que debería caer justo en una casilla sucia (de forma aleatoria) 
 y que la acción (aleatoria) sea limpiar , ya que hay pocas probabilidades de que esto pase porque la suciedad es muy poca , el desempeño no será bueno.
 
 #### C) ¿Puede un agente reactivo simple con una función de agente aleatoria superar a un agente reactivo simple? 
 
 Si el agente reactivo simple tiene una muy mala performance puede superarlo uno aleatorio.
 
 #### D)¿Puede un agente reactivo con estado mejorar los resultados de un agente reactivo simple? 
 
 No puede mejorar los resultados , ya que la cantidad de pasos va a ser la misma para ambos y ninguno tiene forma de ver el entorno y la cantidad de casillas sucias que quedan.
