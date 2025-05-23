def myfunc(x,y):
    print(f"x={x} and y={y}")
myfunc(y=14,x=34)

#
def myfun1(*n):
    add=0
    for i in n:
        add=add+i
    print("sum =",add)

myfun1(10,20,25)

#the function whic has no name or name as know as anano,as function or lemda function
#note= lemda function is one line function by defulat the lemda function is return with argument 
#Note = lamda is a reserve keyword

s=lambda x:x*x
print(s(10))
a1=lambda a,b:a if a>b else b
print(a1(10,20))
