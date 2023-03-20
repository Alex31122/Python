
# str.format()  =    optional method that gives users
#                    more control when displaying output

name = "Hector"

print("Hello, my name is {}".format(10))
print("Hello, my name is {name:10}. Nice to meet you".format(name))
print("Hello, my name is {0:<10}. Nice to meet you".format(name)) #  left alignment
print("Hello, my name is {:>10}. Nice to meet you".format(name)) #  right alignment
print("Hello, my name is {:^10}. Nice to meet you".format(name))

