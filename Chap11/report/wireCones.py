import math
from OpenGL.GL import *
from myRotateCanvas import MyRotateCanvas


class WireCones(object):
    def __init__(self):
        self.apex = (0, 1, 0)
        NOP = 20

        self.circle = []  

        for i in range(NOP + 1):
            t = 2*math.pi*i / NOP  
            self.circle.append((math.sin(t), -1, math.cos(t)))  

    def displayEdges(self):
        glColor3dv((1, 1, 0))  

        glBegin(GL_LINE_LOOP)  

        for i in range(1, len(self.circle)):  
            glVertex3dv(self.circle[len(self.circle) - i])  

        glEnd()  
        glBegin(GL_LINES)  

        for i in range(1, len(self.circle)):  
            glVertex3dv(self.apex)  
            glVertex3dv(self.circle[i])  
        glEnd()  
        

    def display(self):
        NOC = 16  

        for i in range(NOC):
            t = 2*math.pi*i / NOC  
            glPushMatrix()  
            glTranslated(1.6 * math.sin(t), 0, 1.6 * math.cos(t))  
            glScaled(0.3, 1.4, 0.3)  
            self.displayEdges()  
            glPopMatrix()  


def main():
    canvas = MyRotateCanvas()
    dispObj = WireCones()  
    canvas.init(dispObj)  
    canvas.loop()  


if __name__ == "__main__":
    main()
