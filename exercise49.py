# 题目：画图，综合例子。程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。。

for i in range(100, 1000):
    a = i / 100
    b = i % 10 / 10
    c = i % 10 % 10
    print('百位数为：%d' %a)
    print('十位数为：%d' %b)
    print('个位数为: %d' %c)
