# an ecxception can be defind as an un useable condition in a program resulting\intruption in the flow of the program
# whenever an exception occers the program stops the exicution and thus the forther code is not ececuted .
#  ther for an exception is the run time error that are unable to handel python script

# an ecception in a python is an object that represent and error there is basicaly two types of error

# syntax error and logical error

# try an accept case
a = int(input("Enter num a"))
b= int(input("Enter num b"))

try:
    c=a/b
    print(c)
except:
    print("Zero is divisible nahi hota hai ra baba fir se try karo")
finally:
    print("jai ho")

# common exception python provide the numbers of exception but here be are discribing common 
# a list of common exception that can br througn fro a standers python program is givin bliw zero division error
# name error = when a name is not define or found it may be local or global 
# indentation erro
# input output error
#   epf erro=end of file error


        