import random

target= random.randint(1, 100)

while True:
    userChoice = int(input("Guess the target or Quit(Q) :"))
    if(userChoice == "Quit"):
        break
    
    userChoice = int(userChoice)
    if(userChoice == target):
        print("Sucess : Correct Guess!!")
        break
    elif(userChoice < target):
        print("Your number was too small .Take a bigger guess....")
    else:
        print("Your number was too big .Take a smaller guess....")
        
        print("-----GAME OVER------")
