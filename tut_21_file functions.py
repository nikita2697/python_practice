"""
f=open("nikita.txt")
print(f.tell())#tells where is f pointer
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0)#set pointer to desired character's position
print(f.tell())
print(f.readline())
f.close()
"""
with open("nikita.txt") as f:
    print(f.readlines())

