d={}


while(True):
    print('''             press 1 to add
             press 2 to read
             press 3 to update
             press 4 to remove
             press 5 to exit
            ''')
    
    ch=int(input("Enter your choice "))
    if(ch==1):
        n=int(input("Enter no of data to add"))
        for i in range(n):
            print(f"data {i+1}")
            k=input("Enter keys")
            v=input("Enter values")
            d[k]=v
        print(d)    
    elif(ch==2):
        print(d)
    elif(ch==3):
        n = int(input("Enter no of data to update"))
        for i in range(n):
            k=input("enter keys")
            v=input("Enter value")
            d1={}
            d[k]=v
            d.update(d1)

        
    elif(ch==4):
        n=int(input("ENter no of data to remove"))

        for i in range(n):
            k=input("Enter keys to remove")
            d.pop(k)
    elif(ch==5):
        print("Exit")
        break
    else:
       print("wrong input")
       continue

    
    
