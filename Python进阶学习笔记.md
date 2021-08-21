### Python进阶学习笔记

#### 1. 分支与循环结构的应用

##### 1.1 水仙花数

![image-20210821214008875](https://cdn.jsdelivr.net/gh/Sirwenhao/images/C:%5CUsers%5CWH%5CAppData%5CRoaming%5CTypora%5Ctypora-user-images202108212140938.png)

关键知识点：利用python中的$//$和`%`运算符取出一个数字的每一位。`//`表示地板除法，取中间为数有两种写法。

```
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

```
num = int(input("请输入一个整数："))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10

print(reversed_num)
```

