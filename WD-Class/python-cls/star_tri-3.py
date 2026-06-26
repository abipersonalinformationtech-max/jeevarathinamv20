y=0
row=int(input("Enter the value: "))
for i in range(row):
    for j in range(y,i+1):
        print(" ", end="")
    for j in range(y, row-i):
        print("*",end="")
    print("\n")
    
