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

while(True):
    no_of_lines = int(input("enter number of lines to print pattern"))
    boolean_var = int(input("enter 1 or 0"))
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






