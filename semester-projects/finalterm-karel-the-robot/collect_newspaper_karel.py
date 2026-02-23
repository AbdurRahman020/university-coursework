from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

def main():
    move()
    move()
    turnRight()
    move()
    turn_left()
    move()
    pick_beeper()
    makeUTurn()
    move()
    move()
    move()
    turnRight()
    move()
    turnRight()
    
def turnRight():
    # turn Karel 90 degrees to the right by turning left three times
    turn_left()
    turn_left()
    turn_left()

def makeUTurn():
    # turn Karel 180 degrees by turning left two times
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program()
