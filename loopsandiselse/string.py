s=input("Enter the string")
vcnt=0
ccnt=0
x=s.lower()
for i in x:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        vcnt+=1
    else:
        ccnt+=1
print("vovels =",vcnt)            
print("consonent =",ccnt)            