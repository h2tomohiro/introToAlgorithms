""" Guessing Game """
import random


def guessing_game():
    answer = random.randint(1, 3)  # generate a random integer from 1 to 1000
    guess = input("Enter your guess: ")
    guess = int(guess)
    guess_count = 0

    while guess != answer:
        if guess > answer:
            guess_count += 1
            print("Wrong! Guess count" + " " + str(guess_count))#lower
        else:
            guess_count += 1
            print("Wrong! Guess count" + " " + str(guess_count))#higher
        guess = int(input("Enter your guess from to : "))

    print("You got it! The hidden number is" + " " + str(guess))
    print("It took you" + " " + str(guess_count) + " " + "guess(es)")

    # guess = ""
    # guess_count = 0
    # guess_limit = 4
    # out_of_guesses = False
    # #guess_number = int(input("Enter your guess from 1 to 1000"))
    #
    # while guess != answer and not(out_of_guesses):
    #     if guess_count < guess_limit:
    #         guess = input("Enter a guess: ")
    #         guess_count += 1
    #     else:
    #         out_of_guesses = True
    #
    # if out_of_guesses:
    #     print("You Lose!")
    # else:
    #     print("You Win!")
    #     number_of_guesses += 1
    #     if guess < answer:
    #         print('Your guess is too low')
    #     if guess > answer:
    #         print('Your guess is too high')
    #     if guess == answer:
    #         return True
    #
    # if guess == answer:
    #     print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
    # else:
    #     print('You did not guess the number, The number was ' + str(answer))
    # while low <= high:
    #     mid = (low + high) // 2
    #     if l[mid] == value:
    #         print('Found')
    #         return True
    #     elif l[mid] < value:
    #         low = mid + 1
    #     else:
    #         high = mid - 1
    # print('Not Found')
    # return False
    # print(answer)

    # while True:
    #     guess = int(input("Enter your guess from 1 to 100"))
    #     if(answer < guess):
    #         print("The number is smaller than your number")
    #     elif(answer > guess):
    #         print("The number is greater than your number")
    #     else:
    #         print("This is the number")

    # while True:
    #     upperbound = 1000
    #     lowerbound = 0
    #     mid = (upperbound - lowerbound) / 2 + lowerbound
    #     print("Is your secret number %s?" % mid)
    #     guess = input(
    #         "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    #     if guess == 'h':
    #         upperbound = mid
    #     elif guess == 'l':
    #         lowerbound = mid
    #     elif guess == 'c':
    #         print
    #         'Game over. Your secret number was: ' + str(mid)
    #         break
    #     else:
    #         print
    #         'Sorry, I did not understand your input.'


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game()



