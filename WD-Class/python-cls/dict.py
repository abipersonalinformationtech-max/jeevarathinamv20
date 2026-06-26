'''dictionary/dict:{Ordered, Changeable, No duplicates, key:value pair method}'''

a={"roll_no":101,"name":"ram","tamil":98,"english":74}
print(a)
print()

#type() function used to find that what is the given type of list!
print(type(a))
print()

#the following print function used to display the pair value of the key value in the given list! 
print(a["name"])

print(a["tamil"])

print(a["english"])

print(a.get("roll_no"))
print()

#update() function used to add the new value into the list & also used to update the exsisting value!
a.update({"math":45,"science":74})
print(a)
a.update({"tamil":100})
print(a)

#setdefault() used to set a default value in the given list!
a.setdefault("english",100)
a.setdefault("science",100)
print(a)
print()

#keys() function used to display the key value of the given list!
print(list(a.keys()))

#values() function used to display the pari value of the given list!
print(list(a.values()))
print()

#the following print function used to display the dictionary datatype into the list & tuple format!
print(a.items())
print()

#it leave the finally added value and displays remining items in the list!
a.popitem()
print(a)
print()

#it leave the given item in the print function and displays the remining items in the list!
a.pop("english")
print(a)
'''

        
