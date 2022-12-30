#Otra pregunta de entrevista es hacer un codigo que indique la cantidad de veces que
#se repite cierto caracter en un string

def count_characters(string):
    count_dict = {} #diccionario para almacenar las letras

    for c in string:
        if c in count_dict: #recorremos el string
            count_dict[c] += 1 #si la letra que buscamos ya está, se incrementa en 1
        else:
            count_dict[c] = 1

    print(count_dict)

count_characters("Perro")