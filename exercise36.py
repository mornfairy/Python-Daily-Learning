# 题目：求100之内的素数。素数，只能被1和自身整除的数
import math
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

