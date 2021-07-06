# 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

# string = input("请输入一串字符串：")
#
# letter = 0
# space = 0
# number = 0
# other = 0
#
# for i in string:
#     if 'a' < i < 'z' or 'A' < i < 'Z':
#         letter += 1
#     elif i == ' ':
#         space += 1
#     elif '0' <= i <= '9':  #不能不给数字加单引号，因为i是被当作字符型变量处理的，而不加单引号的数字是整型变量，不能直接比较
#         number += 1
#     else:
#         other += 1
#
# print('字母个数为：%d，空格个数为：%d，数字个数为：%d，其他字符个数为：%d' % (letter, space, number, other))


# 答案解法

import string
s = input('请输入一个字符串:\n')
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print ('char = %d,space = %d,digit = %d,others = %d' % (letters,space,digit,others))
