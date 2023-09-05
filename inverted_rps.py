import random

choices = ["R", "P", "S"]
compChoice = ""
playChoice = ""

def compTurn():
    compChoice = random.choice(choices)
    print(compChoice)
    return compChoice

def playerTurn():
    return

def playGame():
    return

compTurn()
print(compChoice)