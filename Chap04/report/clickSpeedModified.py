from tkinter import Tk, Canvas
import random
import time


class ClickSpeedGame:
    def __init__(self):
        self.W, self.H = (400, 400)
        self.R = 5
        self.TIMES = 10
        self.count, self.fastest = (0, -1)
        self.error = False
        self.ttime = None
        self.x = None
        self.y = None
        self.root = Tk()
        self.canvas = Canvas(self.root, width=self.W, height=self.H, bg='#ffffff')
        self.canvas.pack()
        self.canvas.bind('<Button-1>', self.pressed1)
        self.canvas.bind('<ButtonRelease-2>', self.released2)

    def display(self):
        self.x = random.randint(2+self.R, self.W+2-self.R)
        self.y = random.randint(2+self.R, self.H+2-self.R)
        self.canvas.create_rectangle((2, 2), (self.W+3, self.H+3), outline='', fill='#ffffff')
        if self.error:
            self.canvas.create_rectangle((self.x-self.R, self.y-self.R), (self.x+self.R, self.y+self.R), outline='', fill='#ff0000')
        else:
            self.canvas.create_rectangle((self.x-self.R, self.y-self.R), (self.x+self.R, self.y+self.R), outline='', fill='#000000')

    def pressed1(self, event):
        if self.count > 0:
            xc, yc = (event.x, event.y)
            if self.x - self.R <= xc <= self.x + self.R and self.y - self.R <= yc <= self.y + self.R:
                self.error = False
                self.count = self.count - 1
            else:
                self.error = True
                self.count = self.count + 1
            if self.count > 0:
                print(self.count, 'more!!')
                self.display()
            else:
                self.ttime = time.time() - self.ttime
                if self.fastest < 0 or self.ttime < self.fastest:
                    self.fastest = self.ttime
                print('Finished in', self.ttime, 'secs. Fastest time:', self.fastest, 'secs.')
        else:
            if self.fastest < 0:
                print('Click right button to start.') 
            else:
                print('Click right button to start. Fastest time:', self.fastest, 'secs.')

    def released2(self, event):
        self.error = False
        self.count = self.TIMES
        print('Start clicking ...', self.count, 'more!!')
        self.ttime = time.time()
        self.display()

    def main(self):
        self.root.mainloop()


if __name__ == '__main__':
    game = ClickSpeedGame()
    game.main()
    