#import random module and other required files
import random
from word_list import word_list
from hangman_art import logo, stages

#selects a word randomly from the word_list file and assigns the length to a variable "word_length"
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#creates two variables to represent the lives and duration of the game
game_finished = False
lives = 6

#print hangman logo
print(logo)

#create blanks for the display
display = []
for _ in range(word_length):
    display += "_"

#while loop that keep running until the game ends
while not game_finished:
    #prompting the user to guess a letter to check with the chosen word
    guess = input("Guess a letter: ").lower()

    #checks if the user has entered a letter they've already gussed and tells the user to try again
    if guess in display:
      print(f"You've already guessed the letter {guess}, try again.\n")

    #checks if the guessed letter is in the chosen word and tells the user if the letter is in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess in chosen_word:
        print(f"The letter {guess} is the word, keep guessing!\n")

    #checks if user is wrong and tells the user if the letter isn't in the chosen word
    if guess not in chosen_word:
        lives -= 1
        print(f"The letter {guess} is not the word, you lose a life.\n")
        if lives == 0:
            game_finished = True
            print("You ran out of lives, you lose!\n")
            print(f"The chosen word was {chosen_word}")

    #joins all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #checks if user has got all letters and ends the game if the user guessed all the letter correctly
    if "_" not in display:
        game_finished = True
        print("You guessed the word correctly! You win!\n")

    #prints the hangman art depending on how much lives the user has 
    print(stages[lives])