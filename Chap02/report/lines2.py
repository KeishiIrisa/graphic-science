from tkinter import *
import random

W, H = (600, 600)


def display(canvas):
  origin = (W/2, H/2)
  max_distance = 300
  for _ in range(11):
    end = (random.randint(0, W-1), random.randint(0, H-1))
    distance = ((end[0]-origin[0])**2 + (end[1]-origin[1])**2)**0.5
    color = 'red' if distance > max_distance else 'black'
    canvas.create_line(origin, end, fill=color)


def main():
  root = Tk()
  canvas = Canvas(root, width=W, height=H, highlightthickness=0)
  canvas.pack()
  display(canvas)
  root.mainloop()

if __name__ == '__main__':
  main()
