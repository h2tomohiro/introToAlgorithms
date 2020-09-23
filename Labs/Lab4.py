""" Guessing Game """
import random

def guessing_game():
    answer = random.randint(1, 1000)
    guess_count = 0
    upper = 1000
    lower = 1
    guess = int(input("Enter your guess from" + " " + str(lower) + " " + "to" + " " + str(upper) + ":"))

    while guess != answer:
        if guess > 1000 or 1 > guess:
            guess_count += 1
            print("Wrong! Guess count" + " " + str(guess_count))
        elif guess > answer:
            guess_count += 1
            upper = guess - 1
            print("Wrong! Guess count" + " " + str(guess_count))
        elif guess < answer:
            lower = guess + 1
            guess_count += 1
            print("Wrong! Guess count" + " " + str(guess_count))

        guess = int(input("Enter your guess from" + " " + str(lower) + " " + "to" + " " + str(upper) + ":"))

    print("You got it! The hidden number is" + " " + str(guess))
    print("It took you" + " " + str(guess_count) + " " + "guess(es)")
    pass

# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game()



