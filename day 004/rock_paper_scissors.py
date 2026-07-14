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
---'    ____)____
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

game_imagines = [rock, paper, scissors]

player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_choose = random.randint(0,2)

if player_choose <= 2 and player_choose >= 0:
    print(game_imagines[player_choose])


print(f"computer choose: {game_imagines[computer_choose]}")

if player_choose >= 3 or player_choose < 0:
    print("You typed an invalid number, try again!")

elif player_choose == 0 and computer_choose == 2:
    print("You win!")

elif player_choose == 2 and computer_choose == 0:
    print("You lose!")

elif computer_choose > player_choose:
    print("You lose!")

elif (computer_choose < player_choose):
    print("You win!")

elif computer_choose == player_choose:
    print("it's a draw!")
