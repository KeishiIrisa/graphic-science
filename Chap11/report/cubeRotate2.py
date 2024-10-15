from myRotateCanvas import MyRotateCanvas
from cube2 import Cube


def main():
    canvas = MyRotateCanvas()
    dispObj = Cube()
    canvas.init(dispObj)
    canvas.loop()


if __name__ == "__main__":
    main()
