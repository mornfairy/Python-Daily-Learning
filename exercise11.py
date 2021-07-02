# 题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？

def rabbit(m):  #def后面为函数名，括号内的变量为自变量
    if m == 1 or m == 2:
        return 1   #return后面的就是函数运算最后的结果
    else:
        return rabbit(m-1) + rabbit(m-2)
print(rabbit(18))

