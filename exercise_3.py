#guessing number game for practice
"""
9 guesses
take user i/p number
print left choices
if guess is correct print in how mny guesses he won
"""
n=18
print("guess the number in 9 chances")
i=0

while i<=9:
    i=i+1
    j=int(input("enter number:"))
    if(j==18):
        print("correct number!!!")
        print("you won in",i,"guesses")
        break
    elif(j<18):
        print("no the number is greater than ",j)
        print("choices left",9-(i))
    else:
        print("number is less than",j)
        print("choices left", 9 - (i))
print("game over !!!")

