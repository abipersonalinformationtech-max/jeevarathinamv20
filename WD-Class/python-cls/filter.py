#eligible for vote using filter()
def eligible(vote):
    if vote >= 18:
        return True
    else:
        return False
age=[22,19,17,23,15,30]
result=list(filter(eligible,age))
print(result)
print()

#eligible for vote by user input using filter()
def eligible(vote):
    if (vote>=18):
        return True
    else:
        return False
age=input("Enter age: ").split()
numbers = [int(n) for n in age]
result=list(filter(eligible,numbers))
print(result)
