# Turtle_Drawing
***利用Turtle递归绘制分形几何图形***

## 一、Turtle的常用方法

方法  | 描述  
 ---- | ----- 
 turtle.forward(distance)  | 向当前画笔方向移动distance像素长度 
 turtle.backward(distance)  | 向当前画笔相反方向移动distance像素长度 
turtle.right(degree) | 顺时针移动degree°
turtle.left(degree) | 逆时针移动degree°
turtle.penup() |	提起笔移动，不绘制图形，用于另起一个地方绘制
turtle.pendown() | 移动时绘制图形，缺省时也为绘制
turtle.goto(x,y) |	将画笔移动到坐标为x,y的位置 
turtle.mainloop()或turtle.done() |	保持图形不消失，必须是乌龟图形程序中的最后一个语句
turtle.fillcolor(colorstring)	| 对绘制图形进行颜色填充
turtle.color(color1, color2) |	同时设置pencolor=color1, fillcolor=color2
turtle.begin_fill() |	准备开始填充图形
turtle.end_fill() | 填充完成
turtle.hideturtle() |	隐藏画笔的turtle形状
turtle.showturtle() |	显示画笔的turtle形状

## 二、绘制简单图形

**正方形**  
![image](https://github.com/xuedengyue/Turtle_Drawing/blob/master/image/%E6%AD%A3%E6%96%B9%E5%BD%A2.png)

**正方形填充颜色**  
![image](https://github.com/xuedengyue/Turtle_Drawing/blob/master/image/%E6%AD%A3%E6%96%B9%E5%BD%A2%E5%A1%AB%E5%85%85%E9%A2%9C%E8%89%B2.png)

**五角星**  
![image](https://github.com/xuedengyue/Turtle_Drawing/blob/master/image/%E4%BA%94%E8%A7%92%E6%98%9F.png)

**八角形**  
![image](https://github.com/xuedengyue/Turtle_Drawing/blob/master/image/%E5%85%AB%E8%A7%92%E5%BD%A2.png)

## 三、递归绘制雪花

  **雪花的绘制，可以看作是三个完全相同部分的叠加**，所以只需要绘制出一个基本图形，其他的图形在此基础上旋转方向即可。
  
  **初始的图形（即0阶）是一条线段,每增加一阶，则将上一阶线段中间1/3的位置上画一个三角形**，代码如下：
  
```
def snow(size , level):
    #递归出口，如果阶数减为0，则只是绘制一个线段
    if level == 0:
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
``` 
  
**0阶图形**  
![image](https://github.com/xuedengyue/Turtle_Drawing/blob/master/image/0%E9%98%B6.png)

**1阶图形**  
![image](https://github.com/xuedengyue/Turtle_Drawing/blob/master/image/%E4%B8%80%E9%98%B6.png)

**2阶图形**  
![image](https://github.com/xuedengyue/Turtle_Drawing/blob/master/image/2%E9%98%B6.png)

**3阶图形**  
![image](https://github.com/xuedengyue/Turtle_Drawing/blob/master/image/3%E9%98%B6.png)

**则在上面的基础上，可以绘制雪花图案如下： ** 

**1阶雪花**  
![image](https://github.com/xuedengyue/Turtle_Drawing/blob/master/image/snow/1%E9%98%B6.png)

**2阶雪花**  
![image](https://github.com/xuedengyue/Turtle_Drawing/blob/master/image/snow/2%E9%98%B6.png)

**3阶雪花**  
![image](https://github.com/xuedengyue/Turtle_Drawing/blob/master/image/snow/3%E9%98%B6.png)

**4阶雪花**  
![image](https://github.com/xuedengyue/Turtle_Drawing/blob/master/image/snow/4%E9%98%B6.png)

## 四、递归绘制树
  **使用递归算法绘制树的图形**,代码如下
  '''
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
  
  **9阶树的图形如下**  
  ![image](https://github.com/xuedengyue/Turtle_Drawing/blob/master/image/9%E9%98%B6%E6%A0%91.png)
