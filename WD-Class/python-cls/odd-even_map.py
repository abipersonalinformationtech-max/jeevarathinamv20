#odd/even using map()
a=[1,2,3,4,5,6,7,8,9,10]
def result(odd_even):
    if(odd_even%2)==0:
        return 'even'
    else:
        return 'odd'
b=list(map(result,a))
print(b)
