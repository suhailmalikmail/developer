
from turtle import *
from colorsys import hsv_to_rgb

bgcolor("black")
colormode(1.0)
tracer(0)
hideturtle()
pensize(2)

offset = 0      # color ghumane ke liye
twist = 2       # shape badalne ke liye

try:
    while True:
        clear()
        penup()
        home()              # har frame center se shuru
        setheading(0)
        pendown()

        h = offset
        for i in range(40):
            color(hsv_to_rgb(h % 1, 1, 1))
            h += 0.025

            left(1)
            forward(1)

            for j in range(2):
                left(twist)
                circle(140, steps=60)   # steps kam = tez drawing

        update()
        offset += 0.02      # rainbow ghoomta hai
        twist += 0.03       # pattern dheere-dheere badalta hai
except (Terminator, TclError):
    pass