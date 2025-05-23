
def return_with_argument(a,b,c,d):
    
    return a,b,c,d

x=return_with_argument(12,34,56,78)
ad=0
for i in x:
    ad=ad+i
    print(i)
print(ad)    

#Note = when we delcare the function with having same name but
# passing paramite is diffrent this concept is know as function 
# overloading and python is dynamicaliy type so function 
# overloding should not supported

# Example

def myfun(a):
    return a

def myfun(b):
    return b
myfun(12)

# types of argument 
# default argument
#keyword argument
#positional argument
#variable length argument


