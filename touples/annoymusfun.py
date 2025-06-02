# a function in python we can create a function having whitout name is knoe as annomuse function
# aisa function jiska koie nam nahi hota
# lamda,filter,reduse example of ananoums function
# lamda is single line function isme return karane ki jarurt nai hoti hai 
# filter  

x=lambda a,b:a if a>b else b
print(x(20,20))

# write a program to find maximum from three input taken from user using lamda function
y=lambda a,b,c:a if (a >= b and a >= c) else (b if b >= c else c)
a=int(input("enter num "))
b=int(input("enter num "))
c=int(input("enter num "))
print(y(a,b,c))

# filter function 
# the filter function returns on itretion where the item are filtered throug a function to tast 
# itam is accepted or not
# when we using filter function minimum
# remove all the empty string from the list using filter function

name=['raj','','man','','raj','']
def mydata(ldt):
    if(ldt==''):
        return False
    else:
        return True
    
mylist=filter(mydata,name)
print(list(mylist))    