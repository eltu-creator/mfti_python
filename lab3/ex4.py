from graph import *

def main():
    background(700, 500, 6)

    run()

def landscape(width, height):
    """"draws sky, see, beach
    height, width - size of the landscape"""
    penSize(0)
    boarder_sky = 0.45*height
    boarder_see = 0.7*height
    boarder_beach = height
    brushColor(0, 200, 255)
    rectangle(0, 0, width, boarder_sky) #sky
    brushColor('blue')
    rectangle(0, boarder_sky, width, boarder_see)
    brushColor('yellow')
    rectangle(0, boarder_see, width, boarder_beach)
    return boarder_sky, boarder_see, boarder_beach

def waves(width, height, numWaves):
    pass

def background(width, height, numWaves):
    """draws background
    width, height are width and hight of the image"""
    canvasSize(width, height)
    windowSize(width, height)

    boarder_sky, boarder_see, boarder_beach = landscape(width, height)
    waves(width, height, numWaves)

main()
