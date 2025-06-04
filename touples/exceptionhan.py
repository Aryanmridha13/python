# rexing exception

#  an exception can be rese forsefully by using the raire close in python it is usefull
# in thai sinaruo where we need to rase an exception to stop the excucation of the erro
  
# try:
#     age=int(input("Enter you age"))
#     if(age<18):
#         raise ValueError
#     else:
#         print("Valid age")
# except ValueError:
#     print("Value not valid ",ValueError)      

# file handling in python
# file handling is an important part of any web scripting language. python has capability to handel a file python we can creat a new file 
# to handel a file first we open  a method to opening a file using method

# f=open("loop.py")
# print(f.read())
# print(f.read(10))#khan tak ke charecter read karna hai
# print(f.readline())

# mode of file
# small R = read onlay mode this is read the file if file not exist this mode generate the error
# write mode= it is used to update the data and if filw dosnt exis it create new file and store the data to new file
# apend mode= data shoude be added last of the file if file dosnt exist it create a file and store tha data
# x mode(write mode)=if file dosnt exit create the file and add the data if old file is exit than it dosnt change the file

#  make a file manegment system using file handling 
f=open("text.txt","w")
f.write("ashish gandu")