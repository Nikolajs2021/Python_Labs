"""
# Author: L00170289
# Week 2 - 30/09/2021
# Python Loops and Selection Structures
# Q1 - Guessing Game
"""

print("Guess the number\n")
hidden_number = int(input("Player 1: Pick a number from 1 to 10 for player 2 to guess: "))
print("\n" * 100)
print("Player 2: Guess the number that player 1 picked\n")
attempt = int(input("Enter your guess:  "))
count = 1
while attempt != hidden_number:
    count += 1
    print("!" * 50)
    attempt = int(input("Incorrect. Try again: "))
    print("You've entered",count , "attempts")
print("\n" * 10)
print("="*50)
print("You're correct, the hidden number was", hidden_number)
print("You guessed correctly in", count , "attempts.")
print("="*50)
