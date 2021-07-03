# 题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5

# # 确定质数个数最难
# i = int(input("请输入一个数字："))
# #l = []
# for j in range(2, i + 1):
#     if i % j == 0:
#         i //= j
#         if i == 1:
#             print(j)
#         else:
#             print('{} *'.format(j),end = ' ')
# print('{} = {}'.format(i, j), end=' ')
#     #break
#         #print(j)
#         #l.append(j)
# # print(l)


# # 答案解法
#
# def reduceNum(n):
#     print('{} = '.format(n), end = " ")
#     if not isinstance(n, int) or n < 0:
#         print('请输入一个正确的数字！')
#         exit(0)
#     elif n in [1]:
#         print('{}'.format(n))
#     while n not in [1]:
#         for index in range(2, n+1):
#             if n % index == 0:
#                 n //= index
#                 if n == 1:
#                     print(index)
#                 else:
#                     print('{} *'.format(index),end = ' ')
#                 break
# reduceNum(90)
# reduceNum(100)


# 高分解法

def prime(n):
    l = []
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                n = int(n / i)  #这一步想不出来
                l.append(i)
                break
    return l

s = input("输入一个正整数：")
if s.isdigit() and int(s) > 0:
    print(s, "=", "*".join([str(x) for x in prime(int(s))]))
else:
    print("请输入正确的正整数：")