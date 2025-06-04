# print all nagetive and positive number in alist

# li=[1,2,-3,-4,5-6,-3,-2,1,56,45,-78]
# for i in li:
#     if(i>0):
#         print(f"positive num ={i}")

# for i in li:
#     if(i<0):
       
#         print(f"negative num ={i}")  

   
# a=[12,34,2,3,4,5,67,89,3]
# b=len(a)
# print(b)
# sum=0
# for i in a:
#     sum=sum+i

# print(sum)    
# print(sum/b)    

# largest number in a list

l=[1,2,3,4,56,78,3,2,4,56,789,6,79]
b=len(l)
large=l[0]
seclarge=l[0]
index=0

for i in range(b):
    if(l[i]>large):
        seclarge=large
        large=l[i]
        index=i
    elif(l[i]>seclarge):
        seclarge=l[i]    
    

print(f"largest i {large} and seclarge is {seclarge}")

