# 题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

# 最简单最暴力的方法直接判断是几位数，取出每一位，对应位值进行比较

# num = list(input("请输入一个数字："))
#
# for i in range(len(num)):
#     if i < len(num)-1-i and num[i] == num[len(num) - i - 1]:
#         print('回文数', end=' ')   # 也可以判断，但问题是每次只要满足条件就会输出这句
#     else:
#         break

#  高赞解法

a = input("输入一串数字：")
b = a[::-1]  #核心点在此处，将输入当成字符串然后用字符串的切片方法
if a == b:
    print("%s是回文数" %a)
else:
    print("%s不是回文数" %a)
