#递归方式绘制雪花

import turtle

#递归函数
#size是绘制的线段长度，level是绘制的阶数
def snow(size , level):
    #递归出口，如果阶数减为0，则只是绘制一个线段
    if level == 0:
        turtle.speed(0)
        turtle.forward(size)
    else:
        #递归调用，线段长度减为原来的1/3，阶数减一，绘制降阶后的图形
        snow(size/3, level-1)
        #相左旋转60度，绘制第二个“儿子”的图形
        turtle.left(60)
        snow(size/3, level-1)
        #向右旋转120度，绘制第三个“儿子”的图形
        turtle.right(120)
        snow(size/3, level-1)
        #向左旋转60度，绘制第四个儿子的图形
        turtle.left(60)
        snow(size/3, level-1)
#设置最高阶的线段长度
size = 300
#设置最高阶数
level = 4
#准备填色
turtle.color("white","gray")
turtle.begin_fill()
#调用绘制图形的函数
snow(size,level)
turtle.right(120)
snow(size,level)
turtle.right(120)
snow(size,level)
turtle.end_fill()
turtle.hideturtle()
turtle.mainloop()