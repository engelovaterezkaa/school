names = [
    "Alice", "Bob", "Charlie", "David", "Eva",
    "Fiona", "George", "Hannah", "Isaac", "Jack",
    "Katherine", "Liam", "Mia", "Noah", "Olivia",
    "Paul", "Quinn", "Rachel", "Sam", "Tina"
]

print(names[3]) #vypsani konkretniho jmena 

#vypsani vsech jmen - for: 
for name in names:
    print(name)

for i, name in enumerate(names): #nejen hodnota ale i index pri vypsani (pouzijeme enumerate), kdyz napiseme jen i, zacne od nuly, kdyz i + 1 tak od 1
    print(i + 1, name)


#s fstringem 
for i,name in enumerate(names):
    print(f"{i + 1}. {name}")