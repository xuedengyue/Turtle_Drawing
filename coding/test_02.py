#绘制正方形，练习形状线条颜色以及颜色的填充
#练习写文本命令，turtle.write(s [,font=("font-name",font_size,"font_type")])
#线条颜色为红色，填充颜色为黄色

import turtle

#设置绘制的边框颜色和填充颜色
turtle.color("red","yellow")

#准备开始填充
turtle.begin_fill()

for i in range(4):
    turtle.forward(100)
    turtle.right(90)
#填充结束
turtle.end_fill()

#提起笔移动，之后移动画笔将不再绘制形状，否则会导致从图形到文本之间出现一个线条
#相应的，pendown()方法是放下画笔，开始绘制形状
turtle.penup()
#goto(x,y) 将画笔移动到绝对位置（x,y）
turtle.goto(-100,-200)
turtle.color("gray")
turtle.write("Drawing by xuedengyue", font=('Arial', 25, 'normal'))

#保持住绘制的图形
turtle.mainloop()