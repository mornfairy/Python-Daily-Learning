# 题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。

# 斐波那契数列，第三项是前两项之和

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return int(fib(n-1) + fib(n-2))
s = 0.0
for i in range(1, 21):
    s += float(fib(i+2)) / float(fib(i+1))
    print("%s / %s" % (fib(i+2), fib(i+1)))