import random
import art
import words
from os import system

stages = art.hangman_stages
logo = art.hangman_logo

word_list = words.word_list
chosen_word = random.choice(word_list)

#Testing code
print(logo + "\n")
print(f'Pssst, the solution is {chosen_word}.')

display = []
for letter in chosen_word:
    display += ("_")

word_length = len(chosen_word)
end_of_game = False
lives = 6



while not end_of_game:
    guess = input("Guess a letter\n").lower()
    system('clear')
    print(logo + "\n")

    if len(guess) == 1:
        if guess in display:
            print(f"You've already guessed {guess}. Try again!")

        # Checks guess against every letter. Nothing else needs to be in here
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Removes life if wrong letter guessed
        if guess not in chosen_word:
            lives -= 1
            print(f"The letter {guess} was wrong. You lose a life. Guess again!\n")
        elif "_" not in display:
            end_of_game = True
            print(f"You guessed {chosen_word}! You win the game!")
        else:
            print(f"You guessed {guess} right. What's your next guess?\n")

        # Checks lives left, everytime a guess is made
        if lives == 0:
            end_of_game = True
            print("You ran out of lives. You lose the game!")

        # Checks if won, everytime a guess is made
    else:
        print("You need to guess ONE letter!\n")
    print(stages[lives])
    # Print function which doesn't show list formatting
    print(f"{' '.join(display)}\n")