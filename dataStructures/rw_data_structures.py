#Lists
list = [1,2,3,"Hola", True]
print(f"This is the original list: {list}")
list.append("Nuevo")
print(f"Añadía algo a la lista: {list}")
list.remove(list[0])
print(f"Elimine al 1 de la lista: {list}")
list.pop()
print(f"Elimine al ultimo elemento de la lista {list}")


#Tuples
tuples = (10.24, 24.10)
print(f"\nThis is a tuple: {tuples}, we use this data structure to group values that must be together. Like a point(x,y,z)")

#Dictionaries
dictionarie = {"key": "value", "Messi": "champion"}
print(f"\nThis is the original dictionarie: {dictionarie}")
print(f"Search a value with its key: 'Messi': {dictionarie['Messi']}")
dictionarie["Maradona"] = 86
print(f"Add a key-value-pair to the dictionarie {dictionarie}")

#Create a dictionarie comprehension
myDictionarie = {x: x**2 for x in [1,2,3,4]}
print(f"This is a dictionarie comprehension: {myDictionarie}")

#set
set = set()
set.add(1)
set.add(2)
set.add(3)
set.add(4)
set.add(2)

print(set)

set.remove(1)
print(set)

print(f"The length of this set is {len(set)}")
