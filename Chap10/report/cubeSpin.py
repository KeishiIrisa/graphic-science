from mySpinCanvas import MySpinCanvas
from Chap10.report.cube import Cube


def main():
    canvas = MySpinCanvas()
    dispObj = Cube()
    canvas.init(dispObj)
    canvas.loop()


if __name__ == "__main__":
    main()
