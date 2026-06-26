def sum():
    a=int(input("Enter tamil mark: "))
    b=int(input("Enter enlish mark: "))
    c=int(input("Enter maths mark: "))
    d=int(input("Enter science mark: "))
    e=int(input("Enter social mark: "))
    total=a+b+c+d+e
    print("Total:",total)
    if(a>=35)and(b>=35)and(c>=35)and(d>=35)and(e>=35):
        print("Result: Your pass!")
    else:
        print("Result: Your fail!")
sum()

def add(a,b,c,d,e):
    total=a+b+c+d+e
    print("Total:",total)
    if(a>=35)and(b>=35)and(c>=35)and(d>=35)and(e>=35):
        print("Result: Your pass!")
    else:
        print("Result: Your fail!")
    
add(int(input("enter your marks: \n")),int(input()),int(input()),int(input()),int(input()))
