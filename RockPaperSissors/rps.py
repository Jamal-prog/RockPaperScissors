#!/usr/bin/env python3

#import random
import random


def runGame():
        # create arr that holds choices
    choices = ["rock", "paper", "sissors"]

   

    # create a random index to get cpu answer
    randIdx = random.randint(0, 2)

    # grab random index from choices
    cpuChoice = choices[randIdx]
    
  

    print("---------------------------------------")
    # saves player input and make it all lowercase for conditional purpose
    playerChoice = input("What is your choice? Rock, Paper, or Sissors - ").lower()

    
    if playerChoice in choices:

        # Conditions
        if playerChoice == "rock" and cpuChoice == "sissors":
            print(f"Player Choice: {playerChoice} , CPU choice {cpuChoice}, You won!!")
           
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            
        elif playerChoice == "paper" and cpuChoice == "rock":
            print(f"Player Choice: {playerChoice} , CPU choice: {cpuChoice}, You won!!") 
           
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
           
        elif playerChoice == "sissors" and cpuChoice == "paper":
            print(f"Player Choice: {playerChoice} , CPU choice: {cpuChoice}, You won!!")
            
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
         
        else:
            print(f"Player Choice: {playerChoice} , CPU choice: {cpuChoice}, Sorry, again!")    #loser handling
            
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
           
        # any input error handling
    else:
        print("Please pick a valid choice: Rock, Paper, or scissors")
    
# intro to game 
run = input("Welcome to Rock, Paper, Scissors, Do you wish to begin yes/no? ").lower()
x = True
if run == "yes":
   while x:
        runGame()
        print("---------------------------------------")
        # end game prompt
        endGame = input("Type 'end' to end game or press enter to keep playing: ").lower()
        # end game condition
        if endGame == "end":
            break
     

     





