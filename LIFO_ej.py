#ejercicio: revertir la palabra yesterday con stack
#debe haber un metodo push y pop, y una clase Stack
class Stack:
    def __init__(self): #guarda los elementos en un stack
        self.items = []

    def is_empty(self): #checa si el stack está vacío
        return self.items == []

    def push(self, item): #agrega elementos al stack
        self.items.append(item)

    def pop(self): #quita el último elemento del stack
        return self.items.pop()

    def peek(self): #muestra el último elemento del stack
        last = len(self.items)-1
        return self.items[last]

    def size(self): #nos da el tamaño del stack
        return len(self.items)

stackY = Stack()
revYst = "" #para almacenar la palabra al reves

for c in "yesterday":
    stackY.push(c)
print(stackY.items)

for i in range(len(stackY.items)): 
    revYst += stackY.pop()

print(revYst)

#NO SE COMO NI PORQUÉ PERO TIENE QUE ESTAR TOOODO EL ASUNTO DE LOS METODOS
#PUSH, POP, PEEK, ETC