

# str.format()  =    optional method that gives users
#                    more control when displaying output

number = 3.14159

print("The number pi is {:.3f}".format(number)) # 3floats

number = 1000

print("The number is {:,}".format(number))
print("The number is {:b}".format(number)) # binary
print("The number is {:o}".format(number)) # octal
print("The number is {:x}".format(number)) # hexadecimal
print("The number is {:X}".format(number))
print("The number is {:E}".format(number)) # scientific notation
print("The number is {:e}".format(number))
