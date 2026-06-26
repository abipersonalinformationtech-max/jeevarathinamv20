row=int(input("Enter value: "))
for i in range(row):
    for j in range(row-i):
        print("*",end="")
    print("\n")


'''row=int(input("Enter the value: "))
for i in range(row, 0, -1):
    for j in range(0, i):
        print("*",end="")
    print("\n")'''
