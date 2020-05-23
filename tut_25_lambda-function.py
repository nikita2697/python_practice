#lambda function or anonymous function:its a one liner function

def add(a,b):
    return a+b
print("using functon",add(3,4))

add1=lambda a,b:a+b
print("using lambda",add1(4,5))

a=[[3,8],[4,5],[6,9]]
def a_ssort(a):
    return a[-1]
a.sort(key=a_ssort)
print(a)