import turtle as trtl
 
trtl.color('green','blue')

trtl.begin_fill()
for i in range(75):
    trtl.speed(30)
    trtl.forward(300)
    trtl.left(170)

trtl.end_fill()

wn = trtl.Screen()
wn.mainloop()
