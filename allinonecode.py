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
        
