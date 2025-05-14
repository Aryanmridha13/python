p=float(input("Enter the marks of Physics :"))
m=float(input("Enter the marks of Maths :"))
c=float(input("Enter the marks of Chemistry :"))
total_marks=p+m+c
per=(total_marks/3)
if (p<0 or c<0 or m<0 or p>100 or c>100 or m>100):
    print("you enter invelid number ") 
elif((p<33 and c>=33 and m>=33) or (p>=33 and c<33 and m>=33) or (p>=33 and c>=33 and m<33)) :
    if((p<33 and c>=33 and m>=33)):
        print("you are fail in Physics =",p)
    elif((p>=33 and c<33 and m>=33)) :
        print("you are fail in Chemistry =",c)
    elif((p>=33 and c>=33 and m<33)):
        print("you are fail in Meths =",m)
     
