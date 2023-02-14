#aplicandola solucion al problema de Last Digit

input_string = "Buy 1 get 2 free"
new_list = [c for c in input_string if c.isdigit()][-1] #funcion isdigit
#lo que nos dice la línea de arriba es que se hará un loop por cada caracter del string
#para crear una lista con cada elemento separado
print(new_list)