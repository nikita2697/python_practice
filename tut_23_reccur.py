#recurrsion
"""
def fact_itterative(n):
    fact = 1
    for i in range(1 , n+1):
        fact=fact*i
    return fact
def fact_recurrsive(n):
    fact=1
    if(n==1):
        return 1
    else:
        return n*fact_recurrsive(n-1)

a=int(input("enter number:"))

print("factorial using itterative function:",fact_itterative(a))
print("factorial using recurrsive function:",fact_recurrsive(a))
"""
def fibbo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibbo(n-1)+fibbo(n-2)
for i in range(0,5):
    print(fibbo(i))

print("n th fibbo",fibbo(4))