import random

# Generate the first random number between 33 and 126
correct_number = random.randint(33, 126)

while True:
    guess = int(input("Please Enter a Number Between 33 and 126 (Enter -1 To Exit This Program): "))

    if guess == -1:
        print("You have chosen to end this program. Thank you for using this program.")
        break
    elif guess < 33: #this is so when the user guess out of range from 33 it'll let the user know
        print("Value out of range! This is too low.")
                    #This tells the user guess that it our of range when it's above 126
    elif guess > 126:
        print("Value out of range! This is too high.")

        #This will tell the user that the number in range is incorrect and it's too low
    elif guess < correct_number:
        print("Incorrect guess! Your guess is too low.")
    elif guess > correct_number:
        print("Incorrect guess! Your guess is too high.")
    elif guess == correct_number:
        print(f"Congratulations! You have guessed the correct number! The ASCII character for {guess} is '{chr(guess)}'.")
        # Generate a new random number for the next round
        correct_number = random.randint(33, 126)
        print("A new number has been chosen. Try to guess the new number!")

