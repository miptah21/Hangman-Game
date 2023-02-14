import random as rd

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["banana", "mango", "apple"]
chosen_word = rd.choice(word_list)
lives = 6

#Testing Code
print(f"Pssst, the solution is {chosen_word}")

display = []
word_length = len(chosen_word)
#Create blanks
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\nCurrent letter: {letter}\nGuessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    if guess not in display:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    #Join all the elements in the list and turn it into a String.
    print(f" ".join(display))

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("Game Over")

    print(stages[lives])