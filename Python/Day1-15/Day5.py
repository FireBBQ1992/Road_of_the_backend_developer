# -*-coding:utf8 -*-
'''
問題一：生成斐波那契數列的前20個數。
說明：斐波那契數列（Fibonacci sequence），又稱黃金分割數列，是義大利數學家萊昂納多·斐波那契（Leonardoda Fibonacci）在《計算之書》中提出一個在理想假設條件下兔子成長率的問題而引入的數列，所以這個數列也被戲稱為"兔子數列"。斐波那契數列的特點是數列的前兩個數都是1，從第三個數開始，每個數都是它前面兩個數的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。斐波那契數列在現代物理、準晶體結構、化學等領域都有直接的應用。

問題一：找出10000以內的完美數。
說明：完美數又稱為完全數或完備數，它的所有的真因子（即除了自身以外的因子）的和（即因子函式）恰好等於它本身。例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美數。完美數有很多神奇的特性，有興趣的可以自行了解。

問題一：輸出100以內所有的素數。
說明：素數指的是隻能被1和自身整除的正整數（不包括1）。

上面練習的參考答案在本章對應的程式碼目錄中，如果需要幫助請讀者自行檢視參考答案。
'''
# 問題一
# array = []
# a = 0
# b = 1
# for _ in range(20):
#     a, b = b, a+b
#     array.append(a)
# print(array)


#問題二(方法一)
# import math
# for num in range(2, 10000):
#     result = 0
#     for factor in range(1, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             result += factor
#             if factor > 1 and num // factor != factor:
#                 result += num // factor
#     if result == num:
#         print(num)

#問題二(方法二)
# for i in range(1,10001):
#     list = []
#     sum = 0
#     for j in range(1,i):
#         if i % j == 0:
#             sum += j
#             list.append(j)
#     if i == sum :
#         print ("%d 是完美數, 因子是 "%i, list )


# 問題三
for input_number in range(2,100):
    is_prime = True
    for j in range(2, input_number):
        if input_number % j == 0:
            is_prime = False
            break
    if is_prime :
        print('%d 是素數' % input_number)


