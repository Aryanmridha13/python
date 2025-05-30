# list in python
# basic list method 
a=[1,2,5,6,7,8,3,9]
b=len(a)
for i in range(b):
    print(a[i]) 

a.append(15)
a.extend([2,4,7])
a.insert(0,3)
print(a)
a.remove(3)
print(a)
a.pop(5)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.reverse()
print(a)
a.clear()
print(a)