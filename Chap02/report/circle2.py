from tkinter import *
import sys
import math

W, H = (600, 600)
R = 250

def circle(cen=(W / 2, H / 2), r=R):
    if len(sys.argv) > 1:
        num = sys.argv[1]
    else:
        num = input('# of points -> ')

    n = int(num)
    p = []

    for i in range(n):
        t = 2 * math.pi * i / n
        p.append((r * math.cos(t) + cen[0], r * math.sin(t) + cen[1]))
   
    return tuple(p)

def display(canvas, points):
    total_length = 0
    for i in range(len(points)):
        j = (i + 1) % len(points)
        canvas.create_line(points[i], points[j])
        total_length += math.dist(points[i], points[j])
    total_length /= (2 * R)
    canvas.create_text(W / 2, H / 2, text=str(total_length))

def main():
    root = Tk()
    canvas = Canvas(root, width=W, height=H)
    canvas.pack()
    points = circle()
    display(canvas, points)
    root.mainloop()

if __name__ == '__main__':
    main()