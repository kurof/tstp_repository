#EJERCICIO DE LAST DIGIT 
#Usa la list comprehension para pasar [1,7,5,3,2]  a una lista nueva. Esta lista##
#deberá tener todos los enteros de la lista multiplicados por 7. Imprime esa lista.

og_list = [1,7,5,3,2]
new_list = [c*7 for c in og_list] #multiplicando todos los elementos por 7

print(new_list)