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

drawing = [rock, paper, scissors]

choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)


print(drawing[choice])
print("Computer chose:\n")
print(drawing[computer_choice])

if choice == computer_choice:
    print("You draw")
elif choice == 0 and computer_choice == 1:
    print("You lose")
elif choice == 1 and computer_choice == 2:
    print("You lose")
elif choice == 2 and computer_choice == 0:
    print("You lose")
else:
    print("You win!")
