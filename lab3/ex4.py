from graph import *

def main():
    background(700, 500, 6)

    run()

def landscape(width, height):
    """"draws sky, see, beach
    height, width - size of the landscape"""
    penSize(0)
    height_sky = 0.45*height
    height_see = 0.7*height
    height_beach = height
    brushColor(0, 200, 255)
    rectangle(0, 0, width, height_sky) #sky
    brushColor('blue')
    rectangle(0, height_sky, width, height_see)
    brushColor('yellow')
    rectangle(0, height_see, width, height_beach)
    return height_sky, height_see, height_beach

def waves(width, height, numWaves):
    pass

def background(width, height, numWaves):
    """draws background
    width, height are width and hight of the image"""
    canvasSize(width, height)
    windowSize(width, height)

    height_sky, height_see, height_beach = landscape(width, height)
    print(height_sky, height_see, height_beach)
    waves(width, height, numWaves)

main()
