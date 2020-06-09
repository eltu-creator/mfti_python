from graph import *

def main():
    background(700, 500, 6)

    run()

def landscape(width, height):
    pass

def waves(width, height, numWaves):
    pass

def background(width, height, numWaves):
    """draws background
    width, height are width and hight of the image"""
    canvasSize(width, height)
    windowSize(width, height)
    landscape(width, height)
    waves(width, height, numWaves)

main()
