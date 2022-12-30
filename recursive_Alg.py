#Ejemplo de algoritmo recursivo, este imprimirá la letra de la canción
#99 bottles of beer on the wall

def bottles_of_beer(bob):
    if bob < 1: #esta línea satisface la primera regla, si Bob es menor a 1: deja de llamarse
        print("""No more bottles of beer on the wall. No more bottles of beer.""")
        return

    tmp = bob

    bob -= 1 #esta cumple la segunda porque va a cambiar el estado y decrementará para cumplir la primera regla

    print("""{} bottles of beer on the wall.\n{} bottles of beer. Take one down, pass it around,
          \n{} bottles of beer on the wall.""".format(tmp,tmp,bob))

    bottles_of_beer(bob) #la última regla se satisface al llamar a la función

bottles_of_beer(99) #llamamos la función con el número de botellas