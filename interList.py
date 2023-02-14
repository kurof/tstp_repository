#encontrar la interseccion entre dos listas

def interseccion(list1,list2):
    list3 = [value for value in list1 if value in list2]
    return list3 
    #se hace una lista con los numeros para comparar si el elemento está en ambas listas

####otra forma

def return_intersection(list1,list2): #este conviene si usamos mas de 2 sets
    set1 = set(list1) #convertimos la lista a set para usar intersection()
    set2 = set(list2)
    return list(set1.intersection(set2)) #convertimos a list el resultado de intersection()

list1 = [2,43,48,62,64,28,3]
list2 = [1,28,42,70,2,10,62,31,4,14]

print("Resultado creando funcion de 0: ",interseccion(list1,list2))
#por alguna razon el instructor lo habia puesto como return_interseccion
#pero está mal.

#para el intersection():
new_list = return_intersection(list1,list2)
print("Solución con funcion intersection(): ",new_list)
