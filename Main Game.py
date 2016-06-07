from random import randint

# randomint = random integer between 0,100
randomint = (randint(0, 100))
print("Hi,Guess No. Between 0,100")
print("Happy Guessing :D")
print("You Have 5 Chances")
print("Let's Go")
# c = chances
print(randomint)
c = 5
c = (int(c))
# maxsc = max score
maxsc = 1500
maxsc = (int(maxsc))
continuex=True
print("You Will Win If You Get In The First Time With Score:1500.Good Luck :) ")
# inrandomint = input random integer anddddddddddddddddd i have changed to integer
inrandomint = int((input("Guess: ")))
while continuex == True :
    if inrandomint == randomint:
        print("Good Job")
        print("You Make It")
        print("You Are AWESOME")
        print("Score : %d" % (maxsc))
        print("From %d Chances" % (c))
        continuex=False
    elif inrandomint != randomint and 0 < inrandomint < 100:
        inrandomint = int((input("Guess: ")))
        print("Wrong :(")
        c -= 1
        maxsc -= 300
        print("You Have %d Chances" % (c))
        print("Your Score Is %d" % (maxsc))
        if c == 0:
            print("Game Over")
            continuex = False
            print("Try Again Later")
            print("Score : %d" % (maxsc))
            exit()
            print("You Have %d Chances" % (c))
            print("Your Score Is %d" % (maxsc))
        elif inrandomint < 50 and randomint < 50:
            print("Still There It Is Less Than 50")
        elif inrandomint > 50 and randomint > 50:
            print("Still There It Is More Than 50")
        elif inrandomint < 50 and randomint > 50:
            print("Hint:It Is More Than 50")
        elif inrandomint > 50 and randomint < 50:
            print("Hint:It Is Less Than 50")
else:
    print("GoodBye!!")









