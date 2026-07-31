from karel.stanfordkarel import *

def main():
    fillRowOfType1()
    while left_is_clear():
        moveUp()
        fillRowOfType2()
        if left_is_clear():
            moveUp()
            fillRowOfType1()
    
def fillRowOfType1():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()
    
    moveToRowStart()

def fillRowOfType2():
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()
    
    moveToRowStart()

def moveToRowStart():
    makeUTurn()
    while front_is_clear():
        move()
    makeUTurn()

def moveUp():
    if left_is_clear():
        turn_left()
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
