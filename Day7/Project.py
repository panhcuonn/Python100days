word_list = ["ardvark","baboon","camel"]
import random

stages = ['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
=========
      ''','''
 +---+
  |   |
  0   |
 /|\  |
 /    |
      |
=========
      ''','''
 +---+
  |   |
  0   |
 /|\  |
      |
      |
=========
      ''','''
 +---+
  |   |
  0   |
 /|   |
      |
      |
=========
      ''','''
 +---+
  |   |
  0   |
 /    |
      |
      |
=========
      ''','''
 +---+
  |   |
  0   |
      |
      |
      |
=========
      ''','''
 +---+
  |   |
      |
      |
      |
      |
=========
''']
chosen_word = random.choice(word_list)
changes = 6

print(f'Pssst, the solution is {chosen_word}.')

word_length = len(chosen_word)
display = []
for letter in chosen_word:
    display += "_"
print(display)

end_game = False
while not end_game:
    
    guess = input("Guess a letter: ").lower()
    for i in range(word_length):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter

    if guess not in chosen_word:
        changes -= 1
        if changes == 0:
            end_of_game = True
            print("You lose.")
    print(display)

    if "_" not in display:
        end_game = True
        print("You win")
    print(stages[changes])