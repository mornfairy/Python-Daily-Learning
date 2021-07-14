# 题目：练习函数调用。
# 程序分析：使用函数，输出三次 RUNOOB 字符串。

def hello_runoob():
    print('RUNOOB')

def hello_runoobs():
    for i in range(3):
        hello_runoob()

if __name__ == '__main__':
    hello_runoobs()


# 此处记录一下if __name__ == '__main__'的作用以及运行机制

# 作用：一个python文件通常有两种使用方法，第一种是作为脚本直接执行；第二种是import到其他的python程序中当作被调用模块执行。
# if __name__ == '__name__'的作用就是控制这两种情况的执行。在if __name__ == '__main__'的情况下，第一种情况被执行。当
# 被当作模块引入时，只执行if __name__ == '__main__'之前的语句，之后的没有执行。

#if __name__ == '__main__':的原理

# 每个python模块（python文件，也就是此处的 test.py 和 import_test.py）都包含内置的变量 __name__，当该模块被直接执行的时候
# __name__ 等于文件名（包含后缀 .py ）；如果该模块 import 到其他模块中，则该模块的 __name__ 等于模块名称（不包含后缀.py）。
# 而 “__main__” 始终指当前执行模块的名称（包含后缀.py）。进而当模块被直接执行时，__name__ == 'main' 结果为真。


# 创建文件test.py
test.py

print('this is one')
print('__name__:', __name__)

if __name__ == '__main__':
    print('this is two')

# 创建文件import_test.py

import_test.py

import test