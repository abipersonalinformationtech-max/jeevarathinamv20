'''set: {Unordered, Unchangeable, Unindexed, No duplicates}'''

x={11,12,13,14,15}
print(x)
print()

#type() function used to find that what is the given type of list!
print(type(x))
print()

#add() function used to add the new item into the given list!
#in this add() function we can add the item one by one, more than one can't be added!
x.add(16)
x.add(17)
print(x)
print()

#clear() function used to clear all the items stored in the given list &
#finally it displays the type of list like (set typle etc..)!
x.clear()
print(x)

