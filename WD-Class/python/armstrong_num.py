n=int(input("Enter 3 digit Number: "))
s=n
a=n%10
n=n//10
b=n%10
c=n//10
e=(c*c*c)+(b*b*b)+(a*a*a)
if(s==e):
    print(e,"is Armstrong Number")
else:
    print("you are entered the in valid number. Please enter a valid Armstrong number!")
