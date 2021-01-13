import turtle as trtl

print("pick 2 colors")

color_1 = input("What color would you like?: ")
color_2 = input("can you give me another color: ")
 
trtl.color(color_1, color_2)

trtl.begin_fill()
for i in range(75):
    trtl.speed(30)
    trtl.forward(300)
    trtl.left(170)

trtl.end_fill()

wn = trtl.Screen()
wn.mainloop()
