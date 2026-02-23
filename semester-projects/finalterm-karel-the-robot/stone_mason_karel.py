from karel.stanfordkarel import *

def main():
    """
    Main function to repair all columns in the grid.
    
    Karel will move through the grid, column by column, repairing each
    column by placing beepers. The process repeats until there are no 
    more columns to repair.
    """
    while front_is_clear():
        repair()
    
    repair()

# repair the current column by placing beepers from the bottom to the top
def repairingColumn():
    while front_is_clear():
        # place a beeper at the current position to repair the column
        placingBeepers()
        # move up one step in the column
        move()
    
    # place a beeper at the top of the column if needed
    placingBeepers()

# move Karel to the next column to the right, while ensuring it can move horizontally
def moveToNextColumn():
    # move Karel horizontally until it reaches the end of the current column
    while front_is_clear():
        move()
    
    # turn left to face the next column
    turn_left()
    
    # move Karel horizontally by 4 steps (as per the given configuration) to the next column
    if front_is_clear():
        horizontalSteps()

# repair the current column and move Karel to the next column
def repair():
    # turn Karel to face the column for repair
    turn_left()
    # repair the current column
    repairingColumn()
    # turn Karel to face the next column
    makeUTurn()
    # move to the next column
    moveToNextColumn()

# turn Karel 180 degrees to face the opposite direction
def makeUTurn():
    turn_left()
    turn_left()

# place a beeper at the current position if no beeper is present
def placingBeepers():
    if no_beepers_present():
        put_beeper()
        
# move Karel 4 steps horizontally to the right, steps no. are given in specifications 
def horizontalSteps():
    for _ in range(4):
        move()

if __name__ == "__main__":
    run_karel_program()