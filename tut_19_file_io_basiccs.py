#file basics
"""
r - read(default)
w - write
x - create if not exists
a - add more content
t - text mode(default)
b- binary mode
+ - read write
"""

# f= open("nikita.txt","rt")
# content=f.read(3)
# print("1st",content)
#
# content=f.read(3)
# print("2nd",content)

# f=open("nikita.txt")
# content=f.read()
# print(content)
# f.close # best prctice to close file if opned after use

#line by line read

# f = open("nikita.txt")
# for i in f:
#     print(i)
#
# f.close()

#character wise

# f = open("nikita.txt")
# content=f.read()
# for i in content:
#     print(i)
#
# f.close()


# linewise with readline function
# f = open("nikita.txt")
# print(f.readline())
# #print(f.readline())
# f.close()

# readlines:store line wise in list

f = open("nikita1.txt","w+")
content=f.readlines();
if f.tell()==0:
    print("nothing to read in file")
else:
    print(f.readlines())
#print(f.readline())
f.close()


