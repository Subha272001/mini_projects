import random
from game_data import data
from art import logo4,vs


chosen_data=random.choice(data)
print(chosen_data["name"])
print(chosen_data["follower_count"])
print(chosen_data["description"])
print(chosen_data["country"])
is_game_over=False
while not is_game_over:
    print(logo4)
    chosen_data=random.choice(data)
    current_score=0
    is_loop_over=False
    while not is_loop_over:
        print(f"Compare A: {chosen_data['name']},{chosen_data['description']},{chosen_data['country']}")
        print(vs)
        chosen_data2=random.choice(data)
        print(f"Against B: {chosen_data2['name']},{chosen_data2['description']},{chosen_data2['country']}")
        guess_maxfollowers_celeb=input("Who has more followers: Type 'A' OR 'B': ")
        if guess_maxfollowers_celeb.upper()=='B':
            if chosen_data2['follower_count']>chosen_data['follower_count']:
                current_score+=1
                # print(logo4)
                print(f"You are right current score is: {current_score}")
                chosen_data=chosen_data2
            else:
                is_loop_over=True
        else:
            if chosen_data['follower_count']>chosen_data2['follower_count']:
                # print(logo4)
                current_score+=1
                print(f"You are right current score is: {current_score}")
                chosen_data=chosen_data
            else:
                is_loop_over=True
    # print(logo4)
    print(f"Sorry that's wrong final score is {current_score}")
    is_game_over=True

        

        
