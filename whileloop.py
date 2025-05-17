i=1
while(i<=10):
    print(i)
    i+=1
print("this is last digit to check",i)    

# wrie a program to fine a factorial of a number input taking form the user
fact=1
a = 1
sum=0
num = int(input("Enter a number"))
while(a<=num):
    fact=fact *a 
    sum+=fact #a  
    a+=1
print(f"factorial ={fact}")
print(f"sum ={sum}")

# write a program to reverns the number taken from the user
n = int(input("Enter numbers"))
rev=0
sum =0
while(n>0):
    r=n%10
    rev=rev*10+r
    n=n//10
    sum=sum+r
print(rev) 
print(sum)   

# write a program to check input number is prime or not

pnum = int(input("Enter a number"))
i=2
while(i>=pnum):
    if(pnum/i==0):
        print("Number is not prime")
        break    
    else:
        print("number is  prime") 
        break   
    i+=1

