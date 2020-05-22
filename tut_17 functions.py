"""
a=5
b=6
c=sum((a,b))#builtin
print(c)
"""
#
def functionf1():
    print("hello function 1")

def function2(a,b):
    print("in function 2: ",a+b)

def function3(a,b):
    """this function returns avg of 2 numbers"""
    #it called doc string which is like coment but u can prrint it using  function3.__doc__
    avg=(a+b)/2
    print(avg)
    return avg

functionf1()
print("function1 returns:",functionf1())
function2(5,7)
print("function2 returns",function2(2,3))
print(function3(4,8))
print("function3 returns:",function3(4,8))

function3(7,3)

print(function3.__doc__) #if there are multiple files and u hv to chk wht specific function does