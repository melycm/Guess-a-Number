play = True
number = int(input("I am thinking of a number between 1 and 10. What's the number? "))
import random 
my_random_number = random.randint(1, 10)
print(my_random_number)
count = 0
while number != my_random_number:
    if number < my_random_number:
        count += 1
        print("{} is too low. ".format(number))
        number = int(input("What's the number? "))
    if number == my_random_number:
        count +=1
        print("{}. Yes! You win!".format(number))
        break
    if number > my_random_number:
        count += 1
        print("{} is too high. ".format(number))
        number = int(input("What's the number? "))

    if count == 4:
        print("You ran out of guesses")
        break

again=str(input("Do you want to play again (Y or N)? "))
if again == "N":
    play = False
if again == "Y":
    play = True

play = True
number = int(input("I am thinking of a number between 1 and 10. What's the number? "))
import random 
my_random_number = random.randint(1, 10)
print(my_random_number)
count = 0
while number != my_random_number:
    if number < my_random_number:
        count += 1
        print("{} is too low. ".format(number))
        number = int(input("What's the number? "))
    if number == my_random_number:
        count +=1
        print("{}. Yes! You win!".format(number))
        break
    if number > my_random_number:
        count += 1
        print("{} is too high. ".format(number))
        number = int(input("What's the number? "))

    if count == 4:
        print("You ran out of guesses")
        break

again=str(input("Do you want to play again (Y or N)? "))
if again == "N":
    play = False
if again == "Y":
    play = True