from graph import *

def main():
    background(700, 500, 6)
    cloud(100, 100, 20, 20)
    ship(350, 350, 100, 20)
    sun(600, 100, 25)
    umbrella(100, 285, 175, 175)

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
     num_waves - number of waves, one wave - yellow + blue
     boarder_see - y of the boarder of the see"""
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
    """draws background and sets canvas&window size
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
    """x, y - position of the centre"""
    penSize(0)
    brushColor('yellow')
    circle(x, y, radius)

def umbrella(x, y, width, height):
    """"width - width of the base of the triangle, height - total height
    x, y - position of the tip of umbrella"""
    penSize(0)
    brushColor(246, 64, 89)
    polygon([(x, y), (x - width/2, y + height/5), (x + width/2, y + height/5), (x, y)])
    dl = width/7 #distance between line on umberlla
    penColor('black')
    for i in range(1, 7):
        line(x, y, x - 1/2*width  + i*dl, y + height/5)
    penColor(137, 63, 0)
    penSize(1/20*width)
    line(x, y + height/5, x, y + height)
main()
