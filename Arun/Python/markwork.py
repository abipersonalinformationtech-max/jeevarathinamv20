tam = int(input("Enter Tamil Mark : "))
eng = int(input("Enter English Mark :"))
mat = int(input("Enter Maths Mark :"))
sci = int(input("Enter Science Mark :"))
soc = int(input("Enter Social Mark :"))

total = tam + eng + mat + sci + soc
avg = total / 5

print("Total : ",total)
print("Average : ",avg)

a=int(input("Enter pass"))
if a >=pass:
    print("Eligible for pass")
    else:
        print("Not Eligible for pass")