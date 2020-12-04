#CODE BREAKER GAME
code=7090
answer1=0
answer2=9
answer3=0
answer4=5
print("This is a code breaker game")
print("Try breaking the code with the clue given")
while answer1!=7:
    answer1=int(input("Enter Your Code : "))
    if answer1 > 7 :
        print("Guess lower")
        print('Try Again')
    elif answer1 < 7:
            print("Guess higher")
            print("Try Again")
    elif answer1==7:
                print('You are right,try guessing the next code')
    else:
        print("Try Again")
while answer2!=0:
    answer2=int(input("Enter Your Code : "))
    if answer2 > 0 :
        print("Guess lower")
        print("Try Again")

    elif answer2 < 0:
            print("Guess higher")
            print('Try Again')

    elif answer2==0:
                print('You are right,try guessing the next code')
while answer3!=9:
    answer3=int(input("Enter Your Code : "))
    if answer3 > 9 :
        print("Guess lower")
        print('Try Again')
    elif answer3 < 9:
            print("Guess higher")
            print("Try Again")
    elif answer3==9:
                print('You are right,try guessing the next code')
while answer4!=0:
    answer4=int(input("Enter Your Code : "))
    if answer4 > 0 :
        print("Guess lower")
        print('Try Again')
    elif answer4 < 0:
            print("Guess higher")
            print("Try Again")
    elif answer4==0:
                print("Congratulations you have guessed all the code correctly and the code is 7090")
                break





