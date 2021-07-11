# 题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

# def reverse(s, l):
#     if l == 0:
#         return
#     print(s[l-1])
#     reverse(s, l-1)
#
# s = input("请输如字符串：")
# l = len(s)
# reverse(s, l)

# # 非递归方法
#
# s = input('请输入字符串：')
# l = list(s)
# print(l)
# l.reverse()
# print(l)
# for i in l:
#     print(i)

# 我自己写的递归
def reverse(s):
    l = list(s)
    l.reverse()
    return l

s = input("请输入一段字符串：")

print(reverse(s))