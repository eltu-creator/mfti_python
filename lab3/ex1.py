from graph import *

def eye(x, y, eyeSize):
    penColor('black')
    brushColor('red')
    circle(x, y, eyeSize)
    brushColor('black')
    circle(x, y, eyeSize/2)
xpos = 300
ypos = 300
size = 100
windowSize(600, 600)
#draw head
penColor('black')
brushColor('yellow')
circle(xpos, ypos, size)
#draw eyes
eye(xpos - 1/2*size, ypos - 1/3*size, size/6)
eye(xpos + 1/2*size, ypos - 1/3*size, size/8)
#draw mouth
rectangle(xpos - 1/2*size, ypos + 1/2*size, xpos + 1/2*size, ypos + (1/2 + 1/7)*size)
#draw eyebrows
penSize(1/15*size)
line(xpos - 1.1*size, ypos - 9/10*size, xpos - 1/7*size, ypos - 1/3*size)
line(xpos + 1/5*size, ypos - 1/3*size, xpos + 1.1*size, ypos - 5/7*size)
run()
