import random

def guess_number():
    num = random.randint(1,101)
    return num
print("Welcome to the number guessing game: ")
print("I am thinking of a number of between 1 to 100: ")
actual_num=guess_number()
difficulty_level=input("Choose a difficulty : Type 'easy' or 'hard': ")

if difficulty_level.lower()=='easy':
    is_game_over=False
    attempts=10
    while not is_game_over:
        print(f"You have {attempts} attempts remaining")
        guess=int(input("Make a guess: "))
        attempts-=1
        if guess<actual_num:
            print("Too low.\nGuess again.")
        elif guess>actual_num:
            print("Too high.\nGuess again.")
        else:
            print("You won!")
            is_game_over=True
            
        if attempts==0:
            is_game_over=True
    
else:
    is_game_over=False
    attempts=5
    while not is_game_over:
        print(f"You have {attempts} attempts remaining")
        guess=int(input("Make a guess: "))
        attempts-=1
        if guess<actual_num:
            print("Too low.\nGuess again.")
        elif guess>actual_num:
            print("Too high.\nGuess again.")
        else:
            print("You won!")
            is_game_over=True
            
        if attempts==0:
            is_game_over=True
    
            
    