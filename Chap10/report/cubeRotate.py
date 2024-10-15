from myRotateCanvas import MyRotateCanvas
from Chap10.report.cube import Cube


def main():
    canvas = MyRotateCanvas()
    dispObj = Cube()
    canvas.init(dispObj)
    canvas.loop()


if __name__ == "__main__":
    main()