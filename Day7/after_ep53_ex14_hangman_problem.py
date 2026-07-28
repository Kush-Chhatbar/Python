import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""

for letter in range(0, len(chosen_word)):
    placeholder += "_"

print(placeholder)

correct_letters = []
game_over = False
lives = 6

while not game_over:

    guess = input("Guess the letter: ").lower()
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)


    if guess in correct_letters:
        print(f"You've already guessed the letter : {guess} \n No lives were reduced.\n Lives Left: {lives}")

    if guess not in chosen_word:
        print(f"You guessed :{guess}. It is not in the word. You loose life.")
        lives -= 1
        print(f"Lives left: {lives}")
        if(lives == 0):
            game_over = True
            print(f"The correct word was: {chosen_word}")
            print("You LOSE!")

    if "_" not in display:
        game_over = True
        print("You win!")

    print(stages[6-lives])
