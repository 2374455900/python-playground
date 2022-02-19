import math
import turtle


def drawCircleTurtle(x, y, r):
    turtle.up()  # 开始绘画
    turtle.setpos(x + r, y)  # 定位
    turtle.down()

    for i in range(0, 365, 5):  # 0到360°，以5为步长
        a = math.radians(i)
        turtle.setpos(x + r * math.cos(a), y + r * math.sin(a))


drawCircleTurtle(100, 100, 50)
turtle.mainloop()
