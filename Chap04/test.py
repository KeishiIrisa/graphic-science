from tkinter import *
import math

W, H = (400, 400)

def pressed(event):
    global startX, startY, points
    startX, startY = (event.x, event.y)
    points = [(startX, startY)]

def dragged(event):
    global canvas, startX, startY, points
    x, y = (event.x, event.y)
    points.append((x, y))
    canvas.create_oval((x-5, y-5), (x+5, y+5), outline="black", fill="black")

def draw_cardioid():
    global canvas, points
    canvas.delete("all")
    if len(points) < 2:
        return
    a = math.sqrt((points[0][0] - points[1][0])**2 + (points[0][1] - points[1][1])**2)
    for t in range(0, 360):
        theta = math.radians(t)
        r = 2 * a * (1 - math.cos(theta))
        x = r * math.cos(theta) + points[0][0]
        y = r * math.sin(theta) + points[0][1]
        canvas.create_oval((x-2, y-2), (x+2, y+2), outline="black", fill="black")

def main():
    global canvas, points
    root = Tk()
    canvas = Canvas(root, width=W, height=H, bg="#ffffff")
    canvas.pack()
    canvas.bind("<Button-1>", pressed)
    canvas.bind("<B1-Motion>", dragged)
    canvas.bind("<ButtonRelease-1>", lambda event: draw_cardioid())
    root.mainloop()

if __name__ == "__main__":
    main()