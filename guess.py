#This is a "guess the number" game
import random

guessesTaken = 0

print('Hello, friend! What\'s your name?')
name = input()

number = random.randint(1,20)
print('Well,  ' + name + ', I\'m thinking of a number between 1 and 20. Guess the number, and you\'ll get a prize!')

while guessesTaken < 6:
    print('Go on, take a guess!')
    guess = input()
    guess = int(guess)
    guessesTaken= guessesTaken + 1

    if guess < number:
        print('Too low!')

    if guess > number:
        print('Too high!')

    if guess == number:
        break
    
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Darn, you guessed it! I lied about the prize...Oh well, you guessed the number in ' + guessesTaken + ' guesses!')

else:
    number = str(number)
    print('Haha, you didn\'t get it! Well, the number was ' + number + ".")

        
        
