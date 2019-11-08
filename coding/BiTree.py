# 练习使用turtle绘制二叉树
# 二叉树也是明显递归的图形，故使用递归算法

import turtle


# size代表一个树干的长度，level代表数的深度
def tree(size, level):
    if level == 1:
        turtle.forward(size) #递归出口
    else:
        turtle.forward(size)
        #开始画左半边的树
        turtle.right(60)
        #回退前递归
        tree(size / 2, level - 1);
        #回退
        turtle.backward(size/2)

        #绘制右半边树
        turtle.left(120)
        tree(size / 2, level-1)
        turtle.backward(size/2)
        #方向归位
        turtle.right(60)
turtle.speed(0)

turtle.penup()
turtle.goto(0,-300)
turtle.pendown()

turtle.left(90)
tree(300,9)
turtle.hideturtle()
turtle.mainloop()