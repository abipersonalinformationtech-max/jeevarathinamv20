'''y=0
row=int(input("Enter the value: "))
for i in range(row):
    for j in range(y, row-1):
        print(" ", end="")
    for j in range(y, i+1):
        print("*", end="")
    print("\n")'''

'''row=int(input("enter: "))
for i in range(row):
    for j in range(row, i, -1):
        print(" ", end="")
    for k in range(i + 1):
        print("* ", end="")
    print()'''


y=0
row=int(input("Enter the value: "))
for i in range(y, row):
    for j in range(row-i):
        print(" ", end="")
    for j in range(i):
        print(" *", end="")
    print()

    
for i in range(1,6):
    for j in range(6-i):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    print()
