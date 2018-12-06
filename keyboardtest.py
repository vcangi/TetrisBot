import keyboard
import time


# Holds a key (string) for a number of seconds
def holdKey(key,secs):
    for i in range(round(secs*100)):
        keyboard.press(key)
        time.sleep(0.01)
    keyboard.release(key)


# Short press of key to move a tetris piece one unit
def moveUnit(key):
    holdKey(key,.05)
    time.sleep(0.05)


def moveLeft(units = 1):
    for i in range(units):
        moveUnit("left")


def moveRight(units = 1):
    for i in range(units):
        moveUnit("right")


def hardDrop():
    moveUnit("up")


def rotateCW():
    moveUnit("a")


time.sleep(1)
moveLeft(5)
moveRight(6)
rotateCW()
rotateCW()
moveLeft(6)
hardDrop()
