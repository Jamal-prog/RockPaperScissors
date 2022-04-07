#!/usr/bin/env python3

#import random
import random


def runGame():
        # create arr that holds choices
    choices = ["rock", "paper", "scissors"]

    # create a random index to get cpu answer
    randIdx = random.randint(0, 2)

    # create a default starting score
    playerScore = 0 

    # grab random index from choices
    cpuChoice = choices[randIdx]

    print("---------------------------------------")

    # saves player input and make it all lowercase for conditional purpose
    playerChoice = input("What is your choice? Rock, Paper, or Scissors - ").lower()

    
    if playerChoice in choices:
        print("ROCK")
        print("PAPER")
        print("SCISSORS")
        print("")
        # Conditions
        if playerChoice == "rock" and cpuChoice == "scissors":
            print(f"Player Choice: {playerChoice} , CPU choice {cpuChoice}, You won!!")
            rockImg()
            scissorsImg()
            playerScore += 1
         
            
        elif playerChoice == "paper" and cpuChoice == "rock":
            print(f"Player Choice: {playerChoice} , CPU choice: {cpuChoice}, You won!!") 
            paperImg()
            rockImg()
            playerScore += 1
           
        elif playerChoice == "scissors" and cpuChoice == "paper":
            print(f"Player Choice: {playerChoice} , CPU choice: {cpuChoice}, You won!!")
            scissorsImg()
            paperImg()
            playerScore += 1
           
        elif playerChoice == cpuChoice:
            print(f"Player Choice: {playerChoice}, CPU choice: {cpuChoice}, There is a tie!")
        else:
            print(f"Player Choice: {playerChoice} , CPU choice: {cpuChoice}, Sorry, try again!")    #loser handling
            playerScore -= 1
            if playerScore < 0:
                playerScore=0

        # any input error handling
    else:
        print("Please pick a valid choice: Rock, Paper, or scissors")

    return playerScore
    
def rockImg():
    # ascii art for Rock     
   print("""
        _______
    ---'   ____)
          (_____) 
          (_____)
          (____)
    ---.__(___)
    """)

def paperImg():
    # paper ascii art
    print("""
        _______
    ---'    ____)____
               ______)
              _______)
             _______)
     ---.__________)
    """)

def scissorsImg():
    # scissors ascii art
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)   

# intro to game 
rockImg()
paperImg()
scissorsImg()
run = input("Welcome to Rock, Paper, Scissors, Do you wish to begin yes/no? ").lower()
score = 0
if run == "yes":
   while True:
        gameScore = runGame()
        print("---------------------------------------")
        # end game prompt
        endGame = input("Type 'end' to end game or press anything else to keep playing: ").lower()
        # end game condition
        if endGame == "end":
            score += gameScore
            print(f"Player Score: {score}")
            break
        else:
            score += gameScore
elif run == "no":
    print("Restart game to continue")
      
     

     





