import random

selected_value = random.randint(0,20)
#print(dir(random))
#help(random)
print(selected_value)

while True:
    guessed_value = int(input("Please enter an integer to guess the value: "))
    if guessed_value < selected_value:
        if selected_value - guessed_value < 5:
            print("Guessed value is low")
        else:
            print("Guessed value is too low")
    elif guessed_value > selected_value:
        if guessed_value - selected_value > 5:
            print("Guessed value is too high")
        else:
            print("Guessed value is high")
    else:
        print("You found the guessed value " + str(selected_value))
        break

