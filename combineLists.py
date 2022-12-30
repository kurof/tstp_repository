#Esto es parte de las preguntas de entrevista con soluciones en Python

movies = ["Interstellar","Inception","The Prestige","The Dark Knight","Batman Begins"]
#primero se hacen las listas

ratings = [1,10,10,8,6]

new_list =[] #creamos la lista dónde se hará la tupla nueva

for tree in zip(movies,ratings):
    new_list.append(tree) #se agregan los elementos a la lista nueva
    #Lo que hará el zip es tomar los elementos de las listas y juntarlos

print(new_list) #vemos el resultado