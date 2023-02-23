#Aquí irá la siguiente leccion: busqueda en una linked list

import random

class Node:
    def __init__(self, data=None, next= None):
        self.data = data
        self.next = next
    
    def print_node(self):
        print(self.data)
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append_node(self, data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def search(self, target):
    #acepta un parametro llamado target, que será el elemento que buscamos
        current = self.head #la busqueda empieza al inicio de la lista

        while current != None: #creamos un while loop para pasar por todos los elementos
            if current.data == target:
                print("Found it!")
                return True
        
            else:
                current = current.next #si no se encuentra, pasamos al siguiente elemento
        print("Not found") #si se llegó al último elemento y no ha sido encontrado
        return False
    
    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data, end=" ") #end es para ponerle un espacio al final del elemento
            node = node.next
        print("\n")

the_list = LinkedList()

for j in range(0,20): 
    j = random.randint(1,30) #pondremos numeros del 1 al 30 de forma aleatoria
    the_list.append_node(j)

the_list.print_list()
the_list.search(10)