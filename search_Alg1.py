#Ejemplo de ejecución del algoritmo de búsqueda con cartas

def ss(number_list, n):
    found = False #se estará buscando un número, cuando se encuentre pasará a True

    for i in number_list:
        if i == n:
            found = True
            break #si se encuentra, termina el programa

    return found #el return va en el mismo espacio que for

#Para probar el programa
numbers = range(1,101)
result = ss(numbers,99)
print(result)