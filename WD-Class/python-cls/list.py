'''list:[Ordered, Changeable, Allows duplicate]'''

n = int(input("Enter the value: "))
list=[]
for i in range(0, n):
    list.append(i)
    print("List[",i,"]=",i)
print()
  
#list of user input:
a=[]
n=int(input("Enter the limit : "))
print("Enter the value: ")
for i in range(0, n):
    a.append(input())
for i in range(0, n):
    print("a[",i,"]=",a[i])
