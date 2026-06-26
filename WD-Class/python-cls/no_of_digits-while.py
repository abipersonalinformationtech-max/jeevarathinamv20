n=int(input("Enter the value: "))
count=0
while n !=0:
    n//=10
    count+=1
    print("number of digits: "+str(count))
