
#!/usr/bin/env python3

from random import randint  # Import random number generator
import sys #kill function
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" #hide pygame welcome message  
import pygame   #import pygame
import time    #import time for playing sound

#_________________________________________________________________________Variables
random1 = randint(1, 10)        #   Random number 1
random2 = randint (1, 10)       #   Random number 2
total_questions = 0  # Total questions
percent_wrong = 0    #  Questions wrong
timed = False       # If timed(Not yet implemented)
#___________________________________________________________________________Functions


def sound (n):      # Play sound function
    if n == 1:
        pygame.mixer.init()
        pygame.mixer.music.load("y.mp3")
        pygame.mixer.music.play()
        time.sleep(1)
    else:
        pygame.mixer.init()
        pygame.mixer.music.load("n.mp3")
        pygame.mixer.music.play()
        time.sleep(1)


def number (n1, n2):       #    Question function
    global total_questions
    global percent_wrong

    sn1 = str(n1)       # Convert number to string 
    sn2 = str(n2)       # Convert number to string
    a = n1 * n2         # Find answer
    
    q = input(sn1 + "*" + sn2 + "=")        # Ask question
    
    if  q == str(a) :               # Check if correct
        os.system('cls' if os.name == 'nt' else 'clear')    #   Clear terminal
        print("correct "   )            # And if so print correct 
        sound(1)
        total_questions = total_questions +  1  # Add 1 question to total questions
        
    else:
        total_questions = total_questions + 1   # Add 1 to total questions
        percent_wrong =+ 1
        sound(2)
        os.system('cls' if os.name == 'nt' else 'clear')    # Clear terminal
        print ("incorrect, the answer was" + str(a))  # If not correct then say incorrect 
        

def call ():                            # Call function
    global random1                  # Global var
    global random2                  # Global var

    
    number(random1, random2)        # Call number
    random1 = randint(1,10)         # Regenerate random number
    random2 = randint(1,10)         # Regenerate random number





#__________________________________________________________________________________________Call Questions and end script
quest_num = input("how many questions do you want? :") # Ask how many questions the user wants
print (quest_num)

quest_num_save = int(quest_num)  # Save answer

while quest_num_save > 0 :  # Loop until all questions are answered
        call()      # Call question
        quest_num_save -= 1 # Subtract 1 from answers left
else:
    print ("you got " + str(percent_wrong) + " out of " + str(total_questions) + " wrong" ) # Print how many the user got wrong
    sys.exit()      # Exit script

