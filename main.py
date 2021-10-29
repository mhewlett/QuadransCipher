# Import random
import random

# Setup variables
loop = 'y'



# Begin program loop
while loop.lower() == 'y':

    guess = ''
    guesses = []


    # Construct program variables and prevent duplicates
    rand1 = random.randint(0, 9)
    rand2 = random.randint(0, 9)
    if rand2 == rand1:
        rand2 = random.randint(0, 9)
    rand3 = random.randint(0, 9)
    if rand3 == rand2 or rand3 == rand1:
        rand3 = random.randint(0, 9)
    rand4 = random.randint(0, 9)
    if rand4 == rand3 or rand4 == rand2 or rand4 == rand1:
        rand4 = random.randint(0, 9)

    # Concatenate the variables into a single answer
    answer = str(rand1) + str(rand2) + str(rand3) + str(rand4)


    print('QUADRAN\'S CIPHER')
    print('You have 10 chances to crack the code.')

    for num_of_guess in range(10):
        # Declare hint variables
        correct = 0
        exact = 0

        # Ask user for input
        print()
        print('Enter 4 numbers like \'####\' and guess the random number!')
        print('Numbers range from 0-9 with no duplicates.')
        if num_of_guess > 0:
            print('Guesses so far (plus hints):')
            print(guesses)
        print('Guess #' + str(num_of_guess + 1))
        guess = input('> ')


        # If the user enters non integers
        if not guess.isdigit():
            print('That\'s not an appropriate answer. Try again.')
            continue

        # If the user enters more or less than 4 numbers
        elif len(guess) > 4:
            print('You have entered too many digits.')
            continue
        elif len(guess) < 4:
            print('You have not entered enough digits.')
            continue

        # If the user provides an adequate answer
        else:

            if guess == answer:
                print()
                print('You guessed correctly! It took you ' + str(num_of_guess + 1) + ' tries!')
                print('Would you like to play again?')
                loop = input('Y or N? > ')
                break

            else:
                if guess[0] == str(rand1):
                    exact += 1
                if guess[0] == str(rand2):
                    correct += 1
                if guess[0] == str(rand3):
                    correct += 1
                if guess[0] == str(rand4):
                    correct += 1

                if guess[1] == str(rand1):
                    correct += 1
                if guess[1] == str(rand2):
                    exact += 1
                if guess[1] == str(rand3):
                    correct += 1
                if guess[1] == str(rand4):
                    correct += 1

                if guess[2] == str(rand1):
                    correct += 1
                if guess[2] == str(rand2):
                    correct += 1
                if guess[2] == str(rand3):
                    exact += 1
                if guess[2] == str(rand4):
                    correct += 1

                if guess[3] == str(rand1):
                    correct += 1
                if guess[3] == str(rand2):
                    correct += 1
                if guess[3] == str(rand3):
                    correct += 1
                if guess[3] == str(rand4):
                    exact += 1

                guesses.append(f'{guess}-({exact}/{correct})')
                print(f'{exact} numbers are in the correct position.')
                print(f'{correct} numbers are correct but in the wrong position.')
                if num_of_guess < 10:
                    print('Try again!')
                continue
    if guess != answer:
        print()
        print('You ran out of guesses.')
        print(f'The answer was {answer}.')
        print('Would you like to play again?')
        loop = input('Y or N? > ')
        print()