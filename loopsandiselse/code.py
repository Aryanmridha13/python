#writ a program to take two input from the user and after the
#input of second find all the palindron number of second input times

n=int(input("Enter first number"))
n1=int(input("Enter second number"))
n3=n+1
i=1
while(i<=n1):
    temp=n3
    rev=0
    while(temp>0):
        r=temp%10
        rev=rev*10+r
        temp=temp//10
    if(rev==n3):
        print("palindron num =",rev)
        i+=1
    n3+=1        


