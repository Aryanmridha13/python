def myfun():
    print("this is the first type of function")
#no return no argument function  

myfun()

#write a program to find the number having 4 factor 
# or not between to two input taking from use and using 
# no return with argument function

def four_factor(n1,n2):
    for i in range(n1,n2+1):
        cnt=0
        for j in range(1,i+1):
            if(i%j==0):
                cnt+=1
        if(cnt==4):
            print(i)

n1=int(input("Enter a number1 :"))                    
n2=int(input("Enter a number2 :"))
four_factor(n1,n2)   

# third type


def return_without_argument():
    a=13
    b=12
    c=34
    d=23
    return a,b,c,d

x=return_without_argument()
ad=0
for i in x:
    ad=ad+i
    print(i)
print(ad)    


# fourth type

