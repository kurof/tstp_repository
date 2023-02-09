#otro ejemplo de duplicados

def return_duplicates(a_list):
    dups = []
    a_set = set()

    for item in a_list:
        length_one = len(a_set)
        a_set.add(item)
        length_two = len(a_set)

        if length_one == length_two:
            dups.append(item) #agregamos elemento duplicado a la lista
    return dups

a_list = ['Susan Addams','Kwame Goodall','Jill Hampton','Susan Addams']
dups = return_duplicates(a_list)

print(dups) #se imprime la lista de duplicados