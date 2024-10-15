from OpenGL.GL import *
from myTranslateCanvas import MyTranslateCanvas
import colorsys
import math

class ColorCone(object):
    def __init__(self):
        self.sides = 360
        self.height = 2
        self.radius = 1

    def display(self):
        # 底面（HSV円錐の円周）
        glBegin(GL_TRIANGLE_FAN)
        glColor3d(1, 1, 1)
        glVertex3d(0, 0, 0)  # 中心点
        for i in range(self.sides, -1, -1):
            angle = 2 * math.pi * i / self.sides
            x = self.radius * math.cos(angle)
            y = self.radius * math.sin(angle)
            glColor3dv(colorsys.hsv_to_rgb(i / self.sides, 1, 1))
            glVertex3d(x, y, 0)
        glEnd()

        # 側面
        glBegin(GL_TRIANGLE_FAN)
        glColor3d(0, 0, 0)
        glVertex3d(0, 0, self.height)  # 頂点
        for i in range(self.sides + 1):
            angle = 2 * math.pi * i / self.sides
            x = self.radius * math.cos(angle)
            y = self.radius * math.sin(angle)
            glColor3dv(colorsys.hsv_to_rgb(i / self.sides, 1, 1))
            glVertex3d(x, y, 0)
        glEnd()


def main():
    canvas = MyTranslateCanvas()
    dispObj = ColorCone()
    canvas.init(dispObj)
    canvas.loop()

if __name__ == '__main__':
    main()
