guesses=0
from random import randint
number = randint(1,10)
print("Guess a number between 1 and 10")
guess = int(input())
guesses=guesses+1
while guess != number and guesses < 3:
  print("Incorrect")
  print("Guess a number between 1 and 10")
  guess = int(input())
  guesses=guesses+1
if guess == number:
  print("Correct")
  print("You took", guesses, "guesses")
else:
  print("The correct number is ", number)
  print("Guess limit reached")