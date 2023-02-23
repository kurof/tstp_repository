#ejemplo de FIFO con una fila de cine
import time
import random

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
    
    #lo de arriba es el mismo codigo del ejemplo de FIFO
    #ahora lo que viene son lineas nuevas}
    def simulate_line(self,till_show,max_time):
        #trabaja con 2 parametros: el tiempo que hay antes de que empiece la pelicula
        #y el tiempo limite para que una persona pueda comprar un boleto
        pq = Queue() #simulará la fila
        tix_sold = [] #mantiene registro de la compra

        for i in range(100): 
        #llenamos la fila (queue) de personas del 1 al 100 (que sería del 0 al 99)
            pq.enqueue("person" + str(i))

        #el modulo time tiene una funcion llamada time que nos devuelve un numero float
        #que representa el número de segundos desde el epoch, una medida de tiempo que
        #los programadores usan como referencia.
        
        t_end = time.time() + till_show
        #t_end es el tiempo límite que hay para comprar los boletos, cuando la sim termina
        #sumando el tiempo actual (time.time()) mas la hora a la que empieza la pelicula
        now = time.time() #tiempo actual

        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randint(0,max_time) #numero aleatorio que representa el tiempo de serv
            time.sleep(r) #dependiendo del tiempo r, será el tiempo que NO se ejecutara el code
            person = pq.dequeue() #una vez que pase el tiempo, se quita a la persona
            print(person)
            tix_sold.append(person) #se agrega la persona a la lista de ventas
        return tix_sold

queue = Queue()
sold = queue.simulate_line(20,2)
print(sold)