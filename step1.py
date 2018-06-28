
number = int(input("I am thinking of a number between 1 and 10. What's the number? "))
secret_number = 5
while number != secret_number:
    if number < secret_number:
        number = int(input("Nope, try again. What's the number? "))
    if number == secret_number:
        number = int(input("Yes! You win!"))
    if number > secret_number:
        number = int(input("Nope, try again. What's the number? "))