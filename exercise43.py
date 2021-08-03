# 题目：求输入数字的平方，如果平方运算后小于 50 则退出。


while True:  # 不把主程序放入while循环中，主程序结构体就只执行一次
    num = int(input("请输入数字: "))
    b = num * num
    if b >= 50:
        print(b)
        break  # 此处不加break不能跳出
    else:
        print("请继续输入")

# while True:
#     x = int(input('input a num :'))
#     x *= x
#     print('结果为：{}'.format(x))
#     if x > 50:
#         break
