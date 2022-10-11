import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

choice=int(input("Enter 0 for rock or 1 for paper or 2 for scissors: "))
list1=[rock,paper,scissors]
print("Your choice: ")
if choice==0:
    print(list1[0])
elif choice==1:
    print(list1[1])
else: 
    print(list1[2])
print("Computer choice: ")
computer_choice=random.randint(0,3)
print(list1[computer_choice])

if choice==0:
    if computer_choice==2:
        print("you win")
    elif computer_choice==0:
        print("draw")
    else:
        print("you lose")
if choice==1:
    if computer_choice==2:
        print("you lose")
    elif computer_choice==0:
        print("you win")
    else:
        print("draw")
if choice==2:
    if computer_choice==2:
        print("draw")
    elif computer_choice==0:
        print("you lose")
    else:
        print("you win")


