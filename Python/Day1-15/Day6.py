#練習1：實現計算求最大公約數和最小公倍數的函式。

def gcd(x,y):
    (x, y) = (y, x) if x>y else (x, y)
    for factor in range (x, 0, -1):
        if x % factor == 0 and y % factor == 0:
            return factor
def lcm(x, y):
    return x * y // gcd(x, y)

# def is_palindrome(num):
#     print ("")


if __name__ == '__main__':
    x = int(input('請輸入第一個數字 :'))
    y = int(input('請輸入第二個數字 :'))
    print ("%d 和 %d 的最大公因數為 %d , 最小公倍數為 %d" %(x,y, gcd(x,y), lcm(x,y)))