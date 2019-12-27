import time
import random
main_game = False
rules = False
count_char = 0
count_guess = 0
guess_game = False
word_selection = False
char_selection = False
char_list = []
word_found = []
selected_list = []
final_guess =[]
a = 0
player_name = input("What is your name? ")
print("Welcome to Hangman Game " + player_name + "!")
print("If you want to directly to start playing press Y and enter, if you want to learn about rules press R and enter "
      "and if you want to quit the game press N and enter! ")

while True:
    try:
        decision = input("What is your decision (Y, R or N)! ")
        low_decision = decision.lower()
        if low_decision == "y":
            main_game = True
            word_selection = True
            break
        elif low_decision == "r":
            rules = True
            break
        elif low_decision == "n":
            print("You decided to quit the game :( ")
            break
        raise TypeError
    except TypeError:
        print("Please enter Y/ R or N to be able to decide about the fucking game!")

while rules:
    print("Rules of the game is coming in a second...")
    time.sleep(1)
    print("1. The computer is going to select random word from created txt file at local.")
    time.sleep(0.5)
    print("2. You will enter chars according to the length of selected word to guess missing chars!")
    time.sleep(0.5)
    print("3. At the end of guessing, you will have 3 guesses for selected word!")
    time.sleep(0.5)
    print("4. If you can find the correct word you will win, else you can restart again!")
    time.sleep(2)
    try:
        decision_2 = input("What is your decision for the game, Y for play the game N for quit the game! ")
        low_decision_2 = decision_2.lower()
        if low_decision_2 == 'y':
            main_game = True
            word_selection = True
            break
        elif low_decision_2 == 'n':
            print("You decided to quit the game :( ")
            break
        raise TypeError
    except TypeError:
        print("Please enter Y or N to be able to decide about fucking game!")

while main_game:
    while word_selection:
        print("Game will start in a second....")
        time.sleep(1)
        print("The game has been started.")
        f = open("hangman.txt", "r")
        words_list = f.read().split('\n')
        random_word = random.randint(0, len(words_list) - 1)
        selected_word = words_list[random_word]
        print("The length of the word is " + str(len(selected_word)))
        print("That is why you will get " + str(len(selected_word)) + " times char selection to guess.")
        char_selection = True
        word_selection = False
        break
    while char_selection and count_char < len(selected_word):
        selected_char = input("Please enter a char: ")
        selected_list.append(selected_char)
        count_char += 1
        if selected_char in selected_word:
            print("You found 1 char")
            print("You have " + str(len(selected_word) - count_char) + " times guess!")
            char_list.append(selected_word.index(selected_char))
        else:
            print("Try again! You have " + str(len(selected_word) - count_char) + " times guess!")
    guess_game = True

    for i in range(0, len(selected_word)):
        if i in char_list:
            word_found.append(selected_word[i])
        else:
            word_found.append("_")
    print(str(selected_list))
    print(str(word_found))
    while guess_game and count_guess < 3:
        if a < 1:
            print("You will have 3 chances to guess it correctly!")
            a += 1
        guessed_word = input("Please enter your guess: ")
        final_guess.append(guessed_word)
        count_guess += 1
        print("Your guess times is " + str(3 - count_guess))

    if selected_word == final_guess:
        print("You won!")
    else:
        print("You lost, selected word was " + selected_word)

    print("This is the end of the game, if you want to play again just press Y, to quit the game press N and enter!")
    final = input("Please Y or N? ")

    if final.lower() == "y":
        count_guess = 0
        guessed_word = 0
        a = 0
        word_selection = True
    elif final.lower() == "n":
        break












