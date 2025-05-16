n= int(input("Enter any number"))
oans =0
eans=0
i=1
#while(i<=n):
    #ans=ans+i
    #print(ans)
   # i+=1
while(i<=n):
     if(i%2==0):
          eans=eans+i
         
     else:
          oans=oans+i  
        
     i+=1 

print("Even",eans)
print("Even",oans)