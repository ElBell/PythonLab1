from random import randrange

random_number: int = randrange(10)
user_guess: int = None
previous_guess: int = None
count: int = 1

while user_guess != random_number:
    previous_guess = user_guess
    user_guess = int(input("Guess a number between 0 and 9\n"))
    if user_guess not in range(10):
        user_guess = int(input("Please guess between 0 and 9"))
        count += 1
    elif user_guess == previous_guess:
        print("You just guessed that, please guess a different number")
    elif user_guess > random_number:
        print("That's a bit too high")
        count += 1
    elif user_guess < random_number:
        print("That's a bit too low")
        count += 1
    else:
        print("You win! It took you {} tries".format(count))
