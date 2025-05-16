p=float(input("Enter the marks of Physics :"))
c=float(input("Enter the marks of Chemistry :"))
m=float(input("Enter the marks of Maths :"))

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
elif((p<33 and c<33 and m>=33) or(p<33 and c>=33 and m<33) or (p>=33 and c<33 and m<33)):
    if((p<33 and c<33 and m>=33) ): 
      print("you are fail in Physics =",p,"\n""you are fail in Chemistry =",c)  
    elif((p<33 and c>=33 and m<33)):
          print("you are fail in Physics =",p,"\n"" and you are fail in Maths =",m)  
    elif( (p>=33 and c<33 and m<33)):
          print("you are fail in Chemistry =",c,"\n"" and you are fail in Maths =",m) 
elif((p<33 and c<33 and m<33)) :
    print("you are fail in All three subject")
    print("you are marks is Physics =",p)
    print("you are marks is Chemistry =",c)
    print("you are marks is Meths =",m)
else:
    if(per>=60):
        print("your are Persentage =",per)
        print("your are Total Marks is =",total_marks)
        print("you are pass in 1st Division") 
    elif(per>=45):
        print("your are Persentage =",per)
        print("your are Total Marks is =",total_marks)
        print("you are pass in 2nd Division")  
    elif(per>=33):
        print("your are Persentage =",per)
        print("your are Total Marks is =",total_marks)
        print("you are pass in 3rd Division")         
