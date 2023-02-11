# 1. Name:
#      Jacob Briggs
# 2. Assignment Name:
#      Lab 01: Guessing Game
# 3. Assignment Description:
#     Allow the user to guess a number between 1 and ten and have the number of tries reported. 
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was getting the guess to work with the while loop.
#      When I first typed the assignment I had the guess as a function called attempt that would ask for a guess, append it to the list and add a try to the count(x). 
#      After I realized that my guess was a local variable I added the code to the while loop so that it would run. After that my time was just spent trying to set up the video.  
# 5. How long did it take for you to complete the assignment?
#      It took about an hour.
import random

print('This is the "guess a number" game.')
print('You try to guess a random number in the smallest number of attempts')

max_num = int(input('Pick a positive integer: '))
numbers = []

x = 0
guess = 0
print(f'Guess a number between 1 and {max_num}.')
number = random.randint(1, max_num)

while guess != number:
    guess = int(input('> '))
    numbers.append(guess)
    x += 1
    if guess == number:
        print(f'You were able to find the number in {x} guesses.')
        print(f'The numbers you guessed were: {numbers}')
    elif guess > number:
        print('Too high!')
    elif guess < number:
        print('to low!')