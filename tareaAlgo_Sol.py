#SOLUCION DEL INSTRUCTOR

numbers = [1, 1, 2, 2, 3, 3, 4, 5, 5]
count = {} #contador
for i in numbers: #recorre la lista
    if i not in count: 
        count[i] = 1 #si no está en la lista, se pone en 1
    else:
        count[i] += 1 #si ya está, se incrementa en 1
    #lo que se mostrará será el contador de veces que está cada elemento de la lista
    #como: 1: 2 veces, y así

print(count) #para ilustrar lo que hace el loop
for key, value in count.items(): #bbuscamos el que tiene solo 1 en el contador
    if value == 1:
        print(key)