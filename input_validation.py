# OPTION 1
def call_input(dimension):
    try:
        value = float(input("Indicate your %s positioning in the arena: " % dimension))
    except ValueError:
        print("Something went wrong")
        return call_input(dimension)  # É preciso voltar a pedir o return da função, caso contrário não é obtido nenhum resultado da função.
    else:
        return value
      
# OPTION 2
def call_input(dimension):
    while True:
        try:
            return float(input("Indicate your %s positioning in the arena: " % dimension))
        except ValueError:
            print("Something went wrong")
#return acts as a break in the case of code within functions, because return will make the interpreter leave the function with a result, so the while True loop is not infinite.
