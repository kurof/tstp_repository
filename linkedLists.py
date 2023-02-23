#como hacer un modulo, es lo primero que debermos hacer para hacer una linked list

class Node: #creamos la clase
    def __init__(self, data=None, next = None): #debe tener 2 variables
        self.data = data #el dato que vamos a poner
        self.next = None #el siguiente nodo de la lista

    #ya que el metodo anterior solo crea un nodo pero no lo imprime:

    def print_node(self):
        print(self.data) #imprime el dato


#ahora sí, como hacer una linked list
class LinkedList:
    def __init__(self):
        self.head = None #la variable head será la que almacenará la cabeza de la lista

    def append_node(self,data): #para agregar modulos
        if not self.head:
            self.head = Node(data)
            #si la lista no tiene un head todavía, se crea una con el dato que se puso
            return
        else:
            #si ya tiene un head: pasamos a encontrar el ultimo modulo y ponerle la 
            #variable next para poner un modulo nuevo
            current = self.head

            while current.next: #iteramos por la lista
                current = current.next 
                #asignamos la variable current al siguiente elemento de la lista
                #o sea se irán asignando elementos después del head y así

            current.next = Node(data) 
            #cuando llega al final de la lista, se pasa la variable a otro nodo
    
    def print_node(self): #para imprimir todos los modulos
        node = self.head #almacena el inicio de la lista
        while node is not None: #hasta que termine la lista, encuentre el null
            print(node.data) #imprime elprimer elemento
            node = node.next #para obtener el siguiente nodo e imprimirlo

the_list = LinkedList()
the_list.append_node("Monday")
the_list.append_node("Tuesday")
the_list.append_node("Wednesday")
the_list.print_node()

#ejemplo de como hacer un nodo e imprimirlo
#a_node = Node("Monday") #creamos el elemento
#a_node.print_node()