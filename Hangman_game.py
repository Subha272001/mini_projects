import random
from art import stages

word_list=['arya','akriti','akshi','abhavya','ashima']
random_word=random.choice(word_list)

empty_list=[]
random_word_list=[]
for letter in random_word:
    empty_list.append("_")
    random_word_list.append(letter)

# char_found=0
chances=len(stages)
# print(len(stages))
while chances>0 :
    char_found=0
    input_letter=input("guess a letter: ")
    for i in range(0,len(random_word)):
        if input_letter.lower()==random_word[i].lower():
            empty_list[i]=input_letter
            char_found=1
    if char_found==0:
        chances-=1
        print(stages[chances])
        if chances==0:
             print('lose!')
             break
        print(f"you have {chances} lives left")
    if empty_list == random_word_list:
        print("you win")
        break
    print(empty_list)

# if empty_list is random_word_list:
#     print("You win")
