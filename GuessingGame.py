# 1. Name:
#      Collin Hyde
# 2. Assignment Name:
#      Lab 01: Guessing Game
# 3. Assignment Description:
#      This is the "guess a number" game that takes user input to set a range for a random number generator and then plays 
#      until the player guesses it right.
# 4. What was the hardest part? Being able to remember how Python works was the only thing that was rather hard.
#      The assignment went extremely well considering that I have not coded in python for some time. I had some trouble getting
#      the range to set to the user input however I realized quickly that it needed me to specify that it was an int. It took 
#      some research to figure out the list part of the program however did not take that much time. the if and else statements was 
#      really easy so that mad it smooth. It took no more than an hour to finish the code. I'm not necessarily worried about this 
#      assignment just ones in the future. 
# 5. How long did it take for you to complete the assignment?
#      1.5 hours. 



import random


# Print.
print(f"This is the ""guess a number"" game.")
print(f"You try to guess a random number in the smallest number of attempts.")

print("\n")

#Get input.
number_picked = int(input(f"Pick a positive integer: "))


#Set the random number to that input.
randomNumebr = (random.randrange(0,int(number_picked)))

if number_picked == 1:
    randomNumebr = 1



#Make a list.
list = []

print(f"Guess a number between 1 and {number_picked}. ")

# Create a while loop and make a bullion variable.
wrongGuess = True         
while wrongGuess:
    

    # Make a variable for the guess and add it to the list. 
    guess = float(input())
    list.append(guess)
    
    # Make the logic for the game with if and elif functions.

        
    
    if guess < randomNumebr:
        print(f"Too low!")


    elif guess > randomNumebr:
        print(f"Too high!")
        
    # End the game. 
    else:
        
        wrongGuess = False





# Print Information.
print(f"You were able to find the number in", len(list), "guesses.")
print(f"The numbers you guessed were:", list)








