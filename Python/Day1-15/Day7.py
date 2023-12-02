import os
import time


def main():
    content = '北京歡迎你為你開天闢地…………'
    while True:
        # 清理螢幕上的輸出
        os.system('clear')  # os.system('cls')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
    main()