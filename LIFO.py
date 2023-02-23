#Aplicación de LIFO con stacks en Python

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

#from stack import Stack
#por razones de la vida, me marca error con esta linea 
#supongo que es porque instale el stack?
stack1 = Stack()
print(stack1.is_empty())
stack1.push(1) #agregamos un elemento
print(stack1.is_empty()) #no me imprime nada si no pongo el print

#agregando elementos del 1 al 11
for i in range(1,11):
    stack1.push(i)

print(stack1.items)
print(stack1.size())
stack1.pop()
print(stack1.size())
print(stack1.items)

stack2  = Stack()
for c in "Hello":
    stack2.push(c) #agregamos las letras al stack

reversed_string = ""
for i in range(len(stack2.items)): 
#recorremos toda la variable y vamos quitando los últimos elementos con pop
#donde los almacenamos en la variable reverse_string
    reversed_string += stack2.pop()

print(reversed_string)