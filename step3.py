number = int(input("I am thinking of a number between 1 and 10. What's the number? "))
import random 
my_random_number = random.randint(1, 10)
while number != my_random_number:
    if number < my_random_number:
        print("{} is too low. ".format(number))
        number = int(input("What's the number? "))
    if number == my_random_number:
        print("{}. Yes! You win!".format(number))
        number = int(input("Yes! You win!"))
    if number > my_random_number:
        print("{} is too high. ".format(number))
        number = int(input("What's the number? "))