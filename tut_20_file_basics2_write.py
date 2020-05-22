#file write
"""
f =open("nikita2.txt","w")
#f.write("nikita file") #if u again run f.write it wil overwrit content
f.write("hello world")
f.close()

"""
#file append

"""
f =open("nikita.txt","a")
#f.write("nikita file") #if u again run f.write now it will not  overwrit content it will append at end
f.write("\nhello world")#f.write return number of chr u cn store in var and print
f.close()
"""
#read write both

f=open("nikita.txt","r+")
#f.write("nikita file") #if u again run f.write now it will not  overwrit content it will append at end
#f.write return number of chr u cn store in var and print
print(f.read())
f.write("hello world")
f.close()

