#!/usr/bin/env python3

#import random
import random


def runGame():
        # create arr that holds choices
    choices = ["rock", "paper", "scissors"]

    # create a random index to get cpu answer
    randIdx = random.randint(0, 2)

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
        print("********")
        # Conditions
        if playerChoice == "rock" and cpuChoice == "scissors":
            print(f"Player Choice: {playerChoice} , CPU choice {cpuChoice}, You won!!")
            playerScore += 1
         
            
        elif playerChoice == "paper" and cpuChoice == "rock":
            print(f"Player Choice: {playerChoice} , CPU choice: {cpuChoice}, You won!!") 
            playerScore += 1
           
           
        elif playerChoice == "scissors" and cpuChoice == "paper":
            print(f"Player Choice: {playerChoice} , CPU choice: {cpuChoice}, You won!!")
            playerScore += 1
           
         
        else:
            print(f"Player Choice: {playerChoice} , CPU choice: {cpuChoice}, Sorry, try again!")    #loser handling
            playerScore -= 1
            if playerScore < 0:
                playerScore=0
      
  
        # any input error handling
    else:
        print("Please pick a valid choice: Rock, Paper, or scissors")

    return playerScore
    
# intro to game 
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
      
     

     





