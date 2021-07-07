# 题目：一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

# 我的解法，没解决
# l1 = []
# for i in range(1, 1001):
#     l2 = []
#     sum = 0
#     for j in range(1, i):
#         if i % j == 0:
#             l2.append(j)
#             sum += j
# print(l2)
# total = 0
# for k in range(0, len(l2)):
#     total += l2[k]
#     print(total)

for i in range(1, 1001):
    sum = 0
    for j in range(1, i):
        if i % j == 0:
            sum += j
    if sum == i:
        print(i)

# from sys import stdout
#
# for j in range(2, 1001):
#     k = []
#     n = -1
#     s = j
#     for i in range(1, j):
#         if j % i == 0:
#             n += 1
#             s -= i
#             k.append(i)
#
#     if s == 0:
#         print(j)
#         for i in range(n):
#             stdout.write(str(k[i]))
#             stdout.write(' ')
#         print(k[n])
