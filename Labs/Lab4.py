""" Guessing Game """
import random

def guessing_game():
    answer = random.randint(1, 1000)  # generate a random integer from 1 to 1000
    while True:
        guess = int(input("Enter your guess from 1 to 100"))
        if(answer < guess):
            print("The number is smaller than your number")
        elif(answer > guess):
            print("The number is greater than your number")
        else:
            print("This is the number")
    print(answer)

# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    guessing_game()



