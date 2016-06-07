from random import randint
#randomint = random integer between 0,100
randomint=(randint(0,100))
print("Hi,Guess No. Between 0,100")
print("Happy Guessing :D")
print("You Have 5 Chances")
print("Let's Go")
#c = chances
print(randomint)
c=5
c=(int(c))
#maxsc = max score
maxsc = 1500
maxsc =(int(maxsc))
print("You Will Win If You Get In The First Time With Score:1500.Good Luck :) ")
#inrandomint = input random integer anddddddddddddddddd i have changed to integer
inrandomint=int((input("Guess: ")))
if inrandomint == randomint:
    print("Good Job")
    print("You Make It")
    print("You Are AWESOME")
    print("Score : %d"%(maxsc))
    print("From %d Chances"%(c))
elif inrandomint != randomint and 0<inrandomint<100 :
        print("Wrong :(")
        c-=1
        maxsc-=300
        print("You Have %d Chances"%(c))
        print("Your Score Is"%(maxsc))
        if inrandomint<50 and randomint<50 :
            print("Still There It Is Less Than 50")
            inrandomint=int((input("Guess: ")))
            if inrandomint == randomint:
                print("Good Job")
                print("You Make It")
                print("You Are AWESOME")
                print("Score : %d"%(maxsc))
                print("From %d Chances"%(c))
            elif inrandomint != randomint and 0<inrandomint<100 :
                print("Wrong :(")
                c-=1
                maxsc-=300
                print("You Have %d Chances"%(c))
                print("Your Score Is"%(maxsc))
                if inrandomint<50 and randomint<50 :
                    print("Still There It Is Less Than 50")
                    if inrandomint == randomint:
                        print("Good Job")
                        print("You Make It")
                        print("You Are AWESOME")
                        print("Score : %d"%(maxsc))
                        print("From %d Chances"%(c))
                    elif inrandomint != randomint and 0<inrandomint<100 :
                        print("Wrong :(")
                        c-=1
                        maxsc-=300
                        print("You Have %d Chances"%(c))
                        print("Your Score Is"%(maxsc))
                        if inrandomint<50 and randomint<50 :
                            print("Still There It Is Less Than 50")
                            inrandomint=int((input("Guess: ")))
                            if inrandomint == randomint:
                                print("Good Job")
                                print("You Make It")
                                print("You Are AWESOME")
                                print("Score : %d"%(maxsc))
                                print("From %d Chances"%(c))
                            elif inrandomint != randomint and 0<inrandomint<100 :
                                    print("Wrong :(")
                                    c-=1
                                    maxsc-=300
                                    print("You Have %d Chances"%(c))
                                    print("Your Score Is"%(maxsc))
                                    if inrandomint<50 and randomint<50 :
                                        print("Still There It Is Less Than 50")
                                    elif inrandomint>50 and randomint>50 :
                                        print("Still There It Is More Than 50")
                                    elif inrandomint<50 and randomint>50 :
                                        print("Hint:It Is More Than 50")
                                    elif inrandomint>50 and randomint<50 :
                                        print("Hint:It Is Less Than 50")

                        elif inrandomint>50 and randomint>50 :
                            print("Still There It Is More Than 50")
                        elif inrandomint<50 and randomint>50 :
                            print("Hint:It Is More Than 50")
                        elif inrandomint>50 and randomint<50 :
                            print("Hint:It Is Less Than 50")

                elif inrandomint>50 and randomint>50 :
                    print("Still There It Is More Than 50")
                elif inrandomint<50 and randomint>50 :
                    print("Hint:It Is More Than 50")
                elif inrandomint>50 and randomint<50 :
                    print("Hint:It Is Less Than 50")

        elif inrandomint>50 and randomint>50 :
            print("Still There It Is More Than 50")
        elif inrandomint<50 and randomint>50 :
            print("Hint:It Is More Than 50")
        elif inrandomint>50 and randomint<50 :
            print("Hint:It Is Less Than 50")
else:
    print("No. Between 0,100")
    print("Close The Program And Open It Again")
    
            
        
        
        
        


