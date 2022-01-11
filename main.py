# Hangman Game Clone built in Python
# Created by Agamdeep Singh / CodeWithAgam
# Youtube: CodeWithAgam
# Github: CodeWithAgam
# Instagram: @agamdeep_21, @coderagam001
# Twitter: @CoderAgam001
# Linkdin: Agamdeep Singh

# Random Moduel to get the words randomly
import random

# The Python files for the ASCII arts, the Hangman Logo and the words
import assets.hangman_arts as hangman_arts
from assets.hangman_words import word_list as words

# Welcome message for the user
def Welcome():
    print(hangman_arts.logo)
    Rules()
    
def Rules():
    # Give the player a choice to get to know How To Play
    choice = input("\nDo you want to know How To Play? Type (yes/no): ").lower()
    
    # Conditions to skip/toggle How To Play
    if choice == 'yes':
        print('''
    *How TO PLAY:*\n
    - Hangman is game where you've a Word and you have to guess it letter by letter.
    - You have 6 Lives to guess the word.
    - When you make a wrong guess, you lose 1 life.
    - If you lose all lives, you Lose.
    - If you guess the word before losing all 6 lives, you Win.
    ''')

        # Give the user a choice to start the game
        start = input("Do you want to start? (yes/no): ").lower()

        if start == 'yes':
            Main()
        else:
            print("Thanks for using Hangman!")

    else:
        Main()

# The main code of the game
def Main():
    # Select a random word
    chosen_word = random.choice(words)

    # Get the length of the random word
    word_length = len(chosen_word)

    # Set the no. of lives to 6 and the end of game to False
    lives = 6
    end_of_game = False

    # Create an empty list of blanks as display and add 1 blank to the for each letter in the chosen word
    display = []
    for _ in range(word_length):
        display += "_"

    # Give the user a hint
    hint = random.choice(chosen_word).upper()
    print("\nI have a word, can you guess it?")
    print(f"\nHint is: {hint}")

    # This while loops through the guess input unit the game gets over, either by winning or losing
    while not end_of_game:
        # Ask the user to guess a letter
        guess = input("Guess a letter: ").lower()

        # Check if the word is already gussed by the user
        if guess in display:
            print(f"You guessed {guess}, but you've already guessed it.")

        # Check if the word guess by the user is correct
        for position in range(word_length):
            letter = chosen_word[position]
            
            if letter == guess:
                display[position] = letter
            
        # Check if the word guessed by the user is wrong
        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You Lose 1 Life.")
            lives -= 1

            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word was: {chosen_word}")

        # Join all the elements in the list and turn it into a String
        print(f"{' '.join(display)}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        # Print the current stage corresponding to the no. of lives left and wrong words guessed
        print(hangman_arts.stages[lives])

Welcome()