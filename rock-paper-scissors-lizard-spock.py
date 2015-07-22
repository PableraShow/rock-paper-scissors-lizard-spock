# Rock-paper-scissors-lizard-Spock template

# https://class.coursera.org/interactivepython1-007/human_grading/view/courses/975643/assessments/28/submissions

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions

def name_to_number(name):
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == 'rock':
        name = 0
    elif name == 'spock':
        name = 1
    elif name == 'paper':
        name = 2
    elif name == 'lizard':
        name = 3
    elif name == 'scissors':
        name = 4
    else:
        print 'debug test / name_to_number: ' + name
    return name


def number_to_name(number):
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        number = 'rock'
    elif number == 1:
        number = 'spock'
    elif number == 2:
        number = 'paper'
    elif number == 3:
        number = 'lizard'
    elif number == 4:
        number = 'scissors'
    else:
        print 'debug test / number_to_name: ' + number
    return number


def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print ''
    
    # print out the message for the player's choice
    print 'The player has chosen ' + player_choice + '.'

    # convert the player's choice to player_number using the function name_to_number()
    play_number = name_to_number(player_choice)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 4)

    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = str(number_to_name(comp_number))
    
    # print out the message for computer's choice
    print 'The compu. has chosen ' + comp_choice + '.'

    
    def evaluate_winner(play_number, comp_number):
    # compute difference of comp_number and player_number modulo five
        if play_number ==  comp_number:
            message = 'We have a tie.'
        #elif :
            #message = 'The winner is ' + player_choice + ' with ' + comp_choice + '.'
        else:
            message = '- debug test error -'
        print message
        # use if/elif/else to determine winner, print winner message
    
    evaluate_winner(play_number, comp_number)
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric