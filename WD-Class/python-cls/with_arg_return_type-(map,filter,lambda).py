'''with argument return type:
   1)map
   2)filter
   3)lambda'''

#map-it returns all values result!
a=[48,62,34,45,62,23,74,25]

def result(mark):
    if(mark>=35):
        return 'pass'
    else:
        return 'fail'
b=(tuple(map(result,a)))
print(b)

#filter-it returns only the true values!
def result(mark):
    if mark>=35:
        return True
    else:
        return False
mark=[48,62,34,45,62,23,74,25]
res=list(filter(result,mark))
print(res)


#lambda-There is no nee to declare the def befor function name. it is one line function.
#it is also return all values result like map function.
s = lambda x: x**3
a = [1,2,3,4,5,6]
f=list(map(s,a))
print(f)




