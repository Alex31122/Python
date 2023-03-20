# tuple =   collection which is ordered and unchangeable used to group related data

student = ("Hector",16,"male")

print(student.count("Hector"))
print(student.index("male"))

for x in student:
    print(x)

if "Hector" in student:
    print("Hector is here!")