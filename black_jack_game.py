import random

def select_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice()
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(user_score,computer_score):
    
    if user_score>21 and computer_score>21:
        return "You lose!"
    elif user_score==computer_score:
        return "Draw!"
    elif user_score>21:
        return "You lose!"
    elif computer_score>21:
        return "You win!"
    elif user_score==0:
        return "You win with a blackjack"
    elif computer_score==0:
        return "You lose! computer has a blackjack"
    elif user_score>computer_score:
        return "You win!"
    else:
        return "You lose!"

def playgame():
    user_cards=[]
    computer_cards=[]
    game_over=False
    
    for i in range(2):
        user_cards.append(select_card())
        computer_cards.append(select_card())
    
    while not game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your cards{user_cards} current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")
        
        if user_score==0 or computer_score==0 or user_score>21:
            game_over=True
        else:
            user_add_extra_card=input("Type 'y' if user wants to add extra card or type 'n': ")
            if user_add_extra_card=='y':
                user_cards.append(select_card())
            else:
                game_over=True
    while computer_score!=0 and computer_score<21:
        computer_cards.append(select_card())
        computer_score=calculate_score(computer_cards)
    
    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_score(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=='y':
  playgame()
        