#usar stack para crear una lista [1,2,3,4,5] en reversa
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

stack1 = Stack()
for c in range(1,6):
    stack1.push(c)
print(stack1.items)

#tratando de revertir el stack
rev = [] #lista

for i in range(len(stack1.items)):
    while i > 0 and not stack1.is_empty():
    #mientras que el indice sea mayor a 0 y el stack NO esté vacío
        rev.append(stack1.pop()) #se irá agregando el elemento eliminado del stack
        i = i - 1 #reduciendo el indice en 1, poniendo de 1 en 1 en la lista
print(rev)

#weeee tardé mucho en pensar esto, pero gracias a investigar y checar los codigos anteriores
#funciono :D 