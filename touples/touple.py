#when we want to repreent group entity in a ingle entity
#haowhere insertion order is presrved and homogenous and hytoginous
#ob is to be allowed than we can implement the tuple

# touple are immutable changes will not allowed 

tp=('a','b','c','d','e')
print(type(tp))

tp1=list(tp)
print(tp1)
tp1.append(12)
print(tp1)
tp=tuple(tp1)
print(tp)
# list comfrihention and tuple comfrihention 

ls=[i for i in range(1,11)]
print(ls)
ls1=(i for i in range(1,11))
print(ls1)


