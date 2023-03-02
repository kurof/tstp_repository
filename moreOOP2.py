#ejercicio de more OOP 2
#Haz una clase Square que tenga un metodo que calcule su perimetro.
#Cuando imprimas un objeto Square, saldrá un mensaje con el largo de cada lado de la figura.
#Por ejemplo, el código print(Square(29)) deberá decir: 29 by 29 by 29 by 29.

class Square():

    def __init__(self,s1):
        self.s1 = str(s1)

    def __repr__(self):
        return self.s1
    
    def calcularP (self):
        #el perimetro de un cuadrado es n*4
        print("Perimetro = {} by {} by {} by {}".format(self.s1,self.s1,self.s1,self.s1))

num = Square(29)
print(num.calcularP())


#La solucion del instructor
#class Square():

#    def __init__(self,s1):
#        self.s1 = str(s1)
#
#    def __repr__(self):
#        return "{} by {} by {} by {}".format(self.s1, self.s1, self.s1, self.s1)
#    
#    def calcularP (self):
#        #el perimetro de un cuadrado es n*4
#        return self.s1 * 4
#
#print(Square(29))