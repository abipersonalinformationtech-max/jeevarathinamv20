y=0
row=int(input("enter the value:"))
for i in range(row):
    for j in range(y,row-i):
        print(" ", end="")
    for j in range(y, i+1):
        print("*", end="")
    print("\n")
