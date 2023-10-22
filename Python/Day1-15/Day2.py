a = 321
b = 12
print(a + b)    # 333
print(a - b)    # 309
print(a * b)    # 3852
print(a / b)    # 26.75


# a = 100
# b = 12.345
# c = 1 + 5j
# d = 'hello, world'
# e = True
# print(type(a))    # <class 'int'>
# print(type(b))    # <class 'float'>
# print(type(c))    # <class 'complex'>
# print(type(d))    # <class 'str'>
# print(type(e))    # <class 'bool'>

# a = int(input('a = '))
# b = int(input('b = '))
# print ('%d + %d = %d' % (a, b, a + b))
# print ('%d - %d = %d' % (a, b, a - b))
# print ('%d * %d = %d' % (a, b, a * b))
# print ('%d / %d = %f' % (a, b, a / b))
# print ('%d // %d = %d' % (a, b, a // b))
# print ('%d %% %d = %d' % (a, b, a % b))
# print ('%d ** %d = %d' % (a, b, a ** b))


# """
# 將華氏溫度轉換為攝氏溫度

# Version: 0.1
# Author: Johnson
# """
# f = float(input('f = '))
# c = (f - 32) / 1.8
# print ("%.1f 華氏溫度= %.1f 攝氏溫度" % (f, c))


"""
輸入半徑計算圓的周長和麵積

Version: 0.1
Author: Johnson
"""
radius = float(input('請輸入圓的半徑: '))
perimeter = 2 * 3.1416 * radius
area = radius * radius * 3.1416 
print('周長: %.2f' % perimeter)
print('面積: %.2f' % area)