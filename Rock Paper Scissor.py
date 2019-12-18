import random

while True:
    user = input("Please enter rock, paper or scissor: ")
    user_low = user.lower()
    if user_low == "rock":
        break
    elif user_low == "paper":
        break
    elif user_low == "scissor":
        break
    else:
        print("You should enter the input correctly!")

computer = ["rock", "paper", "scissor"]
l = random.randint(0,2)
print(computer[l])

# Comparison side of the selected results
if user_low == "rock" and computer[l] == "paper":
    print("Winner is computer / " + computer[l] + " against / user " + user_low)
elif user_low == "rock" and computer[l] == "scissor":
    print("Winner is user / " + user_low + " against / computer " + computer[l])
elif user_low == "paper" and computer[l] == "rock":
    print("Winner is user / " + user_low + " against / computer " + computer[l])
elif user_low == "paper" and computer[l] == "scissor":
    print("Winner is computer / " + computer[l] + " against / user " + user_low)
elif user_low == "scissor" and computer[l] == "rock":
    print("Winner is computer / " + computer[l] + " against / user " + user_low)
elif user_low == "scissor" and computer[l] == "paper":
    print("Winner is user / " + user_low + " against / computer " + computer[l])
else:
    print("It is a draw!")


