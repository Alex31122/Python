# set = collection which is unorderes, unindexed. No duplicate values

utensils = {"fork","spoon","knife","knife","knife"}
dishes = {"bowl","plate","cup"}

utensils.add("napkin")
utensils.remove("fork")
utensils.clear()
dishes.update(utensils)
dinner_table = utensils.union(dishes)

print(utensils.difference(dishes))
print(dishes.intersection(utensils))

for x in utensils:
    print(x)

for x in dinner_table:
    print(x)