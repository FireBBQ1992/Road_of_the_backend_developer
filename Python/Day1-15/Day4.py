"""
練習1：練習1：輸入一個正整數判斷是不是素數。
提示：素數指的是隻能被1和自身整除的大於1的整數。
Version: 0.1
Author: Johnson
"""

# input_number=int(input("請輸入一個正整數 : "))
# is_prime = True
# for number in range(2, input_number):
#     if input_number % number == 0 :
#         is_prime = False
#         break
         
# if is_prime and input_number != 1:
#     print('%d 是素數' % input_number)
# else:
#     print('%d 不是素數' % input_number)

"""
練習2：輸入兩個正整數，計算它們的最大公約數和最小公倍數。
提示：兩個數的最大公約數是兩個數的公共因子中最大的那個數；兩個數的最小公倍數則是能夠同時被兩個數整除的最小的那個數。
Version: 0.1
Author: Johnson
"""

# x = int(input('x = '))
# y = int(input('y = '))

# if x > y:
#     x, y = y, x
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print ("x : %d 和 y : %d 的最大公因數為 %d " %(x, y, factor) )
#         print ("x : %d 和 y : %d 的最小公倍數為 %d " %(x, y, x * y // factor ) )
#         break



"""
練習3：列印如下所示的三角形圖案。
=============================
*
**
***
****
*****
=============================
    *
   **
  ***
 ****
*****
=============================
    *
   ***
  *****
 *******
*********
=============================
Version: 0.1
Author: Johnson
"""
row = int(input("請輸入行數 : "))

for i in range(row):
    for _ in range(i + 1):
        print ("*", end="")
    print ()

print ("=======================")

#優化前
# for i in range(row):
#     for _ in range(row - i - 1 ):
#         print (" ", end="")
#     for _ in range(i + 1):
#         print ("*", end="")
#     print ()

#優化後
# for i in range(row):
#     for j in range(row):
#         if j < row -i -1:
#             print (" ", end="")
#         else :
#             print ("*", end="")
#     print ()

print ("=======================")

# for i in range(row):
#     for _ in range(row - i - 1):
#         print (" ", end="")
#     for _ in range(2 * i + 1): 
#         print ("*", end="")
#     print ()