# 题目：数字比较。

def compare(num1, num2):
    if num1 > num2:
        print('%s 大于 %s' %(num1, num2))
    elif num1 < num2:
        print('%s 小于 %s' %(num1, num2))
    else:
        print('%s 等于 %s' %(num1, num2))

if __name__ == "__main__":
    num1 = input("请输入第一个数字：")
    num2 = input("请输入第二个数字：")
    compare(num1, num2)
