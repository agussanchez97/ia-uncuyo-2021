import numpy as np
import pandas as pd

train_data_m = pd.read_csv("https://raw.githubusercontent.com/sjwhitworth/golearn/master/examples/datasets/tennis.csv") 

print(train_data_m)

#calcular la entropia de todo el cpnjunto de datos
def calc_total_entropy(train_data, label, class_list):
    total_row = train_data.shape[0] #tamaño total del dataset
    total_entr = 0
    
    for c in class_list: #para cada una de las clases del label
        total_class_count = train_data[train_data[label] == c].shape[0] #numero de clases
        total_class_entr = - (total_class_count/total_row)*np.log2(total_class_count/total_row) #entropia de la clase
        total_entr += total_class_entr #agregar la entropía de la clase a la entropía total del conjunto de datos
    
    return total_entr

#calcular la entropia del conjunto de datos filtrado
def calc_entropy(feature_value_data, label, class_list):
    class_count = feature_value_data.shape[0]
    entropy = 0
    
    for c in class_list:
        label_class_count = feature_value_data[feature_value_data[label] == c].shape[0] #recuenta filas de la clase del label
        entropy_class = 0
        if label_class_count != 0:
            probability_class = label_class_count/class_count #probabilidad de la clase
            entropy_class = - probability_class * np.log2(probability_class)  #entropia de la clase
        entropy += entropy_class
    return entropy

#calcular la ganancia de informacion de cierta caracteristica
def calc_info_gain(feature_name, train_data, label, class_list):
    feature_value_list = train_data[feature_name].unique() #valores de la caracteristica
    total_row = train_data.shape[0]
    feature_info = 0.0
    
    for feature_value in feature_value_list:
        feature_value_data = train_data[train_data[feature_name] == feature_value] #filtra filas con el valor 
        feature_value_count = feature_value_data.shape[0]
        feature_value_entropy = calc_entropy(feature_value_data, label, class_list) #calcula la entropa
        feature_value_probability = feature_value_count/total_row
        feature_info += feature_value_probability * feature_value_entropy #calcula la informacion
        
    return calc_total_entropy(train_data, label, class_list) - feature_info #calculating information gain by subtracting

#funcion para encontrar la característica con la mayor ganancia de información
def find_most_informative_feature(train_data, label, class_list):
    feature_list = train_data.columns.drop(label) #lista de caracteristicas,obviando label 
    max = -1 # guardar la ganancia anterior
    max_info_feature = None

    for feature in feature_list:  #recorre las caracteristicas
        feature_info_gain = calc_info_gain(feature, train_data, label, class_list) #ganancia de la actual caracteristica
        if max < feature_info_gain: #compara con la caracteristica anterior
            max = feature_info_gain
            max_info_feature = feature
            
    return max_info_feature

#Genera un nodo en el arbol y los valores de la caracteristica como ramas

def generate_sub_tree(feature_name, train_data, label, class_list):
    feature_value_count_dict = train_data[feature_name].value_counts(sort=False) #diccionario con los valores de la caracteristica

    tree = {} #nodo
    
    for feature_value, count in feature_value_count_dict.iteritems():#recorre el diccionario

        feature_value_data = train_data[train_data[feature_name] == feature_value] #dataset con solo feature_name = feature_value

        assigned_to_node = False #bandera para marcar si una clase es pura o no (todos yes / todos no)
        for c in class_list: 

            class_count = feature_value_data[feature_value_data[label] == c].shape[0] #contador de clase 

            if class_count == count: #si la clase es pura
                tree[feature_value] = c #agregar el nodo al arbol
                train_data = train_data[train_data[feature_name] != feature_value] #remover los valores del dataset
                assigned_to_node = True
        if not assigned_to_node: #la clase no es pura
            tree[feature_value] = "?" #deja los nodo con ? , como decir apuntando a none
            
    return  tree, train_data

#crear el arbol
def make_tree(root, prev_feature_value, train_data, label, class_list):

    if train_data.shape[0] != 0: #si el dataset no esta vacio
        max_info_feature = find_most_informative_feature(train_data, label, class_list) #encontrar la caracteristica mas informativa
       
        tree, train_data = generate_sub_tree(max_info_feature, train_data, label, class_list) #obtiene nodo del arbol y el conjunto de datos
      
        next_root = None
        
        if prev_feature_value != None: #agregar rama
            root[prev_feature_value] = dict()
            root[prev_feature_value][max_info_feature] = tree
            next_root = root[prev_feature_value][max_info_feature]
        else: #agregar raiz
            root[max_info_feature] = tree
            next_root = root[max_info_feature]
        
        for node, branch in list(next_root.items()): #recorre el arbol
            if branch == "?": #si se puede seguir expandiendo
                feature_value_data = train_data[train_data[max_info_feature] == node] 
                make_tree(next_root, node, feature_value_data, label, class_list) #llamada recursiva

#funcion principal
def id3(train_data_m, label):
    train_data = train_data_m.copy() #copia del dataset para hacer cambios sobre la copia , no sobre el dataset original
    tree = {} #defino el arbol como diccionario
    class_list = train_data[label].unique() #obtener la clases unicas del label

    make_tree(tree, None, train_data_m, label, class_list) #comienzo de la llamada recursiva
    return tree

tree = id3(train_data_m, 'play')

print(tree)
