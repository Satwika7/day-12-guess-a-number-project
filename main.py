import random
from replit import clear
from art import logo
def game():
  print(logo)
  cont="no"
  print("Welcome to number guessing game!\nI am thinking of a number between 1 and 100.")
  level = input("chosse a difficulty. Type 'easy' or 'hard': ").lower()
  value = random.randint(1,100)
  if level=="easy":
    chances=10
  else:
    chances=5
  def chance_left():
    return chances-1
  game_end = False
  while not game_end and chances>=0:
    if chances==0:
      game_end=True
      print("you lost, game ended")
      cont = input("do you want to play again type 'yes' or 'no'.: ").lower()
    else:  
      print(f"you have {chances} chances left to guess a number")
      guess = int(input("make a guess: ")) 
      if guess==value:
        print(f"you win, you guessed the number {guess}.")
        cont = input("do you want to play again type 'yes' or 'no'.: ").lower()
        game_end=True
      else:
        if guess>value:
          print("Too High")
        else:
          print("Too Low")
        chances=chance_left()
    if cont=="yes":
      clear()
      game()
    
game()                    

