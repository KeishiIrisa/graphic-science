from tkinter import *
from PIL import Image, ImageTk
import numpy as np


def grayscale(image):
    height = len(image)
    width = len(image[0])
    for i in range(height):
        for j in range(width):
            average = round((image[i][j][0] + image[i][j][1] + image[i][j][2]) / 3.0)
            image[i][j][0] = average
            image[i][j][1] = average
            image[i][j][2] = average

    return image


def display(canvas, image):
    pil_image = Image.fromarray(np.uint8(image))

    # Tkinterで画像を扱えるようにする
    tk_image = ImageTk.PhotoImage(pil_image)

    canvas.create_image(0, 0, anchor='nw', image=tk_image)
    canvas.image = tk_image


def main(image_path):
    img = Image.open(image_path)
    image_data = np.array(img)

    root = Tk()
    canvas = Canvas(root, width=img.width, height=img.height, bg="white")
    canvas.pack()
    image_data = grayscale(image_data)
    display(canvas, image_data)
    root.mainloop()


if __name__ == '__main__':
    image_path = "filter_sample.jpg"
    main(image_path)
