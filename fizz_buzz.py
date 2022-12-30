#Probando el fizz buzz en pycharm

def fizz_buzz():
    for i in range(1,101):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)

fizz_buzz()
#OK POR ALGUNA RAZON AQUI SI JALA MEJOR
#Tengo la teoría que es por el orden de las operaciones