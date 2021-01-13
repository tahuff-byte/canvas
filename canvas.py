#Imports the turtle library 
import turtle as trtl

#the turtle module pop up window
wn = trtl.Screen()

#ask to pick 2 colors
print("pick 2 colors")

#int vars so the program can gather user input
color_1 = input("What color would you like?: ")
color_2 = input("can you give me another color: ")
 
#putting the color cars in the .color method paramaters
trtl.color(color_1, color_2)

#a for loop that draws the shape then shades it in based on what color you gave it
trtl.begin_fill()
for i in range(75):
    trtl.speed(30)
    trtl.forward(300)
    trtl.left(170)
trtl.end_fill()

wn.mainloop()
