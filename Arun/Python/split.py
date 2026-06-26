'''
    % - modulas - remainder
    // - division - Quatient
'''
num = int(input("Enter the digits : ")) #123

a = num % 10 #3
num = num // 10 #12
b = num % 10  #2
c = num // 10 #1

print("First Digit is",a)
print("Second Digit is",b)
print("Third Digit is",c)
