# l1=list()
# print(type(l1))
# l1.append(12)
# print(l1)

# l2=[]
# n=int(input("Enter the no of data ;"))
# for i in range(n):
#     print("Enter the ",i+1,"Data ;")
#     data=input("enter the data :")
#     l2.append(data)

# print(l2)    

# v=[]
# c=[]
# n=int(input("Enter no of data"))
# for i in range(n):
#     data=input("Enter data")
#     data1=data.upper()
#     if(data1=="A" or data1=="E" or data1=="I" or data1=="u" or data1=="u"):
#         v.append(data1)
#     else:
#         c.append(data1)    

# print("vovwel =",v)        
# print("consonent =",c)     

l1=[12,34,25,67,89,54]
x=max(l1)
print(x)
y=min(l1)
print(y)
l1.sort()
print(l1)
l1.reverse()
print(l1)
z=l1.pop()
print(l1)
l1.insert(0,45)
print(l1)
i=l1.index(45)
print(i)

