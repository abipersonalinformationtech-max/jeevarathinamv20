#1)i)
#odd/even using map()
a=[1,2,3,4,5,6,7,8,9,10]
def result(odd_even):
    if(odd_even%2)==0:
        return 'even'
    else:
        return 'odd'
b=list(map(result,a))
print(b)
print()

#1)ii)
# Using lambda function to check even or odd number
numbers = input("Enter a list of numbers separated by spaces: ").split()
# Convert the input into a list of integers
numbers = [int(num) for num in numbers]
# Check if each number is even or odd using lambda function
result=list(map(lambda num: 'even' if num % 2 == 0 else 'odd', numbers))
# Print the results
for num, result in zip(numbers,result):
    print("Number {} is {}".format(num,result))
print()

#2)i)
#find power value using map() & pow()
base=[1,2,3,4,5]
expo=[5,4,3,2,1]
result=map(pow, base, expo)
result_list=list(result)
print(result_list)
print()

#2)ii)
#find power value using map() with lambda function
num=[1,2,3,4,5]
power=3
result=list(map(lambda x: x**power, num))
print(result)
print()

#3)
#find armstrong number using map()
n=int(input("Enter the value: "))
a=list(map(int,str(n)))
b=list(map(lambda x: x**3,a))
if(sum(b)==n):
    print("The number is an armstrong number")
else:
    print("The number is not an armstrong number")

