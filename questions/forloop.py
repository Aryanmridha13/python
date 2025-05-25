#q1 print hello n time
# n = int(input("Enter a number"))
# for i in range(1,n+1):
#     print("Hello")

# q2 print natural number till n

# n=int(input("enter a number"))
# sum=0
# for i in range(n,0,-1):
#     # sum=sum+i
#     print(i)
# # print(sum)    

#Q3 print table
# n=int(input("enter a number"))
# for i in range(1,11):
#     print(f"{n}*{i}={n*i}")

#Q4factorial

# n=int(input("enter a number"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i

# print(fact)    

# n=int(input("Enter  a number"))
# isEven=0
# isOdd=0

# for i in range(1,n+1):
#     if(i%2==0):
#         isEven=isEven+i
#         print("Even",i)
#     else:
#         isOdd=isOdd+i
#         print("odd",i)
# print(f"even sum ={isEven}")            
# print(f"odd sum ={isOdd}")    


#Q factors

# n=int(input("Enter a number"))
# fact=0
# sum=0

# for i in range(1,n):#n+1 karne par factor nikal jayega
#     if(n%i==0):
#         fact=fact+1
#         sum=sum+i
#         print(i)
# if(sum==n):
#     print("it is perfact num ")
# else:
#     print("not a parfact num")            
# print(fact)        
# print(sum)    

# Q prime

# n=int(input("enter a n"))

# cnt=0
# for i in range(1,n+1):
#     if(n%i==0):
#         cnt=cnt+1
# if(cnt==2):
#     print("Prime")   
# else:
#     print("not Prime")        



#Q fibonaki
# a=-1
# b=1
# for i in range(1,n+1):
        # c=a+b
        # a=b
        # b=c
        # print(c)

#Q reverse

n="Sherhi"
x=len(n)
for i in range(len(n)-1,-1,-1):
    print(n[i])
# print(n[::-1])
    
     