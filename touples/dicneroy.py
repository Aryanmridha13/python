# dicntory is collection of objects in key value pairs

# d={100:"shyam",200:"ram",300:"ashish",400:"mohan"}
# print(d)
# print(d[100])
# for i in d.values():
#     print(i)
# for j in  d.keys():
#     print(j)

# write a program to take empty dictnory and add data from user

# e={}
# m=int(input( "Enter the no of data " ))
# for i in range(m):
#     k=input("Enter kes :")
#     v=input("Enter value :")
#     e[k]=v

# print(e)
# d1={100:"a",200:"t"}
# print(d1)
# d2={200:"Hello",300:"Bhopal",400:"namaste"}
# print(d2)
# d1.update(d2)
# print(d1)
# d1.pop(200)
# print(d1)
# d1.popitem()

d={'100':'value1','200':"value2"}
print(d.get('100'))
print(d.items())
for i,j in d.items():
    print(i,"--->",j)

d1=d.copy()
print(d1)
d.clear()    
print(d)