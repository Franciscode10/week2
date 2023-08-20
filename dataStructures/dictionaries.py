#Creating a dictionarie
Dict = {"key": "value", "key2": "value2"}
print("Complete Dictionarie:")
print(Dict)

#Accessing an element in a dictionarie
print("Accesing an element in a dictionarie")
print(Dict["key"])

#Accessing an element using get()
print("Accessing an element using get()")
print(Dict.get("key2"))

#Create a dictionarie comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print(myDict)

myDict = {x: x+2 for x in [2,3,4]}
print(myDict)