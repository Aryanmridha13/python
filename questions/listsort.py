#buble sort

i=[2,12,4,5,89,76,3,56,0,9,12,5]
x=len(i)
print(x)
for l in range(x):
    for j in range(l+1,x):
        if(i[l]>i[j]):
            i[l],i[j]=i[j],i[l]

print(i)
