from graph import *

def main():
    background(700, 500, 6)

    run()

def landscape(width, height):
    """"draws sky, see, beach
    height, width - size of the landscape"""
    penSize(0)
    brushColor(0, 200, 255)
    rectangle(0, 0, width, 0.45*height) #sky
    brushColor('blue')
    rectangle(0, 0.45*height, width, 0.7*height)
    brushColor('yellow')
    rectangle(0, 0.7*height, width, height)

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
