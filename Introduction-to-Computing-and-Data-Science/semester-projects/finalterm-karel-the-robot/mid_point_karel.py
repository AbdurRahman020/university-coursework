from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
When you finish writing it, MidpointKarel should leave
a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

def main():
    # place the first beeper on the start
    put_beeper()
    # check if there's a clear path ahead
    if front_is_clear():
        # move to the next corner
        move()
        # if there's still a clear path
        if front_is_clear():
            # start the process of finding the midpoint
            findMidPoint()
            # pick up all beepers placed along the way
            removeAllBeepers()
            # move until the midpoint is found (beeper placed)
            moveUntilBeeper()
        else:
            # make a U-turn if there's no more space
            makeUTurn()
            # move to the midpoint from the other direction
            moveUntilBeeper()

def findMidPoint():
    # move to the farthest corner and place a beeper there
    placeBeeperWall()  
    while no_beepers_present():
        # check each corner for a beeper (used for midpoint calculation)
        midPointCheck()
        # search for and place beepers as it moves along
        findBeepers()

# go back to the starting point and pick up all beepers placed along the way
def removeAllBeepers():
    # pick up any beepers in the path
    pickBeepers()
    # turn around to go back to the start
    makeUTurn()
    # keep moving back to the start until the first beeper is found
    moveUntilBeeper()
    # pick up the beeper at the starting position
    pickBeepers()
    # turn around to head toward the midpoint again
    makeUTurn()

# move along a path and pick up all the beepers it finds along the way
def pickBeepers():
    while front_is_clear():
        move()
        pick_beeper()

# keep moving until a beeper is found
def moveUntilBeeper():
    while no_beepers_present():  
        move()

# move to the farthest corner and place a beeper there
def placeBeeperWall():
    while front_is_clear():
        move()  
    put_beeper()
    # turn around and move back
    uTrunAndMove()

# move to the next corner and place a beeper if none is already present
def midPointCheck():
    move()
    if beepers_present():
        uTrunAndMove()
        put_beeper()    

# look for beepers as Karel moves forward, and will stop and place a beeper when one is not found
def findBeepers():
    if no_beepers_present():
        while no_beepers_present():
            move()
        
        uTrunAndMove()
        put_beeper()  
        move()

# turn Karel 180 degrees to face the opposite direction
def makeUTurn():
    turn_left()
    turn_left()

# make a U-turn and then move forward
def uTrunAndMove():
    makeUTurn()
    move()

if __name__ == "__main__":
    run_karel_program()
