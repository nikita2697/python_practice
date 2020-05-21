"""
var = 6
var1=56
var3=int(input("enter number:"))
if var3>var1:
    print("greater")
elif var3==var1:
    print("equal")

else:
    print("less")

list1=[5,7,3]
if 15 not in list1:
    print("not  is in")
"""
#quize:take age val and decide can or can't drie

age=int(input("enter age:"))
if age > 7 and age < 77:
    if age>18:
        print("u can drive")
    elif age==18:
        print("can't decide bcz ur age is not less than 18 nor grtr than 18")
    else:
        print("you can't drive")
else:
    print("enter valid age:(between 7 to 77)")