#練習1：實現計算求最大公約數和最小公倍數的函式。

# def gcd(x,y):
#     (x, y) = (y, x) if x>y else (x, y)
#     for factor in range (x, 0, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor
# def lcm(x, y):
#     return x * y // gcd(x, y)

def is_palindrome(num):
    x = num
    while  x <= 0 or  x % 10 == 0:
        return 
    hou = 0
    while (x > hou) :
        hou = hou * 10 + x % 10
        x //= 10
    if  x == hou or x == (hou//10) :
        print ( f"{num} 是迴文數！" )
    else :
        print ( f"{num} 不是迴文數！" )

    

if __name__ == '__main__':
    # x = int(input('請輸入第一個數字 :'))
    # y = int(input('請輸入第二個數字 :'))
     z = int(input('請輸入迴文數 : '))

    # print ("%d 和 %d 的最大公因數為 %d , 最小公倍數為 %d" %(x,y, gcd(x,y), lcm(x,y)))
    # print (is_palindrome(z))