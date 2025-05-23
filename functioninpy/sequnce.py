#sequence in python
#list
#tuple
#set
#frozen set
#dictnory

# List= is a data type 
# whenever we want to represent a group of indivisual entity or object in an single entity
#then we can implement a list
# 2 insersation order in list is priserved 
#3 list are mutable means changes are allowed 
#4 in list hetroginus as well as homoginus objects are allowe
# syntax of list => li=[o1,o2,o3,o4,o5]

l=[12,23,34,45,56,67,6,77]
x=len(l)
print(x)
for i in range(x):
    for j in range(i+1,x):
        if(l[i]>l[j]):
            l[i],l[j]=l[j],l[i]
            # temp=l[i]
            # l[i]=l[j]
            # l[j]=temp

print(l)
