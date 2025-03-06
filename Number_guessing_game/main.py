
import random

print('Welcome to Number Guess Game 🤗, You have only 5 chances to guess the Number!')

random_number = random.randrange(10,50)

chance = 5

guess_quanter = 0

while guess_quanter < chance:

    guess_quanter += 1

    my_guess = int(input('Enter your guess number 😊 : '))

    if my_guess == random_number:
        print(f'Congratulations! You guess the right game number and your attempt {guess_quanter}, The game number is {random_number} and your number is {my_guess} 😍🎉🎈.')
        break

    elif guess_quanter >= chance and my_guess != random_number:
        print(f'Oops sorry you complete your attemp {guess_quanter}, better luck next time 😓!')

    elif my_guess > random_number:
        print(f'Your guess number is high! to Game number try again 🙄.')

    elif my_guess < random_number:
        print(f'Your guess number is Low! to Game number try again 😫.')




