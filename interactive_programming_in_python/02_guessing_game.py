# "Guess the number" Solution
import simplegui
import random

secret_number = 0
selected_range = 100
remaining_guesses = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, remaining_guesses
    
    print 'Game Started'
    
    if selected_range == 100:
        secret_number = random.randrange(0, 100)
        remaining_guesses = 7
    elif selected_range == 1000:
        secret_number = random.randrange(0, 1000) 
        remaining_guesses = 10

# define event handlers for control panel
def range100():
    global selected_range
    selected_range = 100
    print 'Range is [0, 100]'
    new_game()

def range1000():
    global selected_range
    selected_range = 1000
    print 'Range is [0, 1000]'
    new_game()
    
def input_guess(guess):
    global remaining_guesses 
    remaining_guesses -= 1
    
    if remaining_guesses >= 0:
        guess = int(guess)
    
        if guess > secret_number:
            print 'Lower'
        elif guess < secret_number:
            print 'Higher'
        elif guess == secret_number:
            print 'Correct'
        else:
            print 'Something went wrong'
            
        print str(remaining_guesses) + ' guess remaining'
    else:
        new_game()
    
# create frame
frame = simplegui.create_frame('Guessing Game', 200, 200)

# register event handlers for control elements and start frame
frame.start()
player_guess = frame.add_input('guess', input_guess, 50) 
reset_button = frame.add_button('reset', new_game)
range_100_button = frame.add_button('Range is [0,100)', range100)
range_1000_button = frame.add_button('Range is [0,1000)', range1000)

# call new_game 
new_game()
