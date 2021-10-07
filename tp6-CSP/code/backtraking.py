def print_solution(queen):
    
    x=y=0
    print('')
    print ('La solución al problema de las ocho reinas es:')
    for x in range(len(queen)):
        for y in range(len(queen)):
            if x==queen[y]:
                print('<q>',end='')
            else:
                print('<->',end='')
        print('\t')
        
 
 #Prueba si la reina en (fila, col) está siendo atacada
 # Si es atacado, el valor devuelto es 1, de lo contrario devuelve 0
def attack(row,col,queen):
    
    i=0
    atk=0
    offset_row=offset_col=0
    while (atk!=1)and i<col:
        offset_col=abs(i-col)
        offset_row=abs(queen[i]-row)
                 # Juzga si las dos reinas están en la misma línea o en la misma diagonal
        if queen[i]==row or offset_row==offset_col:
            atk=1
        i=i+1
    return atk

#funcion recursiva principal, recibe un value que seria el nivel , una lista vacia con n posiciones, y un contador 
def decide_position(value,queen,estados):
    
      for i in range(len(queen)):

          if attack(i,value,queen)!=1:
              queen[value]=i
              if value==len(queen)-1:
                print_solution(queen)
                print("Estados",estados)
              else:
                decide_position(value+1,queen,estados+1)
      
          i=i+1
    
