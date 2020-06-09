from graph import *

def ship(x, y, size):
    """size - length of the pole, x, y - bottom of the pole"""
    penSize(7/100*size)
    brushColor('black')
    penColor('black')
    line(x, y, x, y - size)
    brushColor(100, 57, 0)
    penColor('black')
    penSize(1)
    rectangle(x - 2/5*1.5*size, y, x + 3/5*1.5*size, y + 1/3*size)#base
    polygon([(x + 3/5*1.5*size, y + 1/3*size), (x + (3/5*1.5 + 5/7)*size, y), (x + 3/5*1.5*size, y), (x + 3/5*1.5*size, y + 1/3*size)])#nose
    brushColor(235, 240, 192)
    polygon([(x + 7/200*size, y), (x + 4/7*size, y - 1/2*size), (x + 1/7*size, y - 1/2*size), (x + 7/200*size, y)])#tides
    polygon([(x + 7/200*size, y - size), (x + 4/7*size, y - 1/2*size), (x + 1/7*size, y - 1/2*size), (x + 7/200*size, y - size)])#tides
    penSize(4/100*size)
    brushColor('white')
    circle(x + 1.05*size, y + 1/7*size, 1/12*size)

def cloud(x, y, size):
    """size - radius of circles, x, y, -position of top left circle"""
    penSize(1)
    penColor('black')
    brushColor('white')
    circle(x, y, size)
    circle(x + 1.5*size, y, size)
    circle(x - 1.5*size, y + size, size)
    circle(x, y + size, size)
    circle(x + 1.5*size, y + size, size)
    circle(x + 3*size, y, size)
    circle(x + 3.25*size, y + size, size)

def umbrella(x, y, size):
    """size - length of the pole, x, y - position of the tip of umberlla"""
    penSize(1)
    penColor(246, 64, 89)
    brushColor(246, 64, 89)
    polygon([(x, y), (x - 1/2*size, y + 1/5*size), (x + 1/2*size, y + 1/5*size), (x, y)])
    length_base = size
    dl = length_base/7
    penColor('black')
    for i in range(1, 7):
        line(x, y, x - 1/2*size  + i*dl, y + 1/5*size)
    penColor(137, 63, 0)
    penSize(1/20*size)
    line(x, y + 1/5*size, x, y + 6/5*size)


#background
penColor(0, 200, 255)
brushColor(0, 200, 255)
rectangle(0, 0, 500, 225)

penColor(0, 0, 255)
brushColor(0, 0, 255)
rectangle(0, 225, 500, 350)

penColor('yellow')
brushColor('yellow')
rectangle(0, 350, 500, 500)

ship(100, 300, 100)
cloud(100, 100, 20)
#sun
penColor('yellow')
brushColor('yellow')
circle(400, 100, 40)

umbrella(400, 300, 125)

run()
