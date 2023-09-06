import random

choices = ["r", "p", "s"]
tieCount = 0

def compTurn():
    compChoice = random.choice(choices)
    return compChoice

def playTurn():
    playChoice = input("Choose Rock (R), Paper(P), or Scissors (S)").lower()
    choice = True
    
    while choice == True:
        if playChoice == "r":
            choice = False
            return playChoice
        
        elif playChoice == "p":
            choice = False
            return playChoice
        
        elif playChoice == "s":
            choice = False
            return playChoice
        
        else:
            print("Thats not a valid choice. \n")
            playChoice = input("Choose Rock (R), Paper(P), or Scissors (S)").lower()
        
    return playChoice

def playGame(gameNum):
    global tieCount
    win = 0
    while gameNum != 0:
        compChoice = compTurn()
        playChoice = playTurn()
    
        if tieCount % 2 == 0:
            if playChoice == "r" and compChoice == "s":
                gameNum -= 1
                win += 1
                print("Computer chose scissors. You won! \n")
            
            elif playChoice == "p" and compChoice == "r":
                gameNum -= 1
                win += 1
                print("Computer chose rock. You won! \n")
            
            elif playChoice == "s" and compChoice == "p":
                gameNum -= 1
                win += 1
                print("Computer chose paper. You won! \n")
                
            elif compChoice == playChoice:
                tieCount += 1
                print("Computer chose the same thing. You drew. \n")
                
            else:
                gameNum -= 1
                print("Computer won. \n")
            
        elif tieCount % 2 == 1:
            if playChoice == "r" and compChoice == "p":
                gameNum -= 1
                win += 1
                print("Computer chose paper. You won! \n")
            
            elif playChoice == "p" and compChoice == "s":
                gameNum -= 1
                win += 1
                print("Computer chose scissors. You won! \n")
            
            elif playChoice == "s" and compChoice == "r":
                gameNum -= 1
                win += 1
                print("Computer chose rock. You won! \n")
                
            elif compChoice == playChoice:
                tieCount += 1
                print("Computer chose the same thing. You drew. \n")
                
            else:
                gameNum -= 1
                print("Computer won. \n")
    
    return win

games = int(input("How many games do you want to play? (Enter a number)"))
wins = playGame(games)
print("You won " + str(wins) + " times.")