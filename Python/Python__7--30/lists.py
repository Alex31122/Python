# list = used to store multiple items in a single variable

food = ["pizza", "hamburger","hotdog","spaghetti","pudding"]
food[0] = "sushi"
print(food[0])

food.append("ice cream")    # add to the list
food.remove("hotdog")       # remove from the list
food.pop()                  # remove the last element
food.insert(0,"cake")       # insert on the position a element
food.sort()                 # sort the element alphabetically
#food.clear()                # eliminate all the elements

for x in food:
    print(x)