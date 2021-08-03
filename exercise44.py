# 题目：两个变量值互换。

a = int(input("请输入一个数字： "))
b = int(input("请输入一个数字： "))

c = a
a = b
b = c

print(a)
print(b)
print(c)