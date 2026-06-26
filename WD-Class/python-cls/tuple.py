'''tuple: (Ordered, Unchangeable, Allows duplicate)'''

a=(1,2,3,3,4,5,6)
print(a)
print()

#type() function used to find that what is the given type of list!
print(type(a))
print()

#len() function used to find the length of the function!
print(len(a))
print()

#count() function used to find the given num is how many times there in the given type of list!
b=a.count(3)
print(b)
c=a.count(4)
print(c)
print()

#here for loop used to print the list of items one by one!
for i in a:
    print(i)
