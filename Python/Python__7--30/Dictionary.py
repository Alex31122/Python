# Dictinary = A changeable, unordered collection of unique key:value pairs
#             Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

print(capitals['Russia'])
print(capitals.get('Germany'))

capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})

#capitals.pop('China')
#capitals.clear()

print(capitals.items())
print(capitals.keys())
print(capitals.values())

for key,value in capitals.items():
    print(key,value)