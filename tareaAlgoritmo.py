#dada una lista con numeros enteros que se repiten dos veces a excepcion de 1, tenemos que
#encontrar el numero que NO se repite

def unico(lista):
    uSet = set() #hacemos el set para que se pongan los elementos de la lista

    for i in lista: #recorremos la lista
        lenght = len(uSet) #vemos el tamaño de la lista
        uSet.add(i) 
        #agregamos los elementos de la lista, como no se pueden duplicados, se pone 1 vez
        lenght2 = len(uSet) #tomamos otra vez el tamaño de la lista

        if lenght == lenght2: #comparamos los tamaños
            uSet.remove(i) #se eliminan los elementos repetidos

    return uSet

lista = [1,1,2,2,3,3,4,5,5,6,6,7,7]
print(unico(lista))

#está engorroso pero el chiste es que, al tener un set (donde no se puede usar duplicados),
#vamos metiendo los elementos, como se comparan los tamaños y a fin de cuentas set lográ 
#identificar los que se repiten, lo que se hace es eliminar esos elementos que se duplicaron.
#dejando solo el que no tenía duplicado....
#O sea... tiene sentido pero no sé explicarlo.
#Me basé en el código de duplicados.