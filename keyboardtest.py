import keyboard
import time


# Holds a key (string) for a number of seconds
def hold_key(key, secs):
    for i in range(round(secs*100)):
        keyboard.press(key)
        time.sleep(0.01)
    keyboard.release(key)


# Short press of key to move a tetris piece one unit
def move_unit(key):
    hold_key(key, .05)
    time.sleep(0.05)


def move_left(units=1):
    for i in range(units):
        move_unit("left")


def move_right(units=1):
    for i in range(units):
        move_unit("right")


def hard_drop():
    move_unit("up")


def rotate_cw():
    move_unit("a")


time.sleep(1)
move_left(5)
move_right(6)
rotate_cw()
rotate_cw()
move_left(6)
hard_drop()
