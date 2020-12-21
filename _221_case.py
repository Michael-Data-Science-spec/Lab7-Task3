'''
This module is created for 
'''
import sys

def check_tickets(t):
    '''
    This function outputs the number of tickets if it is less than 3. if number\
    of tickes is 3, then the functions outputs the error
    '''
    try:
        assert t < 3
        return 1
    except AssertionError:
        return 0


def game_over():
    '''
    Ends the game after 3 failed attempts
    '''
    print("У вас 3 талони. Гру закінчено")
    print("Ви програли")


def quit_func(inp):
    '''
    Ends the game if input = quit
    '''
    if inp == "quit":
        sys.exit(0)
    else:
        pass
