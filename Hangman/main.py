from hangman_art import stages, logo
from hangman_words import word_list
import random

print(logo)                                          #printing the hangman logo

chosen_word = random.choice(word_list)               #choosing a word from the list of words
number_of_letters = len(chosen_word)
number_of_tries = 0                                  #number of tries the user is on

display_list = []                                    #a display that shows the letters the user has correctly guessed
for x in chosen_word:
    display_list += "_"

display = "".join(display_list)                      #the string counterpart to display_list
print("Word to guess: " + display)
guessed_letters = []                                 #keeps track of the letters the user has guessed

lives = 6
print("You have 6 lives.")
game_over = False

while not game_over:                                 #loops the game till the game is over
    number_of_tries += 1

    guess = input("Guess a letter: ").lower()        #inputting a guess from the user

    for x in range(0,number_of_letters):             #going through each letter of the display
           if chosen_word[x] == guess:               #checking if the guess is equal to any of the correct letters and
               display_list[x] = guess               #                                if so adding them to the display

    if guess in guessed_letters:                     #If the user repeats a guess then this line reminds them.
        print(f"You have already guessed {guess}.")

    if guess not in chosen_word and guess not in guessed_letters:
        lives -= 1                                   #If the user wrongly guesses a letter, they lose a life.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    guessed_letters += guess                         #adding the guess to the list of guessed letters
    display = "".join(display_list)                  #updating the string counterpart of display_list
    print(f"****************************<{lives}>/6 LIVES LEFT****************************\n" + f"No. of attempts: "
          f"{number_of_tries}" + stages[lives] + "\nWord to guess: " + display + f"        You have already guessed the following {guessed_letters}.")
                                                     #shows the lives remaining, the no. of attempts, hangman art and
                                                     #                                                    the display
    if lives == 0:
        game_over = True
        print(f"The correct answer was {chosen_word}")
        print("****************************YOU LOSE****************************")

    if "_" not in display:                           #If there are no underscores("_") in the display, the user has
        game_over = True                             #                            correctly guessed all the letters.
        print(f"The correct answer was {chosen_word}")
        print("****************************YOU WIN****************************")
