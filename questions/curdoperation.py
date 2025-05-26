ls=[]
while(True):
    print(''' 
           press 1 for createt:
          press 2 for read :

''')
    ch=int(input("Enter your choice"))
    if(ch==1):
        n=int(input("Enter the no of data :"))
        for i in range(n):
            print(f"enter the {i+1} data :")
            data=input("Enter the data")
            ls.append(data)
    elif(ch==2):
        print("here is the data")
        print(ls)
    elif(ch==3):
        n=int(input("Enter the no of data :"))
        for i in range(n):
            print(f"enter the {i+1} data :")
            data=input("Enter the data")
            x=ls.index(data)
            data1=input("Enter the data to update")
            ls[x]=data1
    elif(ch==4):
        n=int(input("Enter the no of data :"))
        for i in range(n):
            print(f"enter the {i+1} data :")
            data=input("Enter the data")
            ls.remove(data)
    elif(ch==5):
        print("Exit")
        break
    else:
        print("Wrong input")
        continue        

