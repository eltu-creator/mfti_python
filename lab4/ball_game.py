from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

colors = ['red','orange','yellow','green','blue']
def new_ball():
    '''creates a new ball every 1000 ms
    x, y - coordinates of the ball, r - radius'''
    global x, y, r
    canv.delete(ALL)
    x = rnd(100, 170)
    y = rnd(100, 500)
    r = rnd(30, 50)
    canv.create_oval(x - r, y - r, x + r, y + r, fill=choice(colors), width=0)
    root.after(1000, new_ball)

def click(event):
    '''Prints x, y cordinates and radius of the ball at the moment of click'''
    global points
    x_click, y_click = event.x, event.y
    distance = ((x - x_click)**2 + (y - y_click)**2)**0.5
    if distance < r:
        points += 1
def point_count():
    global points
    canv.create_text(200, 0, text=['points', points], anchor=NE, fill='grey')
    root.after(1000, point_count)

points = 0
point_count()
new_ball()
canv.bind('<Button-1>', click)

mainloop()
