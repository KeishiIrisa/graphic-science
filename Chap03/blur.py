˜from PIL import Image, ImageTk
import numpy as np
from tkinter import Tk, Canvas


def blur(image):
    height, width, _ = image.shape
    copy = image.copy()
    for i in range(height):
        for j in range(width):
            for color in range(3):  # ピクセルの周囲3*3のグリッドの色の平均値により、新しい色を定義する
                sum_color = 0
                count_color = 0
                for k in range(-1, 2):
                    for l in range(-1, 2):
                        if 0 <= i + k < height and 0 <= j + l < width:
                            count_color += 1
                            sum_color += copy[i + k][j + l][color]
                image[i][j][color] = round(sum_color / count_color)
    return image


def display(canvas, image):
    pil_image = Image.fromarray(np.uint8(image))

    tk_image = ImageTk.PhotoImage(pil_image)

    # canvasの中央に配置
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
    image_data = blur(image_data)
    display(canvas, image_data)
    root.mainloop()


if __name__ == '__main__':
    image_path = "filter_sample.jpg"
    main(image_path)
