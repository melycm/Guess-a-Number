
number = int(input("I am thinking of a number between 1 and 10. What's the number? "))
secret_number = 5
while number != secret_number:
    if number < secret_number:
        print("{} is too low. ".format(number))
        number = int(input("What's the number? "))
    if number == secret_number:
        print("{}. Yes! You win!".format(number))
        number = int(input("Yes! You win!"))
    if number > secret_number:
        print("{} is too high. ".format(number))
        number = int(input("What's the number? "))