#Programa para identificar anagramas
def is_anagram(w1,w2):
    w1 = w1.lower() #se pone en minúsculas
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)
    #el metodo sorted, nos regresa un string en orden alfabetico
    #con el que podremos comparar si las 2 palabras tienen las mismas
    #letras.

result = is_anagram("cinema","iceman")
print(result)