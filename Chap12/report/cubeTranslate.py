from myTranslateCanvas import MyTranslateCanvas

from cube import Cube


def main():
    canvas = MyTranslateCanvas()
    dispObj = Cube()
    canvas.init(dispObj)
    canvas.loop()


if __name__ == "__main__":
    main()
