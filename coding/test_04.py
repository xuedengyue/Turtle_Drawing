#绘制正八角形

import turtle

turtle.speed(0)
for i in range(4):

    turtle.color("black","red")
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(45)

    turtle.forward(100)
    turtle.left(135)

    turtle.forward(100)
    turtle.left(45)

    turtle.forward(100)
    turtle.left(180)
    turtle.end_fill()

    turtle.color("black", "blue")
    turtle.begin_fill()
    turtle.forward(100)
    turtle.left(45)

    turtle.forward(100)
    turtle.left(135)

    turtle.forward(100)
    turtle.left(45)

    turtle.forward(100)
    turtle.left(180)
    turtle.end_fill()

turtle.mainloop()