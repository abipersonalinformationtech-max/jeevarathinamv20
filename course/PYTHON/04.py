'''
a = int(input("Enter a Number : ")) # 5
f = 1
for i in range(1,a+1): # 1,4
    f = f*i
print("Factorial is ",f)
'''

txt = input("Enter a string : ")
d = 0
l = 0

for i in txt:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1

print("No of Letters",l)
print("No of Digits",d)

