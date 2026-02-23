from karel.stanfordkarel import *


def main():
    """
    Main function to fill columns alternately with two types of repairs.

    Karel fills the first column using 'fillColumnOfType1', then moves to the right,
    filling the second column with 'fillColumnOfType2'. This process continues as
    long as there are columns to fill.
    """

    # start by filling the first column with the first type of repair
    fillColumnOfType1()

    # loop while there are more columns to the right
    while front_is_clear():
        # move Karel to the right to the next column
        moveRight()
        # fill the current column with the second type of repair
        fillColumnOfType2()

        # check if there is still a column to the right
        if front_is_clear():
            # move Karel back down to the starting position of the next column
            move()
            # fill the next column with the first type of repair
            fillColumnOfType1()

# fill the current column using the first fill type


def fillColumnOfType1():
    # turn left to move in a column
    turn_left()
    # place a beeper at the starting position
    put_beeper()

    while front_is_clear():
        # move up the column
        move()
        if front_is_clear():
            # move up again
            move()
            # then place a beeper
            put_beeper()

    # return to the beginning of the column
    moveToColumnStart()

# fill the current column using the second fill type


def fillColumnOfType2():
    while front_is_clear():
        # move up the column
        move()
        # then place a beeper
        put_beeper()

        if front_is_clear():
            # again move up the column
            move()

    # return to the beginning of the column
    moveToColumnStart()

# return Karel to the starting position of the column


def moveToColumnStart():
    # turn around to face the starting position
    makeUTurn()

    # move back to the starting position
    while front_is_clear():
        move()

    # turn to face the next column
    turn_left()

# move Karel one step to the right and turn to face downwards


def moveRight():
    if front_is_clear():
        # move one step to the right
        move()
        # turn to face up
        turn_left()

# turn Karel 90 degrees to the right


def turnRight():
    turn_left()
    turn_left()
    turn_left()

# turn Karel 180 degrees to face the opposite direction


def makeUTurn():
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()
