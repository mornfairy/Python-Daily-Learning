### Python进阶学习笔记

#### 1. 分支与循环结构的应用

##### 1.1 水仙花数

![image-20210821214008875](https://cdn.jsdelivr.net/gh/Sirwenhao/images/C:%5CUsers%5CWH%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images202108212140938.png)

关键知识点：利用python中的$//$和`%`运算符取出一个数字的每一位。`//`表示地板除法，取中间为数有两种写法。

```python
for i in range(100, 1000):
    a = i // 100
    b = i // 10 % 10
    #b = i % 100 // 10
    c = i % 10

    if i == a ** 3 + b ** 3 + c ** 3:
        print(i)
```

##### 1.2 数字反转

我们要将一个不知道有多少位的正整数进行反转，例如将`12345`变成`54321`

```python
num = int(input("请输入一个整数："))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

print(reversed_num)
```

##### 1.3 CRAPS赌博游戏

![image-20210825222249080](https://cdn.jsdelivr.net/gh/Sirwenhao/images/C:%5CUsers%5CWH%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images202108252222152.png)

规则分析：玩家的起始资金有1000元，每次的下注金额必须大于0且小于等于玩家目前的总资产，游戏结束的条件时玩家输光所有的赌注

- 第一次摇骰子：7或者11玩家胜利    		2、3或者12庄家胜；其他点数继续摇
- 以上情况没出现继续摇时，如果点数为7，庄家胜利；如果点数为第一次的点数，玩家胜利
- 除此之外，继续摇骰子直至分出胜负

```python
from random import randint
money = 1000
while money > 0:
    print('玩家目前的总资产为：%d'%money)
    debt = int(input("请输入本次赌注："))
    while 0 < debt <= money:
        first = randint(1, 6) + randint(1, 6)
        print('玩家第一次的点数为：%d' %first)
        if first == 7 or first == 11:
            print("玩家胜利！")
            money += debt
            print(money)
        elif first == 2 or first == 3 or first == 12:
            print("庄家胜利！")
            money -= debt
            print(money)
        else:
            print("第一次掷色子没有输赢，继续摇色子")
            current = randint(1, 6) + randint(1, 6)
            if current == 7:
                print("庄家胜利！")
                money -= debt
                print(money)
            elif current == first:
                print("玩家胜利！")
                money += debt
                print(money)
print("你破产了，游戏结束！")
```

此程序是我自己所写，存在许多问题：

- 题干要求的是在第一次不成功之后，第一次的模式便不再判断了，但我所写程序中，仍然需要从最开始的输入开始判断
- 多次执行我的程序之后，会出现money累加的操作，使其超出界限

```python
from random import randint

money = 1000
while money > 0:
    print(f'你的总资产为: {money}元')
    go_on = False
    # 下注金额必须大于0小于等于玩家总资产
    while True:   #此处的while循环作用是让你输入一个满足范围的数，且必须满足范围之后才能跳出while语句，执行下面的操作
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    # 第一次摇色子
    # 用1到6均匀分布的随机数模拟摇色子得到的点数
    first = randint(1, 6) + randint(1, 6)
    print(f'\n玩家摇出了{first}点')
    if first == 7 or first == 11:
        print('玩家胜!\n')
        money += debt
        print(f'玩家胜利后钱为：{money}')
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜!\n')
        money -= debt
        print(f'庄家胜利后钱为：{money}')
    else:
        go_on = True
    # 第一次摇色子没有分出胜负游戏继续
    while go_on:  #使用go_on来控制第一次不满足条件时，不再做第一种的判断而执行下面的操作
        go_on = False
        current = randint(1, 6) + randint(1, 6)
        print(f'玩家摇出了{current}点')
        if current == 7:
            print('庄家胜!\n')
            money -= debt
            print(f'庄家胜利后钱为：{money}')
        elif current == first:
            print('玩家胜!\n')
            money += debt
            print(f'玩家胜利后钱为：{money}')
        else:
            go_on = True
print('你破产了, 游戏结束!')
```

##### 1.4 斐波那契数列

![image-20210827214200751](https://cdn.jsdelivr.net/gh/Sirwenhao/images/C:%5CUsers%5CWH%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images202108272142883.png)

程序核心体：

```python
a, b = 0, 1
for _ in range(20):
    a, b = b, a + b  # b = a + b的这个操作绝了
    print(a)
```

#### 2. Python常用数据结构之列表

​		首先列表可以做的事情：用一个变量来保存多个数据，用统一的代码对多个数据进行操作。首先，python中的列表是由一系列的元素按照一定的顺序构成的数据序列，这就意味着列表类型的变量可以==保存多个数据==，==允许有重复的数据==。`[]`代表列表，元素之间用`，`隔开，使用`list`关键字创建列表。列表是一种可变数据类型，即列表可以添加元素、删除元素、更新元素等操作。

##### 2.1 列表操作示例：

```python
items1 = [35, 12, 99, 68, 55, 87]
items2 = [45, 8, 29]
```

- 列表的拼接：

  ```python
  items3 = items1 + items2
  print(items3)    # [35, 12, 99, 68, 55, 87, 45, 8, 29]
  ```

- 列表的重复：

  ```python
  items4 = ['hello'] * 3
  print(items4)    # ['hello', 'hello', 'hello']
  ```

- 列表的成员运算：

  ```Python
  print(100 in items3)        # False
  print('hello' in items4)    # True
  ```

- 获取列表长度：

  ```python
  size = len(items3)
  print(size)                 # 9
  ```

- 列表的索引：

  ```python
  print(items3[0], items3[-size])        # 35 35
  items3[-1] = 100
  print(items3[size - 1], items3[-1])    # 100 100
  ```

- 列表的切片：

  ```python
  print(items3[:5])          # [35, 12, 99, 68, 55]
  print(items3[4:])          # [55, 87, 45, 8, 100]
  print(items3[-5:-7:-1])    # [55, 68]
  print(items3[::-2])        # [100, 45, 55, 99, 35]
  ```

- 列表的比较运算：

```python
items5 = [1, 2, 3, 4]
items6 = list(range(1, 5))
# 两个列表比较相等性比的是对应索引位置上的元素是否相等
print(items5 == items6)    # True
items7 = [3, 2, 1]
# 两个列表比较大小比的是对应索引位置上的元素的大小
print(items5 <= items7)    # True
```

- 列表正向索引的范围是：`0`到`N-1`，负向索引的范围：`-1`到`-N`

##### 2.2 掷6000次色子统计次数

```python
import random

counters = [0] * 6  #创建6个元素均为0的列表
for _ in range(6000):
    face = random.randint(1, 6)
    counters[face - 1] += 1  #此处使用face-1的原因是，列表的下标是从0开始计数的
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')
```

##### 2.3 列表的方法

- 添加和删除元素：

```python
items = ['Python', 'Java', 'Go', 'Kotlin']

# 使用append方法在列表尾部添加元素
items.append('Swift')
print(items)    # ['Python', 'Java', 'Go', 'Kotlin', 'Swift']
# 使用insert方法在列表指定索引位置插入元素
items.insert(2, 'SQL')
print(items)    # ['Python', 'Java', 'SQL', 'Go', 'Kotlin', 'Swift']

# 删除指定的元素
items.remove('Java')
print(items)    # ['Python', 'SQL', 'Go', 'Kotlin', 'Swift']
# 删除指定索引位置的元素
items.pop(0)
items.pop(len(items) - 1)
print(items)    # ['SQL', 'Go', 'Kotlin']

# 清空列表中的元素
items.clear()
print(items)    # []
```

从列表中删除元素其实还有一种方式，就是使用Python中的`del`关键字后面跟要删除的元素，这种做法跟使用`pop`方法指定索引删除元素没有实质性的区别，但后者会返回删除的元素，前者在性能上略优。

- 元素的位置和次数

```python
items = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']

# 查找元素的索引位置
print(items.index('Python'))       # 0
print(items.index('Python', 2))    # 5  此处的2表示从索引为2的位置开始找
# 注意：虽然列表中有'Java'，但是从索引为3这个位置开始后面是没有'Java'的
print(items.index('Java', 3))      # ValueError: 'Java' is not in list
```

```python
items = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']

# 查找元素出现的次数
print(items.count('Python'))    # 2
print(items.count('Go'))        # 1
print(items.count('Swfit'))     # 0
```

- 元素排序和反转

排序操作通过`.sort`实现，元素反转操作通过`.reverse`实现

```python
items = ['Python', 'Java', 'Go', 'Kotlin', 'Python']

# 排序
items.sort()
print(items)    # ['Go', 'Java', 'Kotlin', 'Python', 'Python']  此处是按字母顺序排列了
# 反转
items.reverse()
print(items)    # ['Python', 'Python', 'Kotlin', 'Java', 'Go'] 
```

- 列表生成式

```python
# 创建一个由1到9的数字构成的列表
items1 = [x for x in range(1, 10)]
print(items1)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 创建一个由'hello world'中除空格和元音字母外的字符构成的列表
items2 = [x for x in 'hello world' if x not in ' aeiou']
print(items2)    # ['h', 'l', 'l', 'w', 'r', 'l', 'd']

# 创建一个由个两个字符串中字符的笛卡尔积构成的列表
items3 = [x + y for x in 'ABC' for y in '12']
print(items3)    # ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']
```

`Python`生成式拥有好的性能的原因，`Python`解释器的字节码指令中有专门针对生成式的指令（`LIST_APPEND`指令）

Python中的列表底层是一个可以动态扩容的数组，列表元素在内存中也是连续存储的，所以可以实现随机访问（通过一个有效的索引获取到对应的元素且操作时间与列表元素个数无关）。**列表是容器**，可以**保存各种类型的数据**，**可以通过索引操作列表元素**。

#### 3. Python常用数据结构之元组

​		元组（tuple），容器型数据类型。在Python中，元组也是多个元素按照一定的顺序构成的序列。元组和列表的不同之处在于，==元组是不可变类型==，这就意味着元组类型的变量一旦定义，其中的元素不能再添加或删除，而且元素的值也不能进行修改。定义元组通常使用`()`字面量语法，也建议大家使用这种方式来创建元组。

​		需要注意的是，`()`表示空元组，但是如果元组中只有一个元素，需要加上一个逗号，否则`()`就不是代表元组的字面量语法，而是改变运算优先级的圆括号，所以`('hello', )`和`(100, )`才是一元组，而`('hello')`和`(100)`只是字符串和整数。

```python
# 空元组
a = ()
print(type(a))    # <class 'tuple'>
# 不是元组
b = ('hello')
print(type(b))    # <class 'str'>
c = (100)
print(type(c))    # <class 'int'>
# 一元组
d = ('hello', )
print(type(d))    # <class 'tuple'>
e = (100, )
print(type(e))    # <class 'tuple'>
```

​		元组的应用：当我们==把多个用逗号分隔的值赋给一个变量==时，多个值会打包成一个元组类型；当我们把一个元组赋值给多个变量时，元组会解包成多个值然后分别赋给对应的变量，如下面的代码所示。

```python
# 打包
a = 1, 10, 100
print(type(a), a)    # <class 'tuple'> (1, 10, 100)
# 解包
i, j, k = a
print(i, j, k)       # 1 10 100
```

​		在解包时，如果解包出来的元素个数和变量个数不对应，会引发`ValueError`异常，错误信息为：`too many values to unpack`（解包的值太多）或`not enough values to unpack`（解包的值不足）。

```python
a = 1, 10, 100, 1000
# i, j, k = a             # ValueError: too many values to unpack (expected 3)
# i, j, k, l, m, n = a    # ValueError: not enough values to unpack (expected 6, got 4)
```

​		有一种解决变量个数少于元素的个数方法，就是使用==星号表达式==，我们之前讲函数的可变参数时使用过星号表达式。有了星号表达式，我们就可以让一个变量接收多个值，代码如下所示。需要注意的是，用星号表达式修饰的变量会变成一个列表，列表中有0个或多个元素。还有在解包语法中，星号表达式只能出现一次。需要说明一点，解包语法对所有的序列都成立。

```python
a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)          # 1 10 [100, 1000]
i, *j, k = a
print(i, j, k)          # 1 [10, 100] 1000
*i, j, k = a
print(i, j, k)          # [1, 10] 100 1000
*i, j = a
print(i, j)             # [1, 10, 100] 1000
i, *j = a
print(i, j)             # 1 [10, 100, 1000]
i, j, k, *l = a
print(i, j, k, l)       # 1 10 100 [1000]
i, j, k, l, *m = a
print(i, j, k, l, m)    # 1 10 100 1000 []
```

​		python中的元组和列表是可以互换的

```python
# 将元组转换成列表
info = ('骆昊', 175, True, '四川成都')
print(list(info))       # ['骆昊', 175, True, '四川成都']
# 将列表转换成元组
fruits = ['apple', 'banana', 'orange']
print(tuple(fruits))    # ('apple', 'banana', 'orange')
```

​		**列表和元组都是容器型的数据类型**，即一个变量可以保存多个数据。**列表是可变数据类型**，**元组是不可变数据类型**，所以列表添加元素、删除元素、清空、排序等方法对于元组来说是不成立的。但是列表和元组都可以进行**拼接**、**成员运算**、**索引和切片**这些操作。

#### 4. Python常用数据结构之字符串

​		所谓**字符串**，就是**由零个或多个字符组成的有限序列**，字符串中的字符可以是特殊符号、英文字母、中文字符、日文的平假名或片假名、希腊字母、`Emoji`字符等。

```python
s1 = 'hello, world!'
s2 = "你好，世界！"
print(s1, s2)
# 以三个双引号或单引号开头的字符串可以折行
s3 = '''
hello, 
world!
'''
print(s3, end='')
```

**提示**：`print`函数中的`end=''`表示==输出后不换行==，即将默认的结束符`\n`（换行符）更换为`''`（空字符）。

转义字符串：

​		在字符串中使用`\`（反斜杠）来表示转义，也就是说`\`后面的字符不再是它原来的意义，例如：`\n`不是代表反斜杠和字符`n`，而是表示换行；`\t`也不是代表反斜杠和字符`t`，而是表示制表符。所以如果字符串本身又包含了`'`、`"`、`\`这些特殊的字符，必须要通过`\`进行转义处理。例如要输出一个带单引号或反斜杠的字符串，需要用如下所示的方法。

```python
s1 = '\'hello, world!\''
print(s1)  # 'hello,world!'
s2 = '\\hello, world!\\'
print(s2)  #\hello,world!\
```

原始字符串：

​		Python中的字符串可以`r`或`R`开头，这种字符串被称为原始字符串，意思是字符串中的每个字符都是它本来的含义，没有所谓的转义字符。例如，在字符串`'hello\n'`中，`\n`表示换行；而在`r'hello\n'`中，`\n`不再表示换行，就是反斜杠和字符`n`。Python中还允许在`\`后面还可以跟一个八进制或者十六进制数来表示字符，例如`\141`和`\x61`都代表小写字母`a`，前者是八进制的表示法，后者是十六进制的表示法。

```python
# 字符串s1中\t是制表符，\n是换行符
s1 = '\time up \now'
print(s1)   #	ime up
			ow	
# 字符串s2中没有转义字符，每个字符都是原始含义
s2 = r'\time up \now'
print(s2)   #\time up \now
```

字符串的运算操作：

​		Python为字符串类型提供了非常丰富的运算符，使用`+`实现字符串的拼接，使用`*`实现字符串内容的重复操作（上述例子中，创建一个六个0元素的列表时就用到了），使用`in`和`not in`判断字符串之间的从属关系，使用`[]`和`[:]`从字符串中取出某个或者某些字符。

拼接和重复：使用`+`和`*`运算符实现字符串的拼接和重复操作

```python
s1 = 'hello' + ' ' + 'world'
print(s1)    # hello world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2     # s1 = s1 + s2
print(s1)    # hello world!!!
s1 *= 2      # s1 = s1 * 2
print(s1)    # hello world!!!hello world!!!
```

比较运算：`<`，`>`，`==`，`!=`，Python中还有一个`is`运算符（身份运算符），如果用`is`来比较两个字符串，它比较的是两个变量对应的字符串对象的==内存地址==，简单的说就是两个变量是否对应内存中的同一个字符串。

```python
s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2, s1 < s2)      # False True
print(s2 == 'hello world')    # True
print(s2 == 'Hello world')    # False
print(s2 != 'Hello world')    # True
s3 = '骆昊'
print(ord('骆'), ord('昊'))               # 39558 26122
s4 = '王大锤'
print(ord('王'), ord('大'), ord('锤'))    # 29579 22823 38180
print(s3 > s4, s3 <= s4)      # True False
```

成员运算：`in`和`not in`。Python中可以用`in`和`not in`判断一个字符串中是否存在另外一个字符或字符串，`in`和`not in`运算通常称为成员运算，会产生布尔值`True`或`False`

```python
s1 = 'hello, world'
print('wo' in s1)    # True
s2 = 'goodbye'
print(s2 in s1)      # False
```

获取字符串长度：获取字符串长度没有直接的运算符，而是使用内置函数`len`

索引和切片：如果希望从字符串中取出某个字符，我们可以对字符串进行索引运算，运算符是`[n]`，其中`n`是一个整数，假设字符串的长度为`N`，那么`n`可以是从`0`到`N-1`的整数，其中`0`是字符串中第一个字符的索引，而`N-1`是字符串中最后一个字符的索引，通常称之为正向索引；在Python中，字符串的索引也可以是从`-1`到`-N`的整数，其中`-1`是最后一个字符的索引，而`-N`则是第一个字符的索引，通常称之为负向索引。注意，因为**字符串是不可变类型**，所以**不能通过索引运算修改字符串中的字符**。索引越界（正向索引不在`0`到`N-1`范围，负向索引不在`-1`到`-N`范围），会引发`IndexError`异常，错误提示信息为：`string index out of range`（字符串索引超出范围）。

​		如果要从字符串中取出多个字符，我们可以对字符串进行切片，运算符是==`[i:j:k]`==，其中`i`是开始索引，索引对应的字符可以取到；`j`是结束索引，索引对应的字符==不能取到==；`k`是步长，默认值为`1`，表示从前向后获取相邻字符的连续切片，所以`:k`部分可以省略。假设字符串的长度为`N`，当`k > 0`时表示正向切片（从前向后获取字符），如果没有给出`i`和`j`的值，则`i`的默认值是`0`，`j`的默认值是`N`；当`k < 0`时表示负向切片（从后向前获取字符），如果没有给出`i`和`j`的值，则`i`的默认值是`-1`，j的默认值是`-N - 1`。如果不理解，直接看下面的例子，记住第一个字符的索引是`0`或`-N`，最后一个字符的索引是`N-1`或`-1`就行了。

```python
s = 'abc123456'

# i=2, j=5, k=1的正向切片操作
print(s[2:5])       # c12

# i=-7, j=-4, k=1的正向切片操作
print(s[-7:-4])     # c12

# i=2, j=9, k=1的正向切片操作
print(s[2:])        # c123456

# i=-7, j=9, k=1的正向切片操作
print(s[-7:])       # c123456

# i=2, j=9, k=2的正向切片操作
print(s[2::2])      # c246

# i=-7, j=9, k=2的正向切片操作
print(s[-7::2])     # c246

# i=0, j=9, k=2的正向切片操作
print(s[::2])       # ac246

# i=1, j=-1, k=2的正向切片操作
print(s[1:-1:2])    # b135

# i=7, j=1, k=-1的负向切片操作
print(s[7:1:-1])    # 54321c

# i=-2, j=-8, k=-1的负向切片操作
print(s[-2:-8:-1])  # 54321c

# i=7, j=-10, k=-1的负向切片操作
print(s[7::-1])     # 54321cba

# i=-1, j=1, k=-1的负向切片操作
print(s[:1:-1])     # 654321c

# i=0, j=9, k=1的正向切片
print(s[:])         # abc123456

# i=0, j=9, k=2的正向切片
print(s[::2])       # ac246

# i=-1, j=-10, k=-1的负向切片
print(s[::-1])      # 654321cba

# i=-1, j=-10, k=-2的负向切片
print(s[::-2])      # 642ca
```

需换遍历每个字符：使用`for`循环循环遍历每个字符

字符串方法：在Python中，我们可以通过字符串类型自带的方法对字符串进行操作和处理，对于一个字符串类型的变量，我们可以用`变量名.方法名()`的方式来调用它的方法，所谓方法其实就是跟某个类型的变量绑定的函数。

```python
#大小写相关操作
s1 = 'hello, world!'

# 使用capitalize方法获得  字符串首字母  大写后的字符串
print(s1.capitalize())   # Hello, world!
# 使用title方法获得字符串  每个单词首字母  大写后的字符串
print(s1.title())        # Hello, World!
# 使用upper方法获得  字符串大写  后的字符串
print(s1.upper())        # HELLO, WORLD!

s2 = 'GOODBYE'
# 使用lower方法获得 字符串小写  后的字符串
print(s2.lower())        # goodbye
```

```python
#查找操作  使用find或者index方法
s = 'hello, world!'

# find方法从字符串中查找另一个字符串所在的位置
# 找到了返回字符串中另一个字符串  首字符的索引
print(s.find('or'))        # 8
# 找不到返回-1
print(s.find('shit'))      # -1
# index方法与find方法类似
# 找到了返回字符串中另一个字符串首字符的索引
print(s.index('or'))       # 8
# 找不到引发异常
print(s.index('shit'))     # ValueError: substring not found
```

​		在使用`find`和`index`方法时还可以通过方法的参数来指定查找的范围，也就是查找不必从索引为`0`的位置开始。`find`和`index`方法还有逆向查找（从后向前查找）的版本，分别是`rfind`和`rindex`，代码如下所示。

```python
s = 'hello good world!'

# 从前向后查找字符o出现的位置(相当于第一次出现)
print(s.find('o'))       # 4
# 从索引为5的位置开始查找字符o出现的位置
print(s.find('o', 5))    # 7
# 从后向前查找字符o出现的位置(相当于最后一次出现)
print(s.rfind('o'))      # 12
```

性质判断：

可以通过字符串的`startswith`、`endswith`来判断字符串是否以某个字符串开头和结尾；还可以用`is`开头的方法判断字符串的特征，这些方法都返回布尔值，代码如下所示。

```python
s1 = 'hello, world!'

# startwith方法检查字符串是否以指定的字符串开头返回布尔值
print(s1.startswith('He'))    # False
print(s1.startswith('hel'))   # True
# endswith方法检查字符串是否以指定的字符串结尾返回布尔值
print(s1.endswith('!'))       # True

s2 = 'abc123456'

# isdigit方法检查字符串是否由数字构成返回布尔值
print(s2.isdigit())    # False
# isalpha方法检查字符串是否以字母构成返回布尔值
print(s2.isalpha())    # False
# isalnum方法检查字符串是否以数字和字母构成返回布尔值
print(s2.isalnum())    # True
```

格式化字符串：

​		在Python中，字符串类型可以通过`center`、`ljust`、`rjust`方法做居中、左对齐和右对齐的处理。如果要在字符串的左侧补零，也可以使用`zfill`方法。

```python
s = 'hello, world'

# center方法以宽度20将字符串居中并在两侧填充*
print(s.center(20, '*'))  # ****hello, world****
# rjust方法以宽度20将字符串右对齐并在左侧填充空格
print(s.rjust(20))        #         hello, world
# ljust方法以宽度20将字符串左对齐并在右侧填充~
print(s.ljust(20, '~'))   # hello, world~~~~~~~~
# 在字符串的左侧补零
print('33'.zfill(5))      # 00033
print('-33'.zfill(5))     # -0033
```

`print`输出的两种格式化操作

```python
a = 321
b = 123
print('%d * %d = %d' % (a, b, a * b))
```

```python
a = 321
b = 123
print('{0} * {1} = {2}'.format(a, b, a * b))
```

​		**从Python 3.6开始，格式化字符串还有更为简洁的书写方式，就是在字符串前加上`f`来格式化字符串，在这种以`f`打头的字符串中，`{变量名}`是一个占位符，会被变量对应的值将其替换掉，代码如下所示。**

```python
a = 321
b = 123
print(f'{a} * {b} = {a * b}')
```

