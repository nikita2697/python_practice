"""
print pattern
take input of number of lines
and one boolean char
if boolean true and lines =4
*
**
***
****

if false
****
***
**
*

"""
"""
while(True):
    no_of_lines = int(input("enter number of lines to print pattern: "))
    boolean_var = int(input("enter 1 or 0 to print pattern or e to exit: "))

    i = 0
    if(bool(boolean_var)):
        while(i<=no_of_lines):
            j=0
            while(j<i):
                print("*",end="")
                j+=1
            print("")
            i+=1
    else:
        while (i <= no_of_lines):
            j = no_of_lines
            while (j > i):
                print("*", end="")
                j -= 1
            print("")
            i += 1
"""
"""
num=int(input("number of lines:"))
boolean=bool(int(input("enter 0 or 1:")))
if boolean:
    for i in range(0,num+1):
        print("*"*i)
else:
    for i in range(num+1,1,-1):
        print("*"*i)

"""
num=int(input("number of lines:"))
boolean=bool(int(input("enter 0 or 1:")))
def star(num,boolean):
    if boolean==True:
        c=1
        while(c<num+1):
            print("*"*c)
            c+=1

    else:
        c=num
        while(c>0):
            print("*"*c)
            c -= 1
star(num,boolean)


