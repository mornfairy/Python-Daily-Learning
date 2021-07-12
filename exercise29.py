#  题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

# x = int(input("请输入一个数字："))
#
# a = x // 10000
# b = x % 10000 // 1000
# c = x % 1000 // 100
# d = x % 100 // 10
# e = x % 10
#
# if a != 0:
#     print("5位数：", e , d , c , b , a)
# elif b != 0:
#     print("4 位数：", e, d, c, b)
# elif c != 0:
#     print("3 位数：", e, d, c)
# elif d != 0:
#     print("2 位数：", e, d)
# else:
#     print("1 位数：", e)


# 使用列表方法的reverse
num = list(input("输入一个最多五位的数字"))
print('%d位数字' % len(num))
num.reverse()
for i in num:
    print(i ,' ', end = '')
