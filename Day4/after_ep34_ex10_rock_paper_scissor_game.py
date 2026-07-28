import random
print("Welcom to rock paper and scissor game!")

rock = '''
          _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)
'''

paper = '''
          _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)
'''

scissor = '''
          _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)
'''

game_choice = [rock, paper, scissor]

user_choice = int(input("Choose 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_choice < 0 or user_choice > 2:
    print("You chose an invalid option. You lose!")
else:
    computer_choice = random.randint(0, 2)

    print("You chose:")
    print(game_choice[user_choice])

    print("Computer chose:")
    print(game_choice[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    else:
        print("You lose!")