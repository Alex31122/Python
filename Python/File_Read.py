try:

    with open('Hola')as file:
        print(file.read())

    print(file.closed)
except FileNotFoundError:
    print("That file was not found :(")
