# 题目：使用lambda来创建匿名函数。

# 使用匿名函数来判断两个数的大小

max = lambda x, y: (x > y) * x + (x < y) * y
min = lambda x, y: (x > y) * y + (x < y) * x

if __name__ == "__main__":
    a = int(input('请输入第一个数：'))
    b = int(input('请输入第二个数：'))
    print('较大数字为：%d' % max(a, b))
    print('较小数字为：%d' % min(a, b))

