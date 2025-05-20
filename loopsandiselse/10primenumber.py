n=int(input("Enter a number"))
n1=int(input("Enter second number"))
n2=n+1
i=1
while(i<=n1):
    temp=n2
    cnt=0
    j=1
    while(j<temp):
        if(temp%j==0):
            cnt+=1
        j+=1
    if(cnt==2):
        print("it is a prime number",temp)
        i+=1    
    n2+=1

    #sequence in paython list touple set frozen set dictiory
    #string in paython
    # string i