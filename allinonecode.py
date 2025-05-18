while(True):
    ch=int(input("Enter a choice"))
    if(ch==1):
        n=int(input("Enter a number"))
        i=1
        cnt=0
        while(i<=n):
            if(n%i==0):
                cnt+=1
            i+=1
        if(cnt==2):
            print("Number is prime")
        else:
            print("not prime")
    elif(ch==2):
        n=int(input("Enter the no:"))
        i=1
        while(i<=10):
            print(n*i)
            i+=1
    elif(ch==3):
        n=int(input("Entet the no:"))
        i=1
        a=-1
        b=1
        while(i<=n):
            c=a+b
            a=b
            b=c
            print(c)
            i+=1  
    elif(ch==4):
        print
        n=int(input("enter a number"))
        rev=0
        temp=n
        while(n>0):
            r=n%10
            rev=rev*10+r
            n=n//10
        if(temp==rev):
            print("number is pelindron")
        else:
            print("number is not palindron")        
    elif(ch==5):
        n=int(input("Enter a number"))
        p=len(str(n))
        temp=n
        a_sum=0
        while(n>0):
            r=n%10
            a_sum=a_sum+r**p
            n=n//10
        if(temp==a_sum):
            print("Number is armstrong")
        else:
            print("Number is not armstrong")        
    elif(ch==6):
        n=int(input("Enter number"))
        rev=0
        temp=n
        while(n>0):
            r=n%10
            rev=rev*10+r
            n=n//10
        print("Revers of the number is =",rev,"and the number is=",temp)
    elif(ch==7):
        n=int(input("Enter a number"))
        sum_digit=0
        while(n>0):
            r=n%10
            sum_digit=sum_digit+r
            n=n//10
        print(f"sum of digit ={sum_digit}") 
    elif(ch==8):
        n=int(input("Enter a number"))
        fact=1
        i=1
        while(i<=n):
            fact=fact*i 
            i+=1
        print(f"Factorial of the number is {fact}") 
    elif(ch==9):
        m=int(input("Enter a number")) 
        sum_nmber=0
        i=1
        while(i<=m):
            sum_nmber=sum_nmber+i
            i+=1
        print(f"sum of number {sum_nmber}")
    elif(ch==10):
        n=int(input("Enter a number"))
        first_digit=0
        while(n<10):
            n=n//10 
            first_digit=n
        print(first_digit) 
