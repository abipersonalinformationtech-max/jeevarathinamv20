a=int(input("Enter your Tamil mark :"))
b=int(input("Enter your English mark :"))
c=int(input("Enter your Maths mark :"))
d=int(input("Enter your Science mark :"))
e=int(input("Enter your Social mark :"))
total=a+b+c+d+e
ave = total/5
print("Total: ",total)
print("Average: ",ave)

if(a>=35)and (b>=35)and(c>=35)and(d>=35)and(e>=35):
    print("Result: Pass")
else:
    print("Result: Fail")
    
    
if(total>=450):
    print("Grade: A")
elif(total>=380):
    print("Grade: B")
elif(total>=340):
    print("Grade: C")
else:
    print("Grade: D")