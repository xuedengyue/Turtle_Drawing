#绘制五角星

import turtle

turtle.color("red","green")

turtle.begin_fill()

for i in range(5):
    turtle.forward(200)
    turtle.right(144)

turtle.end_fill()

#提起笔移动，之后移动画笔将不再绘制形状，否则会导致从图形到文本之间出现一个线条
#相应的，pendown()方法是放下画笔，开始绘制形状
turtle.penup()
#goto(x,y) 将画笔移动到绝对位置（x,y）
turtle.goto(-100,-200)
turtle.color("gray")
turtle.write("Drawing by xuedengyue", font=('Arial', 25, 'normal'))

turtle.mainloop()