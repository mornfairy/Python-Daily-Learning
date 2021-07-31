# 题目：求一个3*3矩阵主对角线元素之和。
# 程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。

matrix = [[7, 2, 7], [35, 63, 7], [7, 8, 10]]
sum  = 0
for i in range(0, 3):
    sum += matrix[i][i]
    print(sum)