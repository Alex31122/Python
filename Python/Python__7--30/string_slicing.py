# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Hector Alejandro"

first_name = name[0:6]              # save only the 0 --> 5 characters
last_name = name[7:]                # save from 7th caracter and go on
funky_name = name[0:15:2]            # saves with jumps by 2
reversed_name = name[::-1]

names = [first_name, last_name, funky_name, reversed_name]
print(names)

print("")
print("==========slice()==========")

website1 = "https://google.com"
website2 = "https://wikipedia.com"

slice = slice(8,-4)

print(website1[slice])
print(website2[slice])
