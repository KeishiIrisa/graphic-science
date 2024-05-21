from myCanvas import MyCanvas


def pressed(event):
    global canvas, start
    start = canvas.point(event.x, event.y)


def dragged(event):
    global canvas, start
    canvas.clear()
    canvas.drawPolyline((start, canvas.point(event.x, event.y)))


def main():
    global canvas
    canvas = MyCanvas(width=400, height=400)
    canvas.bind('<Button-1>', pressed)
    canvas.bind('<B1-Motion>', dragged)
    canvas.mainloop()


if __name__ == '__main__':
    main()
