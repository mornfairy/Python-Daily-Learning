#python100 day1 practice

#p1:

# f = float(input('请输入华氏温度：'))
# c = (f - 32)/1.8
# print('%.1f华氏度 = %.1f摄氏度'%(f,c))


#p2:

# r = float(input('请输入半径：'))
# pi = 3.1415926
# s = pi * pow(r,2)
# c = 2 * pi * r
# print('面积为：%.2f'%s + '\n')
# print('周长为: %.2f'%c)


#p3:

# year = int(input('请输入年份：'))
# is_leap = year % 4 == 0 and year % 100 != 0 or \
# year % 400 == 0
# print('year' + '是闰年')

# year = int(input('请输入年份: '))
# # 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
# is_leap = year % 4 == 0 and year % 100 != 0 or \
#           year % 400 == 0
# print(is_leap)

# #p4(英寸厘米互换)
#
# value = float(input('请输入长度：'))
# unit = input('请输入单位：')
# if unit == 'in' or unit == '英寸':
#     print('%f英寸 = %f厘米' %(value,value * 2.54))
# elif unit == 'cm' or unit == '厘米':\
#     print('%f厘米 = %f英寸' %(value,value / 2.54))
# else:
#     print('请输入有效的单位')

# #P5成绩等级转换
#
# grades = float(input('请输入成绩：'))
# if  100 >= grades >= 90:
#     print('A')
# elif  80 <= grades < 90:
#     print('B')
# elif 70 <= grades <80:
#     print('C')
# elif 60 <= grades < 70:
#     print('D')
# elif grades > 100 or grades < 0:
#     print('输入错误')
# else:
#     print('E')   程序太过简单，不能分辨输入是否为分数

# #P6计算三角形面积和周长
#
# a = float(input('请输入边长a:'))
# b = float(input('请输入边长b:'))
# c = float(input('请输入边长c:'))

# #判断能否构成三角形
#
# if (a+b) <= c:
#     print('输入不符合规则，请重新输入')
# elif (a+c) <= b:
#     print('输入不符合规则，请重新输入')
# elif (b+c) <= a:
#     print('输入不符合规则，请重新输入')
# else:
#     cl = a + b + c
#     d = cl / 2
#     print('周长为:%.2f'%cl)
#     e = d*(d-a)*(d-b)*(d-c)
#     s = pow(e,0.5)
#     print('面积为:%.2f'%s)

# #水仙花数计算
#
####my
#
# a = int(input('请输入整数a: '))
#
# b = int(input('请输入整数b：'))
#
# c = int(input('请输入整数c: '))
#
# e = a*100 + b*10 + c
#
# if a**3 + b**3 + c**3 == e:
#     print('%d是水仙花数'%e)
# else:
#     print('输入不符合条件')

# ####author
#
# for num in range(100,1000):
#     low = num % 10
#     mid = num // 10 % 10   #python除法双斜杠为向下取整，3.5//2 = 1
#     high = num // 100
#     if num == low ** 3 + mid ** 3 + high ** 3:
#         print(num)


# # 正整数反转
#
# #先mark作者的程序，我的想法应该不对（考虑位数逐个取出）
#
# # num = int(input('num = '))
# # reversed_num = 0
# # while num > 0:
# #     reversed_num = reversed_num * 10 + num % 10
# #     num //= 10
# # print(reversed_num)
#
# num = int(input('请输入数字:'))
#
# reversed_num = 0
#
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     #print(reversed_num)   #此步可以可视化整个过程
#     num //= 10   #这步贼厉害，就是在此步把原数的最后一位去掉，并把去掉之后的值给num
#     print(num)
# print(reversed_num)

# #百钱百鸡问题
#
# #我没写出来
#
# # a = int()
# #
# # b = int()
# #
# # c = int()
# #
# # while a*5 + b*3 + c/3 == 100:
# #     print('%d公鸡数:'%a)
# #     print('%d母鸡数:'%b)
# #     print('%d小鸡数:'%c)
#
# #author
#
# for x in range(0,20):
#     for y in range(0,33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z / 3 == 100:
#             print('公鸡：%d只，母鸡：%d只，小鸡：%d只'%(x,y,z))


# #CRAPS赌博游戏
#
# #设定玩家初始有一千元，钱输完算结束
#
# from random import randint
#
# money = 1000
#
# while money > 0:
#     print('你的总资产为:',money)
#     needs_go_on = False
#     while True:
#         debt = int(input('请下注: '))
#         if 0 < debt <= money:
#             break
#     first = randint(1,6) + randint(1,6)
#     print('玩家摇出了%d点'% first)
#     if first == 7 or first == 11:
#         print('玩家胜!')
#         money += debt
#     elif first == 2 or first == 3 or first == 12:
#         print('庄家胜!')
#         money -= debt
#     else:
#         needs_go_on = True
#     while needs_go_on:
#         needs_go_on = False
#         current = randint(1,6) + randint(1,6)
#         print('玩家摇出了%d点'%current)
#         if current == 7:
#             print('庄家胜!')
#             money -= debt
#         elif current == first:
#             print('玩家胜！')
#             money += debt
#         else:
#             needs_go_on = True
# print('你破产了，游戏结束回家吧！！！')

# #练习斐波那契数列
#
# a = 0 #int(input('输入整数:'))
#
# b = 1 #int(input('输入整数:'))
#
#
# for _ in range(20):
#     a,b = b,a+b  #这一步没有想到以此种方式替换
#     print(a,end=' ')
# #     c =  a + b
# # a = b
# # b = c
# # c = a + b
#
#
# #author
#
# # a = 0
# # b = 1
# # for _ in range(20):
# #     a, b = b, a + b
# #     print(a, end=' ')

# #完美数
#
# import math
#
# for i in range(1,1000):
#     result = 0
#     for num in range(1,int(math.sqrt(i)) + 1):   # 这一步比较难想出来，math.sqrt(i) + 1为啥要用这种？？？
#         if i % num == 0:
#             result += num
#             if num > 1 and i // num != num:
#                 result += i // num
#     if result == i:
#         print(i)

# #输入M和N计算C(M,N)
#
# m = int(input('m = '))
#
# n = int(input('n = '))
#
# fm = 1
# for num in range(1,m + 1):
#     fm *= num
# fn = 1
# for num in range(1,n + 1):
#     fn *= num
# fm_n = 1
# for num in range(1,m - n +1):
#     fm_n *= num
# print(fm // fn // fm_n)

#
# def fac(num):
#     """求阶乘"""
#     result = 1
#     for n in range(1,num + 1):
#         result *= n
#     return result
# m = int(input('m = '))
# n = int(input('n = '))
#
# print(fac(m) // fac(n) // fac(m - n))


# from random import randint
#
# def roll_dice(n=2):
#     """摇色子"""
#     total = 0
#     for _ in range(n):
#         total += randint(1,6)
#     return total
# def add(a = 0,b = 0,c = 0):
#     """三个数相加"""
#     return a + b + c
#
# print(roll_dice())
#
# print(roll_dice(3))
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))
#
# print(add(c = 50,a = 100,b = 200))


# 在参数名前面的*表示args是一个可变参数

# def add(*args):
#     total = 0
#     for val in args:
#         total += val
#     return total

#在调用add函数时可以传入0个或者多个参数

# print(add())
# print(add(1))
# print(add(1,2))
# print(add(1,2,3))
# print(add(1,3,5,7,9))


# #P7 最大公约数最小公倍数
#
# x = int(input('请输入x：'))
# y = int(input('请输入y：'))
#
# def gcd(x,y):
#     """求最大公约数"""
#     (x,y) = (y,x) if x > y else (x,y)  #先比较大，找出大小值
#     for factor in range(x, 0, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor
# def lcm(x,y):
#     """求最小公倍数"""
#     return x * y // gcd(x,y)  #双斜杠表示地板除法，向下取整


# #P8 定义回文数，回文数是指1234321之类的，正反读都相同的数字
#
# def is_palindrome(num):
#     """判断一个数是不是回文数"""
#     temp = num
#     total = 0
#     while temp > 0:
#         total = total * 10 + temp % 10 #temp除10取余数作为个位数，作为新的total，下一次乘10升为十位数
#         temp //= 10  #temp除10向下取整可以留下依此取出十位、百位、千位等等
#     return total == num
#
#
#
# #P9 判断一个数字是不是素数,质数是指在大于1的自然数中，除了1和它本身以外不再有其他因数的自然数
# def is_prime(num):
#     """判断一个数是不是素数"""
#     for factor in range(2,int(num ** 0.5) + 1):
#         if num % factor == 0:
#             return False
#     return True if num != 1 else False
#
#
# #P10 写一个程序判断输入的正整数是不是回文素数，上述两个模块是函数体，下面的部分是真正的给参数，调用函数的部分
#
# if __name__ == '__main__':
#     num = int(input('请输入正整数：'))
#     if is_palindrome(num) and is_prime(num):
#         print('%d是回文素数'%num)


# s1 = '\'hello, world!\''
# s2 = '\n\\hello, world!\\\n'
# print(s1, s2, end='')

# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2, end='')


# #example
#
# s1 = 'hello ' * 3
# print(s1)
# s2 = 'world'
# s1 += s2
# print(s1)
# print(s2)
#
# print('ll' in s1)
# str2 = 'abc123456'
#
# print(str2[2]) #从0开始正数第二个元素
#
# print(str2[2:5]) #从0开始第二个到第五个元素，不包含第五个
# print(str2[2:])  #从第二个元素开始到结尾
# print(str2[2::2])  #从第二个开始到结尾每次步长为2
# print(str2[::2])   #从开始到结尾，步长为2
# print(str2[::-1])  #从结尾到开始，步长为1
# print(str2[-3:-1]) #从结尾开始到倒数第三个，不包含倒数第一个


# #example
#
# str1 = 'hello, world!'
# print(len(str1))  #通过内置函数len计算字符串长度
#
# print(str1.capitalize())  #将字符串首字母大写后输出
#
# print(str1.title())    #将字符串的每个单词首字母大写之后输出
#
# print(str1.upper())    #将字符串变成大写之后输出
#
# print(str1.find('or')) #查找子串在字符串中的位置
# print(str1.find('shit'))  #找不到不会引发异常
#
# print(str1.index('or')) #与find作用类似，但找不到会引发异常
# #print(str1.index('shit'))  #找不到，引发异常
#
# print(str1.startswith('He'))  #检查字符串是否以指定的字符开始，返回值为布尔类型
# print(str1.startswith('hel'))
#
# print(str1.endswith('!'))    #检查字符串是否以指定的字符结尾
#
# print(str1.center(50,'*'))   #将字符串以指定的宽度剧中并在两侧填充指定字符
# print(str1.rjust(50,' '))    #将字符串以指定的宽度靠右放置并在左侧填充指定字符
#
# str2 = 'abc123456'
# # 检查字符串是否由数字构成
# print(str2.isdigit())  # False
# # 检查字符串是否以字母构成
# print(str2.isalpha())  # False
# # 检查字符串是否以数字和字母构成
# print(str2.isalnum())  # True
# str3 = '  jackfrued@126.com '
# print(str3)
# # 获得字符串修剪左右两侧空格之后的拷贝
# print(str3.strip())



#如何定义列表、遍历列表以及列表的下标运算

# list1 = [1, 3, 5, 7, 100]
# print(list1) # [1, 3, 5, 7, 100]
# # 乘号表示列表元素的重复
# list2 = ['hello'] * 3
# print(list2) # ['hello', 'hello', 'hello']
# # 计算列表长度(元素个数)
# print(len(list1)) # 5
# # 下标(索引)运算
# print(list1[0]) # 1
# print(list1[4]) # 100
# # print(list1[5])  # IndexError: list index out of range
# print(list1[-1]) # 100
# print(list1[-3]) # 5
# list1[2] = 300
# print(list1) # [1, 3, 300, 7, 100]
# # 通过循环用下标遍历列表元素
# for index in range(len(list1)):
#     print(list1[index])
# # 通过for循环遍历列表元素
# for elem in list1:
#     print(elem)
# # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
# for index, elem in enumerate(list1):
#     print(index, elem)



# #如何向列表中添加元素以及如何从列表中移除元素
#
# list1 = [1, 3, 5, 7, 100]
# # 添加元素
# list1.append(200)
# list1.insert(1, 400)
# # 合并两个列表
# # list1.extend([1000, 2000])
# list1 += [1000, 2000]
# print(list1) # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
# print(len(list1)) # 9
# # 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
# if 3 in list1:
# 	list1.remove(3)
# if 1234 in list1:
#     list1.remove(1234)
# print(list1) # [1, 400, 5, 7, 100, 200, 1000, 2000]
# # 从指定的位置删除元素
# list1.pop(0)
# list1.pop(len(list1) - 1)
# print(list1) # [400, 5, 7, 100, 200, 1000]
# # 清空列表元素
# list1.clear()
# print(list1) # []


# #和字符串一样，列表也可以切片、复制以及创建新的列表
#
# fruits = ['grape', 'apple', 'strawberry', 'waxberry']
# fruits += ['pitaya', 'pear', 'mango']
# # 列表切片
# fruits2 = fruits[1:4]
# print(fruits2) # apple strawberry waxberry
# # 可以通过完整切片操作来复制列表
# fruits3 = fruits[:]
# print(fruits3) # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
# fruits4 = fruits[-3:-1]   #如果是从右向左进行切片操作的话，最后一个元素是存在的，即此例中倒数第三个元素
# print(fruits4) # ['pitaya', 'pear']
# # 可以通过反向切片操作来获得倒转后的列表的拷贝
# fruits5 = fruits[::-1]
# print(fruits5) # ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']


# #对列表的排序
#
# list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
# list2 = sorted(list1)
# # sorted函数返回列表排序后的拷贝不会修改传入的列表
# # 函数的设计就应该像sorted函数一样尽可能不产生副作用
# list3 = sorted(list1, reverse=True)
# # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
# list4 = sorted(list1, key=len)
# print(list1)
# print(list2)
# print(list3)
# print(list4)
# # 给列表对象发出排序消息直接在列表对象上进行排序
# list1.sort(reverse=True)
# print(list1)



# #使用列表的生成式语法创建列表
#
# import sys
#
# f = [x for x in range(1, 10)]
# print(f)
# f = [x + y for x in 'ABCDE' for y in '1234567']
# print(f)
# # 用列表的生成表达式语法创建列表容器
# # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
# f = [x ** 2 for x in range(1, 1000)]
# print(sys.getsizeof(f))  # 查看对象占用内存的字节数
# print(f)
# # 请注意下面的代码创建的不是一个列表而是一个生成器对象
# # 通过生成器可以获取到数据但它不占用额外的空间存储数据
# # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
# f = (x ** 2 for x in range(1, 1000))
# print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
# print(f)
# for val in f:
#     print(val)


# #生成斐波那契数列的生成器
#
# def fib(n):
#     a,b = 0,1
#     for _ in range(n):
#         a,b = b,a+b
#         yield a
# def main():
#     for val in fib(20):
#         print(val)
#
# if __name__ == '__main__':
#     main()


# #定义元组
#
# t = ('文豪', 27, True, '河南许昌')
# print(t)
#
# #获取元组中的元素
# print(t[0])
# print(t[3])
#
# #遍历元组中的值
#
# for member in t:
#     print(member)
#
# # 重新给元组赋值
# #t[0] '王呆胖'  #TypeError
# # 变量t重新引用了新的元组原来的元组将被垃圾回收
#
# t = ('王呆胖', 25, True, '山东日照')
# print(t)

# #将元组转换成列表
# person = list(t)  #输出之后，括号变化了，圆括号变成了方括号
# print(person)
#
# #列表修改元素
#
# person[0] = '李小龙'
# person[1] = 25
# print(person)
#
# #将列表转换成元组
# fruits_list = ['apple', 'banana', 'orange']
# fruits_tuple = tuple(fruits_list)
# print(fruits_tuple)



# #创建字典的字面量语法
#
# scores = {'文豪': 94, '白元芳': 78, '狄仁杰': 82}
# print(scores)
# # 创建字典的构造器语法
# items1 = dict(one=1, two=2, three=3, four=4)
# # 通过zip函数将两个序列压成字典
# items2 = dict(zip(['a', 'b', 'c'], '123'))
# # 创建字典的推导式语法
# items3 = {num: num ** 2 for num in range(1, 10)}
# print(items1, items2, items3)
# # 通过键可以获取字典中对应的值
# print(scores['文豪'])
# print(scores['狄仁杰'])
# # 对字典中所有键值对进行遍历
# for key in scores:
#     print(f'{key}: {scores[key]}')
# # 更新字典中的元素
# scores['白元芳'] = 65
# scores['诸葛王朗'] = 71
# scores.update(冷面=67, 方启鹤=85)
# print(scores)
# if '武则天' in scores:
#     print(scores['武则天'])
# print(scores.get('武则天'))
# # get方法也是通过键获取对应的值但是可以设置默认值
# print(scores.get('武则天', 60))
# # 删除字典中的元素
# print(scores.popitem())
# print(scores.popitem())
# print(scores.pop('文豪', 100))
# # 清空字典
# scores.clear()
# print(scores)



# #P1 在屏幕上显示跑马灯
#
# import os
# import time
#
# def main():
#     content = '今天你学python了吗？......'
#     while True:
#         #清理屏幕上的输出
#         os.system('cls')  # os.system('clear')
#         print(content)
#         #休眠200毫秒
#         time.sleep(0.2)
#         content = content[1:] + content[0]
#
# if __name__ == '__main__':
#     main()


# #P2 设计一个函数产生指定长度的验证码，验证码有大小写字母和数字组成
#
# import random
#
# def generate_code(code_len = 6):
#     """生成指定长度的验证码
#     :param code_len:验证码的长度默认为六个字符
#     :return:有大小写英文字母和数字构成的随机验证码"""
#
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0, last_pos)
#         code += all_chars[index]
#     return code


# #P3 设计一个函数返回给定文件名的后缀名
#
# def get_suffix(filename, has_dot=False):
#     """获取文件名的后缀名
#
#     ：param filename:文件名
#     :param has_dot:返回的后缀名是否需要带点
#     :return:文件名的后缀名"""
#
#     pos = filename.rfind('.')
#     if 0 < pos < len(filename) - 1:
#         index = pos if has_dot else pos + 1
#         return filename[index:]   #先找.的位置，找到之后进行切片操作，并将切片留下的后缀名返回
#     else:
#         return ''


# #P4 设计一个函数返回传入的列表中最大和第二大的元素的值
#
# def max2(x):
#     m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1],x[0])  #判断大小
#     for index in range(2,len(x)):   #遍历列表循环
#         if x[index] > m1:           #判断当前值与现存最大值的大小
#             m2 = m1
#             m1 = x[index]
#         elif x[index] > m1:
#             m2 = x[index]
#     return m1,m2


# #P5 计算指定的年月日是这一年的第几天
#
# def is_leap_year(year):
#     """判断指定的年份是不是闰年
#     :param year: 年份
#     :return: 闰年返回True平年返回False"""
#
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
# def which_day(year, month, date):
#     """计算传入的日期是这一年的第几天
#
#     :param year:年
#     :param month:月
#     :param date:日
#     :return:第几天"""
#
#     闰年与平年不同，要区分二月的天数，因此需要将每个月的月数拿出来做两个列表
#     days_of_month = [[31,28,31,30,31,30,31,31,30,31,30,31],
#                      [31,29,31,30,31,30,31,31,30,31,30,31]][is_leap_year(year)]
#
#     total = 0
#     for index in range(month - 1):
#         total += days_of_month[index]
#     return total + date
#
# def main():
#     print(which_day(1980, 11, 28))
#     print(which_day(1981, 12, 31))
#     print(which_day(1994, 12, 3))
#     print(which_day(2016, 3, 1))
#
# if __name__ == '__main__':
#     main()


# #P6 打印杨辉三角
#
# def main():
#     num = int(input('Number of rows'))
#     yh = [[]] * num
#     for row in range(len(yh)):
#         yh[row] = [None] * (row + 1)
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                yh[row][col] = 1
#             else:
#                 yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
#             print(yh[row][col], end='\t')
#         print()
#
# if __name__ == '__main__':
#     main()


# #案例1 双色球
#
# from random import randrange, randint, sample
#
# def display(balls):
#     """输出列表中的双色球号码"""
#     for index, ball in enumerate(balls):
#         if index == len(balls) - 1:
#             print('|', end = ' ')
#         print('%02d' % ball, end = ' ')
#     print()
#
# def random_select():
#     """随机选择一组号码"""
#     red_balls = [x for x in range(1,34)]
#     selected_balls = []
#     selected_balls = sample(red_balls, 6)
#     selected_balls.sort()
#     selected_balls.append(randint(1, 16))
#     return selected_balls
#
# def main():
#     n = int(input('机选几注: '))
#     for _ in range(n):
#         display(random_select())
#
#
# if __name__ == '__main__':
#     main()


# #案例2
#
# """
# 《幸运的基督徒》
# 有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
# """
#
#
# def main():
#     persons = [True] * 30
#     counter, index, number = 0, 0, 0
#     while counter < 15:
#         if persons[index]:
#             number += 1
#             if number == 9:
#                 persons[index] = False
#                 counter += 1
#                 number = 0
#         index += 1
#         index %= 30
#     for person in persons:
#         print('基' if person else '非', end='')
#
#
# if __name__ == '__main__':
#     main()


# #案例3
#
# import os
#
#
# def print_board(board):
#     print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
#     print('-+-+-')
#     print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
#     print('-+-+-')
#     print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])
#
#
# def main():
#     init_board = {
#         'TL': ' ', 'TM': ' ', 'TR': ' ',
#         'ML': ' ', 'MM': ' ', 'MR': ' ',
#         'BL': ' ', 'BM': ' ', 'BR': ' '
#     }
#     begin = True
#     while begin:
#         curr_board = init_board.copy()
#         begin = False
#         turn = 'x'
#         counter = 0
#         os.system('clear')
#         print_board(curr_board)
#         while counter < 9:
#             move = input('轮到%s走棋, 请输入位置: ' % turn)
#             if curr_board[move] == ' ':
#                 counter += 1
#                 curr_board[move] = turn
#                 if turn == 'x':
#                     turn = 'o'
#                 else:
#                     turn = 'x'
#             os.system('clear')
#             print_board(curr_board)
#         choice = input('再玩一局?(yes|no)')
#         begin = choice == 'yes'
#
#
# if __name__ == '__main__':
#     main()



class Studetn(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为学生对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)







































# #绘制国旗
#
# import turtle
#
#
# def draw_rectangle(x,y,width,height):
#     """"绘制矩形"""
#     turtle.goto(x,y)
#     turtle.pencolor('red')
#     turtle.fillcolor('red')
#     turtle.begin_fill()
#     for i in range(2):
#         turtle.forward(width)
#         turtle.left(90)
#         turtle.forward(height)
#         turtle.left(90)
#         turtle.end_fill()
#
# def draw_star(x,y,radius):
#     """"绘制五角星"""
#     turtle.setpos(x,y)
