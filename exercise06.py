#  题目：斐波那契数列。
#
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# 即第三个数字为前两个数字之和
# 在数学上，费波那契数列是以递归的方法来定义：
#
# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)
# # 参考了之前的代码
# a = 0
# b = 1
#
# for _ in range(50):
#     a, b = b,a + b  #这一步不好整
#     print(a,end =' ')

# # 使用函数定义方法
#
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# print(fib(10))

def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a
print(fib(10))