"""
練習1：英制單位英寸與公制單位釐米互換
Version: 0.1
Author: Johnson
"""

# value = int(input ('1. 英吋 \n2. 釐米 \n請輸入單位： '))
# length_value = float(input('請輸入長度： '))

# def switch(value):
#     if value == 1:
#         print("%.2f 英吋為 %.2f 釐米" %(length_value, length_value*2.54))
#     elif value == 2:
#         print("%.2f 釐米為 %.2f 英吋" %(length_value, length_value/2.54))
#     else :
#         print("單位錯誤，請重新輸入")
# switch(value)

# """
# 練習2：百分制成績轉換為等級製成績。
# 要求：如果輸入的成績在90分以上（含90分）輸出A；80分-90分（不含90分）輸出B；70分-80分（不含80分）輸出C；60分-70分（不含70分）輸出D；60分以下輸出E。
# Version: 0.1
# Author: Johnson
# """

# value= int(input("請輸入成績 :"))

# if value >= 90:
#     print ("成績為 A")
# elif value >= 80:
#     print ("成績為 B")
# elif value >= 70:
#     print ("成績為 C")
# elif value >= 60:
#     print ("成績為 D")
# elif value < 60:
#     print ("成績為 E")



"""
判斷輸入的邊長能否構成三角形，如果能則計算出三角形的周長和麵積
Version: 0.1
Author: John
"""
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周長: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面積: %f' % (area))
else:
    print('不能構成三角形')