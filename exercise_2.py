"""
faulty calculator:
45*3=555,56+9=77,56/6=4 these calcullations should be wrong
"""
while(1):
    operator=input("enter operator")
    num1=int(input("enter first num"))
    num2=int(input("enter second num"))
    if (operator == "+"):
        if num1==56 and num2==9:
            print("77")
        else:
            print(num1+num2)
    elif operator=="-":
        print(num1-num2)
    elif operator=="*":
        if num1==45 and num2==3:
            print("555")
        else:
            print(num1*num2)
    else:
        if num1==56 and num2==6:
            print("4")

        else:
            print(num1/num2)
