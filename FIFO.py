#Aplicando FIFO con Queues
class Queue:
    def __init__(self):
        self.items = [] #al igual que el stack, se apoya de una lista
    
    def is_empty(self):
        return self.items == [] #ve si el queue está vacío

    def enqueue(self,item):
        self.items.insert(0,item) 
        #agrega un elemento al frente de la cola, poniendo un indice 0 y el item
    
    def dequeue(self):
        return self.items.pop() #quita el primer elemento del queue y lo devueleve
    
    def size(self):
        return len(self.items) #nos da el tamaño del queue

#from a_queue import Queue #aparentemente no es necesrio hacer esto
aq = Queue()
print(aq.is_empty())

#agregamos elementos al queue
for i in range(11):
    aq.enqueue(i)
print(aq.items)

#para imprimir cada numero de nuestro queue
for i in range(aq.size()):
    print(i) #va imprimiendo cada numero
