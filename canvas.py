import turtle as trtl
import random


ColorList = ['blue' , 'pink' , 'red' , 'purple']
idx = 0
ts = trtl.getscreen()
wn = trtl.Screen()
ts

def MousePos(x, y):
    trtl.onscreenclick(trtl.goto)


def k1():
    for c in ColorList:
        trtl.begin_fill()

trtl.onscreenclick(MousePos)
wn.onkey(k1, "f")
wn.listen()

wn.mainloop()
