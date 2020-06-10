from graph import *

def main():
    background(700, 500, 6)
    cloud(100, 100, 20, 20)
    ship(350, 350, 100, 20)
    sun(100, 600, 25)
    umbrella(100, 400, 100, 100)
    run()

def landscape(width, height):
    """"draws sky, see, beach
    height, width - size of the landscape"""
    penSize(0)
    boarder_sky = 0.45*height
    boarder_see = 0.7*height
    #sky
    brushColor(0, 200, 255)
    rectangle(0, 0, width, boarder_sky)
    #see
    brushColor('blue')
    rectangle(0, boarder_sky, width, boarder_see)
    #sand
    brushColor('yellow')
    rectangle(0, boarder_see, width, height)
    return boarder_sky, boarder_see

def waves(width, height, num_waves, boarder_see):
    """"draws waves
     width, height are width and hight of the image
     num_waves - number of waves
     boarder_see - boarder of the see"""
    penSize(0)
    dl = width/(2*num_waves)
    position = dl/2
    for i in range(1, num_waves + 1):
        brushColor('yellow')
        circle(position, boarder_see + 0.02*height, dl/2)
        brushColor('blue')
        circle(position + dl, boarder_see, dl/2)
        position += 2*dl

def background(width, height, num_waves):
    """draws background
    width, height are width and hight of the image"""
    canvasSize(width, height)
    windowSize(width, height)

    boarder_sky, boarder_see = landscape(width, height)
    waves(width, height, num_waves, boarder_see)

def cloud(x, y, width, height):
    """"x, y - position of the top left oval, top left corner
    of the rectangle ovalis drawn into
    width, height - width and height of the rectangle"""
    pass

def ship(x, y, width, heigth):
    pass

def sun(x, y, radius):
    pass

def umbrella(x, y, width, height):
    pass
main()
