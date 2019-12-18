import string
import random

#Variables that are created
list_l = list(string.ascii_letters)
list_d = list(string.digits)
list_p = list(string.punctuation)
list_all = list_p + list_d + list_l
created_password = list()

print(list_l)
print(list_d)
print(list_p)
print(list_all)

print(len(list_l))
print(len(list_d))
print(len(list_p))


while True:
    while True:
        try:
            length = int(input("Please enter length for the password which is minimum 9 and maximum " + str(len(list_all)) +" : "))
            if length < 9 or length > len(list_all) :
                raise TypeError
            break
        except ValueError:
            print("Please enter an integer!")
        except TypeError:
            print("Enter an integer between 9 - 94")
    while True:
        try:
            if length - 6 > len(list_l):
                letter_length = int(input("Please enter letter length for the password from " + str(len(list_l)) + " to " + str(3) + " : "))
            else:
                letter_length = int(input("Please enter letter length for the password from " + str(length - 6) + " to " + str(3) + " : "))
            if length - 6 < letter_length or 3 > letter_length:
                raise TypeError
            elif letter_length > len(list_l):
                raise TypeError
            break
        except ValueError:
            print("Please enter an integer!")
        except TypeError:
            print("Enter an integer at least withing given range!")
    while True:
        try:
            if (length - letter_length) - 3 > len(list_d):
                digit_length = int(input("Please enter digit length for the password from " + str(len(list_d)) + " to " + str(3) + " : "))
            else:
                digit_length = int(input("Please enter digit length for the password from " + str((length  - letter_length) - (3)) + " to " + str(3) + " : "))
            if length - 6 < digit_length or 3 > digit_length:
                raise TypeError
            elif digit_length > len(list_d):
                raise TypeError
            break
        except ValueError:
            print("Please enter an integer!")
        except TypeError:
            print("Enter an integer at least withing given range!")
    while True:
        try:
            if (length - letter_length - digit_length) > len(list_p):
                punc_length = int(input("Please enter punctual length for the password from" + str(len(list_p)) + str(3) + " : "))
            else:
                punc_length = int(input("Please enter punctual length for the password from " + str(length - letter_length - digit_length) + " to " + str(3) + " : "))
            if length - 6 < punc_length or 3 > punc_length:
                raise TypeError
            elif punc_length > len(list_p):
                raise TypeError
            break
        except ValueError:
            print("Please enter an integer!")
        except TypeError:
            print("Enter an integer at least withing given range!")
    break


print("Your selected password length is " + str(length) + ".")
print("Your selected letter length is " + str(letter_length) + ".")
print("Your selected digit length is " + str(digit_length) + ".")
print("Your selected punctual length is " + str(punc_length) + ".")
print("Your non-entered values will be selected randomly from the database which is created " + str(length - (letter_length + digit_length + punc_length)))

# Let`s select letters
for k in range(0, letter_length):
    a = random.randint(0, len(list_l) - 1)
    created_password.append(list_l[a])
for k in range(0, digit_length):
    a = random.randint(0, len(list_d ) -1)
    created_password.append(list_d[a])
for k in range(0, punc_length):
    a = random.randint(0, len(list_p) - 1)
    created_password.append(list_p[a])
if length - (letter_length + digit_length + punc_length) > 0:
    for k in range(0, (length - (letter_length + digit_length + punc_length))):
        a = random.randint(0, len(list_all) -1)
        created_password.append(list_all[a])

print(created_password)
print(len(created_password))

final_password = ''.join(created_password)

print(final_password)
print(len(final_password))

