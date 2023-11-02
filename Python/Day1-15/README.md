# Python
- 1989年由 Guido von Rossum 創建的編譯器。
- 第一個Python編譯器（直譯器）誕生於1991年2月，由C語言實現且可呼叫 C 語言庫函式。初版 Python 已提供了“類”，“函式”，“異常處理” 等構造塊支援，還有對列表、字典等核心資料型別，同時支援以模組為基礎來構造應用程式。
- Python 1.0 正式釋出於1994年1月。
- Python 2.0 釋出於2000年10月16日，

## 變數與型別

-  整數 (int)： 任意大小的整數數字，可支援二/八/十/十六進位。
-  浮點數：小數，有分數學算法與科學計算法。
-  字串：以單引號或雙引號括起來的任意文字，比如'hello'和"hello",字串還有原始字串表示法、位元組字串表示法、Unicode字串表示法。
-  布林值:只有 `True`、`False` 兩種值。
-  複數：形如3+5j，跟數學上的複數表示一樣，唯一不同的是虛部的i換成了j。實際上，這個型別並不常用。

## 分支結構

### if 語句的使用
  > 構造分支結構可以使用 `if`、`elif`和`else`關鍵字，
  > 與C/C++、Java等語言不同，Python中沒有用花括號來構造程式碼塊而是**使用了縮排的方式來表示程式碼的層次結構**


## 循環結構
- 程式中控制某條或某些指令重複執行的結構。在 Python 中構造迴圈結構有兩種做法，一種是 `for-in` 迴圈，一種是 `while` 迴圈。

### for-in 迴圈
> 已知迴圈執行的次數或者要對一個容器進行迭代

例子
```
sum = 0
for x in range(101):
    sum += x
print(sum)
```
range的用法非常靈活，下面給出了一個例子：

- range(101)：可以用來產生0到100範圍的整數，需要注意的是<font color=#FF0000>取不到101</font>。
- range(1, 101)：可以用來產生1到100範圍的整數，相當於前面是閉區間後面是開區間。
- range(1, 101, 2)：可以用來產生1到100的奇數，其中2是步長，即每次數值遞增的值。
- range(100, 0, -2)：可以用來產生100到1的偶數，其中-2是步長，即每次數字遞減的值。

### while 迴圈
- 當構造不知道具體迴圈次數的迴圈結構時，可使用 While 迴圈來判別
- while迴圈透過一個能夠產生或轉換出`bool值` 的表示式來控制迴圈，表示式的值為 `True` 則繼續迴圈；表示式的值為 `False` 則結束迴圈

例子
```
import random

answer = random.randint(1, 100)
counter = 0
while True:
    counter += 1
    number = int(input('請輸入: '))
    if number < answer:
        print('大一點')
    elif number > answer:
        print('小一點')
    else:
        print('恭喜你猜對了!')
        break
print('你總共猜了%d次' % counter)
if counter > 7:
    print('你的智商餘額明顯不足')
```

## 構造程式邏輯
> 介紹一些經典的案例及習題，來了解如何建立程式中的邏輯以及如何運用一些簡單的演算法

```

# 找出所有水仙花數
# 說明 : 水仙花數也被稱為超完全數字不變數、自戀數、自冪數、阿姆斯特朗數，它是一個3位數，該數字每個位上數字的立方之和正好等於它本身，例如：$1^3 + 5^3+ 3^3=153$。

for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)
```

```
# 正數反轉
# 說明 : 輸入一個數，可將此數做反轉，

num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
```

```
#《百錢百雞》問題
# 說明 :《 算經》一書中提出的數學問題：雞翁一值錢五，雞母一值錢三，雞雛三值錢一。百錢買百雞，問雞翁、雞母、雞雛各幾何？翻譯成現代文是：公雞5元一隻，母雞3元一隻，小雞1元三隻，用100塊錢買一百隻雞，問公雞、母雞、小雞各有多少隻？

# 提示 : 這裡主要是使用窮舉法

for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print('公雞: %d只, 母雞: %d只, 小雞: %d只' % (x, y, z))

```

## 函數與模組的使用
- 程式碼有很多種壞味道，重複是最壞的一種！ ------ Martin Fowler
- 可將重複程式碼的問題，封裝到一個稱之為“函式”的功能模組中。
- 可以使用 `def` 關鍵字來定義函式。
- 函式名後面的圓括號 `( )` 中可以放置傳遞給函式的引數。
- 函式執行完成後我們可以透過 `return` 關鍵字來返回一個值。


### 定義涵式

例子：
```

#輸入M和N計算C(M,N)
def fac(num):
    """求階乘"""
    result = 1
    for n in range(1, num + 1):
        result *= n
    return result

m = int(input('m = '))
n = int(input('n = '))
# 當需要計算階乘的時候不用再寫迴圈求階乘而是直接呼叫已經定義好的函式
print(fac(m) // fac(n) // fac(m - n))
```
> 說明 :
> - Python的 `math` 模組中其實已經有一個名為 `factorial` 函式實現了階乘運算，事實上求階乘並不用自己定義函式。
> - 實際開發中並不建議做這種低階的重複勞動。

### 涵式的引數
- Python 中，函式的引數可以有預設值，也支援使用可變引數。
- 定義一個函式的時候可以讓它有多種不同的使用方式，下列為例子。

```
from random import randint


def roll_dice(n=2):
    """搖色子"""
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total


def add(a=0, b=0, c=0):
    """三個數相加"""
    return a + b + c


# 如果沒有指定引數那麼使用預設值搖兩顆色子
print(roll_dice())
# 搖三顆色子
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
# 傳遞引數時可以不按照設定的順序進行傳遞
print(add(c=50, a=100, b=200))
```

- 以上 `add` 涵式例子有更好的實現方案，因為我們可能會對多個引數進行加法運算。
- 可使用可變引數，方法如下：

```
# 在引數名前面的*表示args是一個可變引數
def add(*args):
    total = 0
    for val in args:
        total += val
    return total


# 在呼叫add函式時可以傳入0個或多個引數
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))
```

### 模塊管理涵式

- 可能會遇到命名衝突的問題。

## Reference
 [Python-100-Days](https://github.com/ateliershen/Python-100-Days-zh_TW) 