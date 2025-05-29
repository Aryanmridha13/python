d={}


while(True):
    print(''' press 1 to add
             press 2 to read
             press 3 to update
            press 4 to remove
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
        print("read")
    elif(ch==3):
        print("update")
    elif(ch==4):
        print("remove")
    elif(ch==5):
        print("Exit")
        break
    else:
       print("wrong input")
       continue

    
    
