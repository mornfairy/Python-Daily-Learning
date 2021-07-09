# 题目：打印出如下图案（菱形）:
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

for i in range(0, 4):
    print(' ' * (3 - i), '*' * (1 + 2 * i))
for j in range(5, 8):
    print(' ' * (j - 4), '*' * (15 - 2 * j))

# for i in range(4):
#     print((3-i) * ' ' + (2*i+1) * '*')
# for i in range(3):
#     print((i+1) * ' ' + (5-2*i) * '*')

# from sys import stdout
#
# for i in range(4):
#     for j in range(2 - i + 1):
#         stdout.write(' ')
#     for k in range(2 * i + 1):
#         stdout.write('*')
#     print('')
#
# for i in range(3):
#     for j in range(i + 1):
#         stdout.write(' ')
#     for k in range(4 - 2 * i + 1):
#         stdout.write('*')
#     print('')