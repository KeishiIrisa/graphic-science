from PIL import Image, ImageTk
import numpy as np
from tkinter import Tk, Canvas


def sepia(image):
    height, width, _ = image.shape
    for i in range(height):
        for j in range(width):
            original_red = image[i][j][0]
            original_green = image[i][j][1]
            original_blue = image[i][j][2]

            # セピアへの変換公式
            sepia_red = round(.393 * original_red + .769 * original_green + .189 * original_blue)
            sepia_green = round(.349 * original_red + .686 * original_green + .168 * original_blue)
            sepia_blue = round(.272 * original_red + .534 * original_green + .131 * original_blue)

            image[i][j][0] = min(255, sepia_red)
            image[i][j][1] = min(255, sepia_green)
            image[i][j][2] = min(255, sepia_blue)
    return image


def display(canvas, image):
    pil_image = Image.fromarray(np.uint8(image))

    tk_image = ImageTk.PhotoImage(pil_image)

    # canvasの中心に配置するように変更
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
    image_data = sepia(image_data)
    display(canvas, image_data)
    root.mainloop()


if __name__ == '__main__':
    image_path = "filter_sample.jpg"
    main(image_path)
