#este es un codigo para la busqueda binaria

def binary_search(the_list,item): 
    #las siguientes variables: first y last mantienen un registro del inicio
    #y final del segmento con el que se está trabajando.
    first = 0  
    last = len(the_list)-1 #este valor cambiará a medida que la lista se reduzca
    found = False

    while first <= last and not found: 
    #mientras que first sea menor o igual a last y no se haya encntrado el item
        mid = (first + last) // 2
        #el doble // es para que nos den el resultado de la división de forma 

        if the_list[mid] == item: #si el item se encuentra en el medio de la lista... True
            found = True
        else:
            if item < the_list[mid]: 
            #si no está: se evaluará si el item es mayor o menor que el valor de enmedio
                last = mid - 1
                #si el elemento es menor, el valor last se pasa al valor de enmedio (mid) - 1
            else:
                first = mid +1
                #si el elemento es menor, el valor first se pasa al valor de enmedio + 1
    return found
    #dependiendo de este valor, ns dará un mensaje de la parte de abajo

#####

the_list = [10,12,13,14,15,18,19] #lista de caracteres
item = 15 #elemento que buscamos

if binary_search(the_list,item):
    print("The item is in the list")
else:
    print("The item is not in the list")