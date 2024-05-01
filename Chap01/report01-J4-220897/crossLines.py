from crossLine import main
import sys

# 引数にint型の回数が指定されていることを確認
if len(sys.argv) <= 1:
    count = int(input("count - >"))
elif sys.argv[2].isdigit():
    count = int(sys.argv[2])
else:
    count = int(input("count - >"))


if __name__ == '__main__':
    for i in range(count):
        main()
        print("Done!")
