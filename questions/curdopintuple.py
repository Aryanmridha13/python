l=()
l1=list(l)
while True:
    print(''' 
         press 1 to creat :
         press 2 to read :
         press 3 to update :
         press 4 to remove :
         press 5 to exit :
         wrong input :
            
''')
    ch=int(input("Enter your choice :"))
    if(ch==1):
        num=int(input("Enter no of data to insert :"))
        for i in range(num):
            print(f"data is {i+1}")
            data=int(input("Enter the data"))
            l1.append(data)
    elif(ch==2):
        print(l1)
    elif(ch==3):
        num=int(input("Enter no  of data to update = "))
        for i in range(num):
            print(f"enter data {i+1}")
            data=int(input("Enter actual data to update  "))
            c=l1.index(data)
            data1=int(input("enter data to update :"))
            l1[c]=data1

    elif(ch==4):
        num=int(input("Enter no of data to remove1 :"))
        for i in range(num):
            print(f"data is {i+1} =")
            d=int(input("Enter the data"))
            l1.remove(d)
    elif(ch==5):
        print("Exit")   
        break
    else:
        print("Wrong input")
        continue    

l=tuple(l1)        
print(l)      
