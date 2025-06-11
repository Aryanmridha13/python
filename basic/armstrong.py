# n=int(input("Enter a number"))
# r=n

# a=n%10
# n=n//10
# b=n%10
# n=n//10

# s=a**3+b**3+n**3

# if(r==s):
#     print("Aemstrong number",s)

# else:
#     print("not a armstrong number",s)

# write  a program to generate fibonaki serice

n=int(input("Enter a number"))
a=-1
b=1

for i in range(n):
    c=a+b
    a=b
    b=c
    print(c)
