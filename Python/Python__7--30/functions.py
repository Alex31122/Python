# function = a block of code which is executed only when it is called.

def hello(first_name,last_name,age):
    print("Hello "+first_name+" "+last_name)
    print("You are " + str(age) + " years old")
    print("Have a nice day!")
#hello(first_name,last_name)

# keyword arguments = arguments preceded by an identifier when we paa them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments that our functions receives.

hello(last_name="Hernandez",age=16,first_name="Hector")