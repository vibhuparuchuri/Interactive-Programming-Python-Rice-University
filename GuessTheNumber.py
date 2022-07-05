# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simpleguitk as simplegui
import random

global range
range=100

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here   
    global secret_number
    global range
    global limit
    
    if(range==100):
        limit=7
        print("New game. Range is from [0,100)")
        print("Number of remaining guesses is",limit)

    else:
        limit=10
        print("New game. Range is from [0,1000)" )  
        print("Number of remaining guesses is",limit)
        
    secret_number=random.randrange(0,range)
    
    print("\n")



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global range
    range=100
    new_game()    
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global range
    range=1000
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    global limit
    limit-=1
    
    print("Guess was",int(guess))
    
    print("Number of remaining guesses is",limit)
    
    if(int(guess)>secret_number):
        if(limit>0):
            print("Lower")
            print("\n")
    elif(int(guess)<secret_number):
        if(limit>0):
            print("Higher")
            print("\n")
    else:
        print("Correct!")
        print("\n")
        new_game()
        
    if(limit==0):
        print("You ran out of guesses. The number was",secret_number)
        print("\n")
        new_game()
            
    

    
# create frame
frame=simplegui.create_frame("Guess the number!",200,200)


# register event handlers for control elements and start frame
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)
frame.add_input("Enter a guess",input_guess,200)
frame.start()

# call new_game 
#new_game()
new_game()

# always remember to check your completed program against the grading rubric
