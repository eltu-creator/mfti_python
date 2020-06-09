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
    brushColor(0, 200, 255)
    rectangle(0, 0, width, boarder_sky) #sky
    brushColor('blue')
    rectangle(0, boarder_sky, width, boarder_see)
    brushColor('yellow')
    rectangle(0, boarder_see, width, height)
    return boarder_sky, boarder_see

def waves(width, height, numWaves, boarder_see):
    penSize(0)
    dl = width/(2*numWaves)
    position = dl/2
    for i in range(1, numWaves + 1):
        brushColor('yellow')
        circle(position, boarder_see + 0.02*height, dl/2)
        brushColor('blue')
        circle(position + dl, boarder_see, dl/2)
        position += 2*dl

def background(width, height, numWaves):
    """draws background
    width, height are width and hight of the image"""
    canvasSize(width, height)
    windowSize(width, height)

    boarder_sky, boarder_see = landscape(width, height)
    waves(width, height, numWaves, boarder_see)

main()
