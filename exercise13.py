# 题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

# for i in range(100,1000):
#     a = int(i / 100)
#     b = int(i / 10 % 10)
#     c = int(i % 10)
#     if i == a*a*a + b*b*b + c*c*c:
#         print(i)
#         print(a, b, c)

# 方法二

for i in range(100, 1000):
    s = str(i)
    #print(s)
    if int(s[0]) **3 +int(s[1]) ** 3 + int(s[2]) ** 3 == i:
        print(i)
