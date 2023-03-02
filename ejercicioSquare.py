#Al parecer me faltaba un programa del curso...
#Define un método en la clase Square llamado change_size() que nos permita pasar
#un número que incremente o decremente (si el número es negativo) a cada lado del cuadrado
#Asegurate de que la instancia del cuadrado sea s1

class Rectangle():
    def __init__(self,w,l):
        self.width = w
        self.len= l
    
    def calculate_perimeter(self):
        return 2*(self.len + self.width)

class Square(Rectangle): 
    def __init__(self,s1): 
        self.s1 = s1 
    
    def calculate_perimeter(self):
        return self.s1 * 4

    def change_size(self,new_size): #segun esta es la solucion
        self.s1 += new_size #para achicar o agrandar el tamaño
    

rectangle = Rectangle(5,6)
print(rectangle.calculate_perimeter())
square =Square(5)
print(square.calculate_perimeter())
print(square.change_size(6))