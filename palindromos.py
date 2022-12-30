#Algoritmo para buscar una palabra palindroma

def es_palindromo(word):
    word = word.lower() #nos aseguramos de que la palabra esté en minúsculas
    return word[::-1] == word
    #lo arriba, hace que la palabra que escribrimos se revierta
    #esto cortando la palabra y poniéndola al revés
    #y este resultado se comparará con la palabra original para ver si es una palabra
    #palindroma.

result = es_palindromo("ana")
print(result)