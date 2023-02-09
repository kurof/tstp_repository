#Ejemplo de uso de set() para evitar duplicados en una lista en Python

a_set = set()

a_set.add('Susan Addams')
a_set.add('Kwame Goodall')
a_set.add('Jill Hampton')

#intento de duplicado
a_set.add('Susan Addams')

print(a_set)