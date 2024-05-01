from PIL import Image, ImageTk
import numpy as np
from tkinter import Tk, Canvas


def reflect(image):
    height, width, _ = image.shape
    for i in range(height):
        for j in range(width // 2):
            # 水平方向でピクセルの色指定を入れ替える。
            image[i][j], image[i][width - 1 - j] = image[i][width - 1 - j].copy(), image[i][j].copy()
    return image


def display(canvas, image):
    pil_image = Image.fromarray(np.uint8(image))

    tk_image = ImageTk.PhotoImage(pil_image)

    # canvasの中央に配置する
    canvas_width = canvas.winfo_reqwidth()
    canvas_height = canvas.winfo_reqheight()
    canvas.create_image(canvas_width // 2, canvas_height // 2, anchor='center', image=tk_image)

    canvas.image = tk_image


def main(image_path):
    img = Image.open(image_path)

    image_data = np.array(img)

    root = Tk()
    canvas = Canvas(root, width=img.width, height=img.height, bg="white")
    canvas.pack()
    image_data = reflect(image_data)
    display(canvas, image_data)
    root.mainloop()
    

if __name__ == '__main__':
    image_path = "filter_sample.jpg"
    main(image_path)
