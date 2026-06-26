a = int(input("Enter A value:"))
b = int(input("Enter B value:"))

print("Before Swap :")
print("A Value is :",a)
print("B Value is :",b)

a = a+b
b = a-b
a = a-b

print("After Swap :")
print("A Value is :",a)
print("B Value is :",b)