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



# class Student(object):
#
#     # __init__是一个特殊方法用于在创建对象时进行初始化操作
#     # 通过这个方法我们可以为学生对象绑定name和age两个属性
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def study(self, course_name):
#         print('%s正在学习%s.' % (self.name, course_name))
#
#     # PEP 8要求标识符的名字用全小写多个单词用下划线连接
#     # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)，驼峰标识，如myname写为MyNam此类的
#     def watch_movie(self):
#         if self.age < 18:
#             print('%s只能观看《熊出没》.' % self.name)
#         else:
#             print('%s正在观看岛国爱情大电影.' % self.name)
#
#
#
#
# def main():
#     # 创建学生对象并指定姓名和年龄
#     stu1 = Student('骆昊', 38)
#     # 给对象发study消息
#     stu1.study('Python程序设计')
#     # 给对象发watch_av消息
#     stu1.watch_movie()
#     stu2 = Student('王大锤', 15)
#     stu2.study('思想品德')
#     stu2.watch_movie()
#
#
# if __name__ == '__main__':
#     main()




# #P1 定义一个类描述数字时钟
#
# from time import sleep
#
# class Clock(object):
#
#     """数字时钟"""
#
#     def __init__(self,hour = 0,minute = 0,second = 0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#
#     def run(self):
#
#         """走字"""
#
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#     def show(self):
#
#         """显示时间"""
#
#         return '%02d:%02d:%02d' % \
#                (self._hour, self._minute, self._second)
#
#
# def main():
#     clock = Clock(21, 51, 10)
#     while True:
#         print(clock.show())
#         sleep(1)
#         clock.run()
#
#
# if __name__ == '__main__':
#     main()


# #P2  定义一个类描述平面上的点并提供移动点何计算到另一个点的距离
#
# from math import sqrt
#
# class Point(object):
#     def __init__(self,x=0, y=0):
#
#         """初始化方法"""
#         self.x = x
#         self.y = y
#
#     def move_to(self,x,y):
#         """移动到指定位置"""
#         self.x = x
#         self.y = y
#
#     def move_by(self,dx,dy):
#         self.x += dx
#         self.y += dy
#
#     def distance_to(self, other):
#         """计算与另一个点的距离"""
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return sqrt(dx ** 2 + dy ** 2)
#
#     def __str__(self):
#         return '(%s, %s)' % (str(self.x), str(self.y))
#
# def main():
#     p1 = Point(3,5)
#     p2 = Point()
#     print(p1)
#     print(p2)
#     p2.move_by(-1, 2)
#     print(p2)
#     print(p1.distance_to(p2))
#
# if __name__ == '__main__':
#     main()



# #使用tkinter做一个简单的GUI应用
#
# import tkinter
# import tkinter.messagebox
#
#
# def main():
#     flag = True
#
#     #修改标签上的文字
#     def change_label_text():
#         nonlocal flag
#         flag = not flag
#         color, msg = ('red', 'Hello,world!')\
#             if flag else ('blue', 'Goodbye,world!')
#         label.config(text = msg,fg = color)
#
#     #确认退出
#     def confirm_to_quit():
#         if tkinter.messagebox.askokcancel('温馨提示','确定要退出码？'):
#             top.quit()
#
#     #创建顶层窗口
#     top = tkinter.Tk()
#     #设置窗口大小
#     top.geometry('240x160')
#     #设置窗口标题
#     top.title('小游戏')
#     #创建标签对象并添加到顶层窗口
#     laebl = tkinter.Label(top,text = 'Hello,World!', font = 'Arial -32',fg = 'red')
#     laebl.pack(expand = 1)
#     # 创建一个装按钮的容器
#     panel = tkinter.Frame(top)
#     # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
#     button1 = tkinter.Button(panel, text='修改', command=change_label_text)
#     button1.pack(side='left')
#     button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
#     button2.pack(side='right')
#     panel.pack(side='bottom')
#     # 开启主事件循环
#     tkinter.mainloop()
#
#
# if __name__ == '__main__':
#     main()



# #P 使用pygame制作游戏窗口
#
# import pygame
#
# def main():
#     #初始化导入pygame模块
#     pygame.init()
#     #初始化用于显示的窗口并设置窗口尺寸
#     screen = pygame.display.set_mode((800, 600))
#     #设置当前窗口的标题
#     pygame.display.set_caption('大球吃小球')
#     running = True
#     #开启一个事件循环处理发生的事件
#     while running:
#         #聪消息队列中获取事件并对事件进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
# if __name__ == '__main__':
#     main()



# import pygame
#
# def main():
#     #初始化导入的pygame中的模块
#     pygame.init()
#     #初始化用于显示的窗口并设置窗口的尺寸
#     screen = pygame.display.set_mode((800, 600))
#     #设置当前窗口的标题
#     pygame.display.set_caption('大球吃小球')
#     #定义变量来表示小球在屏幕上的位置
#     x,y = 50,50
#     running = True
#     #开启一个事件循环处理发生的事件
#     while running:
#         #从消息队列中获取时间并对时间进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#
#         #设置窗口的背景颜色（颜色是由红绿蓝三原色构成的元组）
#         screen.fill((242, 242, 242))
#     # 通过指定的文件名加载图像
#     #ball_image = pygame.image.load('./res/ball.png')
#         #绘制一个圆（参数分别是：屏幕，颜色，圆心位置，半径，0表示填充圆）
#         pygame.draw.circle(screen,(255, 0, 0), (x, y),30,0)
#      #刷新当前窗口（渲染窗口将绘制的图像呈现出来）
#         pygame.display.flip()
#         #没个50毫秒就改变小球的位置再刷新窗口
#         pygame.time.delay(50)
#         x, y = x + 5, y + 5
#         #running = True
#         #开启一个事件循环处理发生的事件
#         #while running:
#         #从消息队列中获取时间并对时间进行处理
#         #for event in pygame.event.get():
#             #if event.type == pygame.QUIT:
#                 #running = False
#
# if __name__ == '__main__':
#     main()



# from enum import Enum, unique
# from math import sqrt
# from random import randint
#
# import pygame
#
#
# @unique
# class Color(Enum):
#     """颜色"""
#
#     RED = (255, 0, 0)
#     GREEN = (0, 255, 0)
#     BLUE = (0, 0, 255)
#     BLACK = (0, 0, 0)
#     WHITE = (255, 255, 255)
#     GRAY = (242, 242, 242)
#
#     @staticmethod
#     def random_color():
#         """获得随机颜色"""
#         r = randint(0, 255)
#         g = randint(0, 255)
#         b = randint(0, 255)
#         return (r, g, b)
#
#
# class Ball(object):
#     """球"""
#
#     def __init__(self, x, y, radius, sx, sy, color=Color.RED):
#         """初始化方法"""
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.sx = sx
#         self.sy = sy
#         self.color = color
#         self.alive = True
#
#     def move(self, screen):
#         """移动"""
#         self.x += self.sx
#         self.y += self.sy
#         if self.x - self.radius <= 0 or \
#                 self.x + self.radius >= screen.get_width():
#             self.sx = -self.sx
#         if self.y - self.radius <= 0 or \
#                 self.y + self.radius >= screen.get_height():
#             self.sy = -self.sy
#
#     def eat(self, other):
#         """吃其他球"""
#         if self.alive and other.alive and self != other:
#             dx, dy = self.x - other.x, self.y - other.y
#             distance = sqrt(dx ** 2 + dy ** 2)
#             if distance < self.radius + other.radius \
#                     and self.radius > other.radius:
#                 other.alive = False
#                 self.radius = self.radius + int(other.radius * 0.146)
#
#     def draw(self, screen):
#         """在窗口上绘制球"""
#         pygame.draw.circle(screen, self.color,
#                            (self.x, self.y), self.radius, 0)
#
#
#
# def main():
#     # 定义用来装所有球的容器
#     balls = []
#     # 初始化导入的pygame中的模块
#     pygame.init()
#     # 初始化用于显示的窗口并设置窗口尺寸
#     screen = pygame.display.set_mode((800, 600))
#     # 设置当前窗口的标题
#     pygame.display.set_caption('大球吃小球')
#     running = True
#     # 开启一个事件循环处理发生的事件
#     while running:
#         # 从消息队列中获取事件并对事件进行处理
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             # 处理鼠标事件的代码
#             if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                 # 获得点击鼠标的位置
#                 x, y = event.pos
#                 radius = randint(10, 100)
#                 sx, sy = randint(-10, 10), randint(-10, 10)
#                 color = Color.random_color()
#                 # 在点击鼠标的位置创建一个球(大小、速度和颜色随机)
#                 ball = Ball(x, y, radius, sx, sy, color)
#                 # 将球添加到列表容器中
#                 balls.append(ball)
#         screen.fill((255, 255, 255))
#         # 取出容器中的球 如果没被吃掉就绘制 被吃掉了就移除
#         for ball in balls:
#             if ball.alive:
#                 ball.draw(screen)
#             else:
#                 balls.remove(ball)
#         pygame.display.flip()
#         # 每隔50毫秒就改变球的位置再刷新窗口
#         pygame.time.delay(50)
#         for ball in balls:
#             ball.move(screen)
#             # 检查球有没有吃到其他的球
#             for other in balls:
#                 ball.eat(other)
#
#
# if __name__ == '__main__':
#     main()


# #将1-9999之间的所有素数保存在三个txt文件中，1-99，100-999，1000-9999
#
#
# from math import sqrt
#
# def is_prime(n):
#     """判断素数的函数"""
#     assert n > 0
#     for factor in range(2, int(sqrt(n)) + 1):
#         if n % factor == 0:
#             return False
#     return True if n != 1 else False
#
#
# def main():
#     filenames = ('a.txt', 'b.txt', 'c.txt')
#     fs_list = []
#     try:
#         for filename in filenames:
#             fs_list.append(open(filename, 'w', encoding = 'utf-8'))
#         for number in range(1,10000):
#             if is_prime(number):
#                 if number < 100:
#                     fs_list[0].write(str(number) + '\n')
#                 elif number < 1000:
#                     fs_list[1].write(str(number) + '\n')
#                 else:
#                     fs_list[2].write(str(number) + '\n')
#     except IOError as ex:
#         print(ex)
#         print('写文件时发生错误!')
#     finally:
#         for fs in fs_list:
#             fs.close()
#         print('操作完成！')
#
# if __name__ == '__main__':
#     main()



# #将字典或者列表以JSON格式保存到文件中
#
# import json
#
# def main():
#     mydict = {
#         'name': '文豪',
#         'age' : 27,
#         'phone' : 18539068687,
#         'friends' : ['王大锤', '白元芳'],
#         'cars' : [
#             {'brand': 'Audi', 'max_speed' : 280},
#             {'brand': 'Benz', 'max_speed' : 320},
#         ]
#     }
#     try:
#         with open('data.json', 'w',encoding = 'utf-8') as fs:
#             json.dump(mydict,fs)
#     except IOError as e:
#         print(e)
#     print('保存数据完成!')
#
# if __name__ == '__main__':
#     main()


# # 求平方函数
#
# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)
#
#     print(squares)

# #更简洁的方法
#
# squares = []
# for value in range(1,11):
#     squares.append(value ** 2)
#     print(squares)




# #绘制国旗
#
# import turtle
#
#
# def draw_rectangle(x, y, width, height):
#     """"绘制矩形"""
#     turtle.goto(x, y)
#     turtle.pencolor('red')
#     turtle.fillcolor('red')
#     turtle.begin_fill()
#     for i in range(2):
#         turtle.forward(width)
#         turtle.left(90)
#         turtle.forward(height)
#         turtle.left(90)
#     turtle.end_fill()
#
# def draw_star(x, y, radius):
#     """"绘制五角星"""
#     turtle.setpos(x, y)
#     pos1 = turtle.pos()
#     turtle.circle(-radius, 72)
#     pos2 = turtle.pos()
#     turtle.circle(-radius, 72)
#     pos3 = turtle.pos()
#     turtle.circle(-radius, 72)
#     pos4 = turtle.pos()
#     turtle.circle(-radius, 72)
#     pos5 = turtle.pos()
#     turtle.color('yellow', 'yellow')
#     turtle.begin_fill()
#     turtle.goto(pos3)
#     turtle.goto(pos1)
#     turtle.goto(pos4)
#     turtle.goto(pos2)
#     turtle.goto(pos5)
#     turtle.end_fill()
#
#
# def main():
#     """主程序"""
#     turtle.speed(12)
#     turtle.penup()
#     x,y = -270, -180
#
#     #画国旗主体
#     width, height = 540, 360
#     draw_rectangle(x, y, width, height)
#
#     #画大星星
#     pice = 22
#     center_x, center_y = x + 5 * pice, y + height - pice * 5
#     turtle.goto(center_x, center_y)
#     turtle.left(90)
#     turtle.forward(pice * 3)
#     turtle.right(90)
#     draw_star(turtle.xcor(), turtle.ycor(), pice * 3)
#     x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]
#
#     #画小星星
#     for x_pos, y_pos in zip(x_poses, y_poses):
#         turtle.goto(x + x_pos * pice, y + height - y_pos * pice)
#         turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
#         turtle.forward(pice)
#         turtle.right(90)
#         draw_star(turtle.xcor(), turtle.ycor(), pice)
#
#     #隐藏海龟
#     turtle.ht()
#
#     #显示绘画窗口
#     turtle.mainloop()
#
#
# if __name__ == '__main__':
#     main()



# #绘制小猪佩奇
#
# """
# 绘制小猪佩奇
# """
# from turtle import *
#
#
# def nose(x,y):
#     """画鼻子"""
#     penup()
#     # 将海龟移动到指定的坐标
#     goto(x,y)
#     pendown()
#     # 设置海龟的方向（0-东、90-北、180-西、270-南）
#     setheading(-30)
#     begin_fill()
#     a = 0.4
#     for i in range(120):
#         if 0 <= i < 30 or 60 <= i <90:
#             a = a + 0.08
#             # 向左转3度
#             left(3)
#             # 向前走
#             forward(a)
#         else:
#             a = a - 0.08
#             left(3)
#             forward(a)
#     end_fill()
#     penup()
#     setheading(90)
#     forward(25)
#     setheading(0)
#     forward(10)
#     pendown()
#     # 设置画笔的颜色(红, 绿, 蓝)
#     pencolor(255, 155, 192)
#     setheading(10)
#     begin_fill()
#     circle(5)
#     color(160, 82, 45)
#     end_fill()
#     penup()
#     setheading(0)
#     forward(20)
#     pendown()
#     pencolor(255, 155, 192)
#     setheading(10)
#     begin_fill()
#     circle(5)
#     color(160, 82, 45)
#     end_fill()
#
#
# def head(x, y):
#     """画头"""
#     color((255, 155, 192), "pink")
#     penup()
#     goto(x,y)
#     setheading(0)
#     pendown()
#     begin_fill()
#     setheading(180)
#     circle(300, -30)
#     circle(100, -60)
#     circle(80, -100)
#     circle(150, -20)
#     circle(60, -95)
#     setheading(161)
#     circle(-300, 15)
#     penup()
#     goto(-100, 100)
#     pendown()
#     setheading(-30)
#     a = 0.4
#     for i in range(60):
#         if 0<= i < 30 or 60 <= i < 90:
#             a = a + 0.08
#             lt(3) #向左转3度
#             fd(a) #向前走a的步长
#         else:
#             a = a - 0.08
#             lt(3)
#             fd(a)
#     end_fill()
#
#
# def ears(x,y):
#     """画耳朵"""
#     color((255, 155, 192), "pink")
#     penup()
#     goto(x, y)
#     pendown()
#     begin_fill()
#     setheading(100)
#     circle(-50, 50)
#     circle(-10, 120)
#     circle(-50, 54)
#     end_fill()
#     penup()
#     setheading(90)
#     forward(-12)
#     setheading(0)
#     forward(30)
#     pendown()
#     begin_fill()
#     setheading(100)
#     circle(-50, 50)
#     circle(-10, 120)
#     circle(-50, 56)
#     end_fill()
#
#
# def eyes(x,y):
#     """画眼睛"""
#     color((255, 155, 192), "white")
#     penup()
#     setheading(90)
#     forward(-20)
#     setheading(0)
#     forward(-95)
#     pendown()
#     begin_fill()
#     circle(15)
#     end_fill()
#     color("black")
#     penup()
#     setheading(90)
#     forward(12)
#     setheading(0)
#     forward(-3)
#     pendown()
#     begin_fill()
#     circle(3)
#     end_fill()
#     color((255, 155, 192), "white")
#     penup()
#     seth(90)
#     forward(-25)
#     seth(0)
#     forward(40)
#     pendown()
#     begin_fill()
#     circle(15)
#     end_fill()
#     color("black")
#     penup()
#     setheading(90)
#     forward(12)
#     setheading(0)
#     forward(-3)
#     pendown()
#     begin_fill()
#     circle(3)
#     end_fill()
#
#
# def cheek(x,y):
#     """画脸颊"""
#     color((255, 155, 192))
#     penup()
#     goto(x,y)
#     pendown()
#     setheading(0)
#     begin_fill()
#     circle(30)
#     end_fill()
#
#
# def mouth(x,y):
#     """画嘴巴"""
#     color(239, 69, 19)
#     penup()
#     goto(x, y)
#     pendown()
#     setheading(-80)
#     circle(30, 40)
#     circle(40, 80)
#
#
# def setting():
#     """设置参数"""
#     pensize(4)
#     # 隐藏海龟
#     hideturtle()
#     colormode(255)
#     color((255, 155, 192), "pink")
#     setup(840, 500)
#     speed(10)
#
#
# def main():
#     """主函数"""
#     setting()
#     nose(-100, 100)
#     head(-69, 167)
#     ears(0, 160)
#     eyes(0, 140)
#     cheek(80, 10)
#     mouth(-20, 30)
#     done()
#
#
# if __name__ == '__main__':
#     main()

# #华氏度转摄氏度
#
# f = float(input('请输入华氏温度：'))
# c = (f - 32) / 1.8
# print('%.1f华氏度 = %.1f摄氏度' % (f, c))

#给半径，计算圆的面积和周长

# r = float(input('请输入半径:'))
# pi = 3.1415926
# s = pi * r * r
# c = 2 * pi * r
# print('面积为:%.1f\n周长为:%.1f' % (s, c))

# import math
#
# radius = float(input('请输入圆的半径:'))
# perimeter = 2 * math.pi * radius
# area = math.pi * radius * radius
# print('周长：%.2f' % perimeter)
# print('面积：%.2f' % area)

# #用for循环实现1-100求和
#
# sum = 0
# for a in range(1,101):
#     sum += a
# print(sum)

#print(sum([i for i in range(1,101)]))
#print(sum(range(1,101)))
#用while实现求和
# sum = 0
# num = 1
# while num <= 100:
#     sum += num
#     num += 1
# print(sum)

# #输入两个正整数计算最大公约数和最小公倍数
#
# x = int(input("请输入整数："))
# y = int(input("请输入整数："))
# if x > y:
#     (x,y) = (y,x)
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print("%d和%d的最大公约数为：%d" %(x,y,factor))
#         print("%d和%d的最小公倍数为：%d"%(x,y,x*y//factor))  #这一步牛逼
#         break


# 打印各种三角图案

# row = int(input("请输入行数："))
# for i in range(row):
#     for _ in range(i + 1):
#         print('*',end='')
#     print()
#
# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ',end='')
#         else:
#             print('*',end='')
#     print()

# for i in range(row):
#     for _ in range(row - i -1):
#         print(' ',end='')
#     for _ in range(2 * i + 1):5
#          print('*',end='')
#     print()


# #斐波那契数列
#
# a = 0
# b = 1
# for _ in range(20):
#     a, b = b, a + b
#     print(a, end=' ')

# # 回文数
#
# num = int(input('请输入一个正整数：'))
# temp = num
# num2 = 0
# while temp > 0:
#     num2 *= 10
#     num2 += temp % 10
#     temp //= 10
# if num == num2:
#     print('%d是回文数' % num)
# else:
#     print('%d不是回文数' % num)


# # 完美数（1-10000）
#
# import math
#
# for num in range(1,10000):
#     result = 0
#     for factor in range(1, int(math.sqrt(num)) + 1):
#         if num % factor == 0:
#             result += factor
#             if factor > 1 and num // factor != factor:
#                 result += num // factor
#     if result == num:
#         print(num)



# #定义函数，求最大公约数和最小公倍数
#
# def gcd(x, y):
#     if x > y:
#         (x, y) = (y, x)
#     for factor in range(x, 1, -1):
#         if x % factor == 0 and y % factor == 0:
#             return factor
#     return 1
#
# def lcm(x, y):
#     return x * y // gcd(x, y)
#
# print(gcd(15, 27))
# print(lcm(15, 27))



# #排序算法（选择、冒泡和归并）
#
# """简单选择排序"""
# def select_sort(items, comp=lambda x, y: x < y):
#     items = items[:]
#     for i in range(len(items) - 1):
#         min_index = i
#         for j in range(i + 1, len(items)):
#             if comp(items[j], items[min_index]):
#                 min_index = j
#         items[i], items[min_index] = items[min_index], items[i]
#     return items

# #python生成式（推导式）用法，用于生成列表、集合和字典
#
# prices = {'AAPL': 191.88,
#           'GOOG': 1186.96,
#           'IBM': 149.24,
#           'ORCL': 48.44,
#           'ACN': 166.89,
#           'FB': 208.09,
#           'SYMC': 21.29}
#
# prices2 = {key: value for key,value in prices.items() if value > 100}
# print(prices2)


# #列表的嵌套
#
# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# scores = [[None] * len(courses) for _ in range(len(names))]
#          #有几门课程就用几个空列表[None]做占位符,所以直接乘以courses列表的长度
# for row, name in enumerate(names):   #enumerate首先列出第一个元素的下标0和值关羽
#     # enumerate是枚举，列出元素的下标和对应的值
#     for col, course in enumerate(courses):#enumerate列出courses中的第一个值的下标和值
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
#         print(scores)

#

# heapq模块（堆排序）
#
# """从列表中找出最大的或最小的N个元素
# 堆结构（大根堆/小根堆）"""
#
#
# import heapq
#
# list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
# list2 = [
#     {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
#     {'name': 'ACME', 'shares': 75, 'price': 115.65}
# ]
# print(heapq.nlargest(3, list1))    #最大元素的输出顺序默认为由大到小
# print(heapq.nsmallest(3, list1))   #最小元素的输出顺序默认为由小到大
# print(heapq.nlargest(2, list2, key=lambda x: x['price']))  #根据关键词price和shares找出最大的
# print(heapq.nlargest(2, list2, key=lambda x: x['shares']))

# """迭代工具模块"""
#
# import itertools
#
# #产生ABCD的全排列
# itertools.permutations('ABCD')
# #产生ABCDE的五选三组合
# itertools.combinations('ABCDE', 3)
# #产生ABCD和123的笛卡尔积
# itertools.product('ABCD', '123')
# #产生ABC的无限循环序列
# itertools.cycle(('A', 'B', 'C'))

# #找出序列中出现次数最多的元素
#
# from collections import Counter
#
# words = [
#     'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
#     'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
#     'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
#     'look', 'into', 'my', 'eyes', "you're", 'under'
# ]
# counter = Counter(words)
# print(counter.most_common(3))


# # 简单选择排序结构体
#
# def select_sort(items, comp=lambda x, y: x < y):
#     """简单选择排序"""
#     items = items[:]
#     for i in range(len(items) - 1):
#         min_index = i
#         for j in range(i + 1, len(items)):
#             mid_index = j
#         items[i], items[min_index] = items[min_index], items[i]
#     return items

# #简单选择排序实例
#
# import sys
# A = [64, 25, 12, 11, 22]
#
# for i in range(len(A)):
#     min_index = i
#     for j in range(i + 1, len(A)):
#         if A[min_index] > A[j]:
#             min_index = j
#     A[i], A[min_index] = A[min_index], A[i]
# print("排序后的数组为：")
# for i in range(len(A)):
#     print("%d" % A[i])


# #冒泡排序结构体
#
# def bubble_sort(items, comp=lambda x, y: x > y):
#     items = items[:]
#     for i in range(len(items) - 1):
#         swapped = False
#         for j in range(len(items) - 1 - i):
#             if comp(items[j], items[j+1]):
#                 items[j], items[j + 1] = items[j + 1], items[j]
#                 swapped = True
#         if not swapped:
#             break
#     return items


# #冒泡排序实例
#
# nums = []
#
# print('冒泡排序(降序排序)')
# while True:
#     print('请输入你想排列的数字个数：')
#     try:
#         x = int(input())  #此处将输入的数字个数赋值给x
#         for i in range(x):
#             a = int(input('请输入第' + str(i+1) + '个整数：'))  #此处记得要将i转为字符串类型
#             nums.append(a)   #使用append方法将a附加到nums列表中
#     except ValueError:
#         print('输入错误，请重新输入：')
#
#     for j in range(len(nums) -1):
#         for k in range(len(nums) - j - 1):
#             if nums[k] < nums[k + 1]:
#                 nums[k], nums[k + 1] = nums[k + 1],nums[k]
#     print(nums)
#
#     jud = input('您是否想要继续？(Y/N)')
#     while jud != 'Y' and jud != 'N':
#         jud = input('输入错误，请重新输入：')
#     if jud == 'Y':
#         nums.clear()
#         continue
#     else:
#         print('再见！')
#         break


# #搅拌排序（冒泡排序的升级版）
#
#
# def bubble_sort(items, comp=lambda x, y: x > y):
#     items = items[:]
#     for i in range(len(items) - 1):
#         swapped = False
#         for j in range(len(items) - 1 - i):
#             if comp(items[j], items[j + 1]):
#                 items[j], items[j + 1] = items[j + 1], items[j]
#                 swapped = True
#         if swapped:
#             swapped = False
#             for j in range(len(items) - 2 - i, i, -1):
#                 if comp(items[j - 1], items[j]):
#                     items[j], items[j - 1] = items[j - 1],items[j]
#                     swapped = True
#         if not swapped:
#             break
#     return items


# #python搅拌排序(即双向冒泡排序)
#
# def bubble_sort(origin_items):
#     comp = lambda x, y: x > y
#     items = origin_items[:]
#     for i in range(len(items) - 1):
#         swapped = False
#         for j in range(i, len(items) - 1 - i):
#             if comp(items[j], items[j + 1]):
#                 items[j], items[j + 1] = items[j + 1], items[j]
#                 swapped = True
#         if swapped:
#             swapped = False
#             for j in range(len(items) - 2 - i, i, -1):
#                 if comp(items[j - 1], items[j]):
#                     items[j], items[j - 1] = items[j - 1], items[j]
#                     swapped = True
#         if not swapped:
#             break
#     return items
#
#
# def main():
#     s = [1, 10, 2, 8, 5, 10, 11, 14, 15, 16]
#     print(bubble_sort(s))
#
# if __name__ == '__main__':
#     main()


# #合并两个有序列表
#
# def merge(items1, items2, comp=lambda x, y: x < y):
#     """合并（将两个有序的列表合成一个有序的列表）"""
#     items = []
#     index1, index2 = 0, 0
#     while index1 < len(items1) and index2 < len(items2):
#         if comp(items1[index1], items2[index2]):
#             items.append(items1[index1])
#             index1 += 1
#         else:
#             items.append(items2[index2])
#             index2 += 1
#     items += items1[index1:]
#     items += items2[index2:]
#     return items
#
# def merge_sort(items, comp=lambda x, y: x < y):
#     return _merge_sort(list(items), comp)
#
# def _merge_sort(items, comp):
#     """归并排序"""
#     if len(items) < 2:
#         return items
#     mid = len(items) // 2
#     left = _merge_sort(items[:mid], comp)
#     right = _merge_sort(items[mid:], comp)
#     return merge(left, right, comp)

# def seq_search(items, key):
#     """顺序查找"""
#     for index, item in enumerate(items):
#         if item == key；
#         return index
#     return -1    #return -1表示不成功

# def bin_search(items, key):
#     """"折半查找"""
#     start, end = 0, len(items) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if key > items[mid]:
#             start = mid + 1
#         elif key < items[mid]:
#             end = mid - 1
#         else:
#             return mid
#     return -1


# #穷举法实例
#
# #公鸡5元一只  母鸡3元一只  小鸡1元三只
# #用100元买100只鸡  问公鸡、母鸡、小鸡各多少只
#
# for x in range(20):
#     for y in range(33):
#         z = 100 - x - y
#         if 5 * x + 3 * y + z // 3 == 100 and z % 3 ==0:
#             print(x, y, z)

# # 五人分鱼
#
# #A,B,C,D,E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# # 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# # B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# # 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
#
# fish = 6
# while True:
#     total = fish
#     enough = True
#     for _ in range(5):
#         if (total - 1) % 5 == 0:
#             total = (total - 1) // 5 * 4
#         else:
#             enough = False
#             break
#     if enough:
#         print(fish)
#         break
#     fish += 5
#     贪婪法例子：假设小偷有一个背包，最多能装20公斤赃物，他闯入一户人家，发现如下表所示的物品。很显然，他不能把所有物品都装进背包，所以必须确定拿走哪些物品，留下哪些物品。

# 名称	价格（美元）	重量（kg）
# 电脑	200	        20
# 收音机	20	        4
# 钟	175	        10
# 花瓶	50	        2
# 书	10	        1
# 油画	90	        9
# """
# 贪婪法：在对问题求解时，总是做出在当前看来是最好的选择，不追求最优解，快速找到满意解。
# 输入：
# 20 6
# 电脑 200 20
# 收音机 20 4
# 钟 175 10
# 花瓶 50 2
# 书 10 1
# 油画 90 9
# """

# class Thing(object):
#     """物品"""
#
#     def __init__(self, name, price, weight):
#         self.name = name
#         self.price = price
#         self.weight = weight
#
#     @property
#     def value(self):
#         """价格重量比"""
#         return self.price / self.weight
#
#
# def input_thing():
#     """输入物品信息"""
#     name_str, price_str, weight_str = input().split()
#     return name_str, int(price_str), int(weight_str)
#
#
# def main():
#     """主函数"""
#     max_weight, num_of_things = map(int, input().split())
#     all_things = []
#     for _ in range(num_of_things):
#         all_things.append(Thing(*input_thing()))
#     all_things.sort(key=lambda x: x.value, reverse=True)
#     total_weight = 0
#     total_price = 0
#     for thing in all_things:
#         if total_weight + thing.weight <= max_weight:
#             print(f'小偷拿走了{thing.name}')
#             total_weight += thing.weight
#             total_price += thing.price
#     print(f'总价值: {total_price}美元')
#
#
# if __name__ == '__main__':
#     main()


# #  分治法例子：快速排序   没整明白
#
# """快速排序 - 选择枢轴元素进行划分，左边都比枢轴小右边都比枢轴大"""
#
# def quick_sort(items, comp=lambda x, y : x <= y):
#     items = list(items)[:]
#     quick_sort(items, 0, len(items) - 1, comp)
#     return items
#
# def _quick_scort(items, start, end, comp):
#     if start < end:
#         pos = _partition(items, start, end, comp)
#         _quick_scort(items, start, pos - 1, comp)
#         _quick_scort(items, pos + 1, end, comp)
#
# def _partition(items, start, end, comp):
#     pivot = items[end]
#     i = start - 1
#     for j in range(start, end):
#         if comp(items[j], pivot):
#             i += 1
#             items[i], items[j] = items[j]. items[i]
#     items[i + 1], items[end] = items[end], items[i + 1]
#     return i + 1

# # 小甲鱼python教程：类
#
# class Turtle:  #python中的类名约定以大写字母开头
#     """关于类的一个简单例子"""
#     # 属性
#     color = 'green'
#     weight = 10
#     legs = 4
#     shell = True
#     mouth = '大嘴'
#
#     # 方法
#     def climb(self):
#         print("我正在很努力的往前爬.....")
#
#     def run(self):
#         print("我正在飞快地向前爬......")
#
#     def bite(self):
#         print("咬死你")


# #  多态
#
# class A:
#     def func(self):
#         print("我是小A......")
#
# class B:
#     def fun(self):
#         print("我是小B.......")
#
# >>>a = A()
# >>>b = B()
# >>>a.fun()
# 我是小A...
# >>>b.fun()
# 我是小B...



# # 回溯法例子    不明白
#
# """回溯法又称试探法，按照选优条件向前搜索，当搜索到某一步，发现原先选择并不优或者达不到目标时，就退回一步重新选择，比较经典的问题包括骑士巡逻"""
#
# import sys
# import time
#
# SIZE = 5
# total = 0
#
# def print_board(board):
#     for row in board:
#         for col in row:
#             print(str(col).center(4), end='')
#         print()
#
# def patrol(board, row, col, step=1):
#     if row >= 0 and row < SIZE and \
#         col >= 0 and col < SIZE and \
#         board[row][col] == 0:
#         board[row][col] = step
#         if step == SIZE * SIZE:
#             global total
#             total += 1
#             print(f'第{total}种走法: ')
#             print_board(board)
#         patrol(board, row - 2, col - 1, step + 1)
#         patrol(board, row - 1, col - 2, step + 1)
#         patrol(board, row + 1, col - 2, step + 1)
#         patrol(board, row + 2, col - 1, step + 1)
#         patrol(board, row + 2, col + 1, step + 1)
#         patrol(board, row + 1, col + 2, step + 1)
#         patrol(board, row - 1, col + 2, step + 1)
#         patrol(board, row - 2, col + 1, step + 1)
#         board[row][col] = 0
#
#
# def main():
#     board = [[0] * SIZE for _ in range(SIZE)]
#     patrol(board, SIZE - 1, SIZE - 1)
#
#
# if __name__ == '__main__':
#     main()

    # 动态规划例子：子列表元素之和的最大值。
    #
    # 说明：子列表指的是列表中索引（下标）连续的元素构成的列表；列表中的元素是int类型，可能包含正整数、0、负整数；程序输入列表中的元素，输出子列表元素求和的最大值，例如：
    #
    # 输入：1 - 2
    # 3
    # 5 - 3
    # 2
    #
    # 输出：8
    #
    # 输入：0 - 2
    # 3
    # 5 - 1
    # 2
    #
    # 输出：9

    # 输入：-9 - 2 - 3 - 5 - 3
    #
    # 输出：-2


# def main():
#     items = list(map(int, input().split()))
#     overall = partial = items[0]
#     for i in range(1, len(items)):
#         partial = max(items[i], partial + items[i])
#         overall = max(partial, overall)
#     print(overall)
#
# if __name__ == '__main__':
#     main()

# #  输出函数执行时间的装饰器
#
# """自定义装饰函数的装饰器"""
#
# def record_time(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         start = time()
#         result = func(*args, **kwargs)
#         print(f'{func.__name__}: {time() - start}秒')
#         return result
#     return wrapper



# """输入M和N计算C（M，N）"""
# #定义函数：def是定义函数的关键字，fact是函数名，num是参数（自变量）
# def fac(num):
#     """求阶乘"""
#     result = 1
#     for n in range(1, num + 1):
#         result *= n
#     return result
#
# m = int(input('m = '))
# n = int(input('n = '))
# #放需要计算阶乘的时候不用再重写代码而是直接调用函数fac
# #调用函数的语法是在函数名后面跟上圆括号并传入参数
#
# print(fac(m) // fac(n) // fac(m - n))


# from random import randint
#
# # 定义摇色子的函数，n表示色子的个数，默认值为2
#
# def roll_dice(n=2):
#     """摇色子返回总的点数"""
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total
#
# # 如果没有指定参数，那么n使用默认值2，表示摇两颗色子
# print(roll_dice())
# # 传入参数3，变量n被赋值为3，表示摇三颗色子获得点数
# print(roll_dice(3))


# def add(a=0, b=0, c=0):
#     """三个数相加求和"""
#     return a + b + c
#
#
# # 调用add函数，没有传入参数，那么a、b、c都使用默认值0
# print(add())         # 0
# # 调用add函数，传入一个参数，那么该参数赋值给变量a, 变量b和c使用默认值0
# print(add(1))        # 1
# # 调用add函数，传入两个参数，1和2分别赋值给变量a和b，变量c使用默认值0
# print(add(1, 2))     # 3
# # 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
# print(add(1, 2, 3))  # 6
# # 传递参数时可以不按照设定的顺序进行传递，但是要用“参数名=参数值”的形式
# print(add(c=50, a=100, b=200))    # 350





# #  使用python实现SROCC，PLCC，KROCC的计算
#
# import pandas as pd
# import numpy as np
#
# #输入原始数据
#
# # # 从txt文件中读入数据
#
# test1 = pd.read_table("data.txt")
# a = test1["ScoreA"]
# #print(a)
# test2 = pd.read_table("data.txt")
# b = test2["ScoreC"]
# #print(b)
#
#
# # a = pd.Series([43.5014, 60.2509, 67.3574, 61.2848, 42.9953, 46.6351, 45.4776,
# #                 43.0422, 38.5426, 29.0167, 69.2392, 65.7653, 55.0551, 54.7645])
# # b = pd.Series([0.7353, 0.7269, 0.7287, 0.7487, 0.7668, 0.8523, 0.8414, 0.8279,
# #                0.7145, 0.8279, 0.7240, 0.7223, 0.7211, 0.7198])
#
# # 计算SROCC
#
# SROCC = a.corr(b, method = 'spearman')
# print('SROCC = %.6f' %SROCC)
#
# # 计算KROCC
# KROCC = a.corr(b, method = 'kendall')
# print('KROCC = %.6f' %KROCC)
#
# # 计算PLCC
# PLCC = a.corr(b, method = 'pearson')
# print('PLCC = %.6f' %PLCC)
#
# # 计算均方根误差RMSE
#
# def rmse(predictions, targets):
#     return np.sqrt(((predictions - targets) ** 2).mean())
#
# rmse_val = rmse(np.array(a), np.array(b))
# print('RMSE = %.6f' %rmse_val)


# # class A(object):
# class A:
#     def __init__(self):
#         print("__init__")
#         super(A, self).__init__()
#
#     def __new__(cls):
#         print("__new__")
#         return super(A, cls).__new__(cls)
#
#     def __call__(self):
#         print('__call__')
#
# A()


# """输入M和N计算C(M,N)"""
#
# # 定义函数：def是定义函数的关键字，fac是函数名，num是参数（自变量）
# def fac(num):
#     """求阶乘"""
#     result = 1
#     for n in range(1, num + 1):
#         result *= n
#     #返回num的阶乘（因变量）
#     return result
#
# m = int(input('m = '))
# n = int(input('n = '))
# # 当需要计算阶乘的时候，直接调用函数fac即可
# # 调用函数的语法是在函数名后面跟上圆括号并传入参数
# print(fac(m) // fac(n) // fac(m - n))
# print(fac(m))
# print(fac(n))
# print(fac(m - n))


# """参数的默认值"""
#
# from random import randint
#
# # 定义摇色子的函数，n表示色子的个数，默认值为2
#
# def roll_dice(n = 2):
#     """摇色子返回总的点数"""
#     total = 0
#     for _ in range(n):
#         total += randint(1, 6)
#     return total
# # 如果没有指定参数，那么n使用默认值2，表示摇两个色子
# print(roll_dice())
# # 传入参数3，变量n被赋值为3，表示摇三颗色子获得点数
# print(roll_dice(3))


# """可变参数"""
#
# # 用星号表达式来表示args可以接受0个或任意多个参数
# def add(*args):
#     total = 0
#     # 可变参数可以放在for循环中去除每个参数的值
#     for val in args:
#         total += val
#     return total
#
# # 在调用add函数时可以传入0个或者任意多个参数
# print(add())
# print(add(1))
# print(add(1, 2))
# print(add(1, 2, 3))


# 设计一个生成指定长度验证码的函数

# # 验证码由数字和英文大小写字母构成
#
# import random
#
# ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
# def generate_code(code_len = 4):
#     """生成指定长度的验证码
#     :param code_len:验证码的长度（默认4个字符）
#     :return: 有大小写英文字母和数字构成的随机验证码字符串
#     """
#     code = ''
#     for _ in range(code_len):
#         # 产生0到字符串长度减1单位的随机数作为索引
#         index = random.randrange(0, len(ALL_CHARS))
#         # 利用索引运算从字符串中取出字符进行拼接
#         code += ALL_CHARS[index]
#     return code

# # 例子1：定义一个类描述数字时钟
#
# import time
#
#
# # 定义数字时钟类
# class Clock(object):
#     """数字时钟"""
#
#     def __init__(self, hour=0, minute=0, second=0):
#         """初始化方法
#         :param hour: 时
#         :param minute: 分
#         :param second: 秒
#         """
#         self.hour = hour
#         self.min = minute
#         self.sec = second
#
#     def run(self):
#         """走字"""
#         self.sec += 1
#         if self.sec == 60:
#             self.sec = 0
#             self.min += 1
#             if self.min == 60:
#                 self.min = 0
#                 self.hour += 1
#                 if self.hour == 24:
#                     self.hour = 0
#
#     def show(self):
#         """显示时间"""
#         return f'{self.hour:0>2d}:{self.min:0>2d}:{self.sec:0>2d}'
#
#
# # 创建时钟对象
# clock = Clock(23, 59, 58)
# while True:
#     # 给时钟对象发消息读取时间
#     print(clock.show())
#     # 休眠1秒钟
#     time.sleep(1)
#     # 给时钟对象发消息使其走字
#     clock.run()


# python基础练习100题

# # 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
#
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i != j) and (j != k) and (k != i):
#                 print(i, j, k)


# python编程：从入门到实践前11章习题

# # 2-3
#
# name = input('请输入名字：')
# print("Hello %s,would you like to learn some Python today?" % name)

# # 2-4
#
# name = input('请输入名字: ')
# print(name.upper())
# print(name.lower())
# print(name.title())

    
# # 2-5
#
# name = input('请输入名字： ')
# word = input('请输入名言： ')
# print('%s once said, "%s" ' % (name, word))
    
# # 2-6
# famous_person = 'Albert Einstein'
# message = 'A person who never made a mistake never tried anything new.'
# print(famous_person + 'once said,' + '"' + message + '"')
    
    
# # 2-7
#
# name = input('请输入名字：')
# print('\t' + name.lstrip() + '\n')
# print('\t' + name.rstrip() + '\n')
# print('\t' + name.strip() + '\n')
    
# # 2-8
#
# print(2 + 6)
# print(2 * 4)
# print(10 - 2)
# print(int(16 / 2))
    
    
# # 3-1
#
# names = ['刘元基', '樊文超', '师少勇', '朱迪', '李孟涞', '逯纪元']
# print(names[0])
# print(names[1])
# print(names[2])
# print(names[3])

# # 3-2
# names = ['刘元基', '樊文超', '师少勇', '朱迪', '李孟涞', '逯纪元']
# print(names[0] + '你好')
# print(names[1] + '你好')
# print(names[2] + '你好')
# print(names[3] + '你好')


# # 3-4 3-5 3-6
#
# guest_names = ['Kobe', 'Grandpa', 'wdp']
# # for i in guest_names:
# #     print(i + '诚挚邀请您参加今晚的宴会')
# print(guest_names[0] + '不能赴宴')
# guest_names[0] = 'sss'
# # for i in guest_names:
# #     print(i + '诚挚邀请您参加今晚的宴会')
#
# print('发现了一个更大的餐桌')
# guest_names.insert(0, '秦始皇')
# guest_names.insert(2, 'ddd')
# guest_names.append('ads')
# print(guest_names)
# # for i in guest_names:
# #     print(i + '诚挚邀请您参加今晚的宴会')
#
# print('只能邀请两位嘉宾')
# while len(guest_names) > 2:
#     print("Sorry "+ guest_names.pop() +" I can't invite you !")
# print(guest_names)
#
# del guest_names[1]
# print(guest_names)
# del guest_names[0]
# print(guest_names)

# # 3-8
#
# places = ['上海', '纽约', '苏州', '武汉', '威海']
# print(places)
# print(sorted(places))
# print(places)
# places.reverse()
# print(places)
# print(places)
# places.reverse()
# print(places)
# places.sort()
# print(places)


# # 4-1
#
# pizza = ['mushroom pizza', 'beckon pizza', 'suage pizza']
# for i in pizza:
#     print('I love ' + i)
# print('I really love bacon pizza!')


# # 4-3
# for i in range(0, 21):
#     print(i)

# # 4-5
# list = []
# for i in range(1,1000001):
#     list.append(i)
# print(min(list))
# print(max(list))
# print(sum(list))



# # 实例2: 工资结算系统
#
# from abc import ABCMeta, abstractmethod
#
# class Employee(metaclass = ABCMeta):
#     """员工"""
#
#     def __init__(self, name):
#         self.name = name
#
#     @abstractmethod
#     def get_salary(self):
#         """结算月薪"""
#         pass
#
# class Manager(Employee):
#     """部门经理"""
#
#     def get_salary(self):
#         return 15000.0
#
# class Programmer(Employee):
#     """程序员"""
#
#     def __init__(self, name, working_hour = 0):
#         super().__init__(name)
#         self.working_hour = working_hour
#
#     def get_salary(self):
#         return 200 * self.working_hour
#
# class Salesman(Employee):
#     """销售员"""
#
#     def __init__(self, name, sales = 0):
#         super().__init__(name)
#         self.sales = sales
#
#     def get_salary(self):
#         return 1800 + self.sales * 0.05
#
# emps = [
#     Manager('刘备'), Programmer('诸葛亮'), Manager('曹操'),
#     Programmer('荀彧'), Salesman('吕布'), Programmer('张辽'),
# ]
# for emp in emps:
#     if isinstance(emp, Programmer):
#         emp.working_hour = int(input(f'请输入{emp.name}本月工作时间: '))
#     elif isinstance(emp, Salesman):
#         emp.sales = float(input(f'请输入{emp.name}本月销售额: '))
#     print(f'{emp.name}本月工资为: ￥{emp.get_salary():.2f}元')


#  手撸se_resnet代码

import torch.nn as nn
from torch.hub import load_state_dict_from_url
from torchvision.models import ResNet
from senet.se_module import SELayer

def conv3x3(in_planes, out_planes, stride = 1):
    return nn.Conv2d(in_planes, out_planes, kernel_size = 3, stride = stride, padding = 1, bias = False)

class SEBasicBlock(nn.Module):
    expension = 1

    def __init__(self, inplanes, planes, stride=1, downsample=None, groups=1,
                 base_width = 64, dilation = 1, norm_layer = None,
                 *, reduction = 16):
        super(SEBasicBlock, self).__init__()
        self.conv1 = conv3x3(inplanes, planes, stride)
        self.bn1 = nn.BatchNorm2d(planes)
        self.relu = nn.ReLU(inplace = True)
        self.conv2 = conv3x3(planes, planes, 1)
        self.bn2 = nn.BatchNorm2d(planes)
        self.se = SELayer(planes, reduction)
        self.downsample = downsample
        self.stride = stride

    def forward(self, x):
        residual = x
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)
        out = self.se(out)

        if self.downsample is not None:
            residual = self.downsample(x)

        out += residual
        out = self.relu(out)

        return out

class SEBottleneck(nn.Module):
    expansion = 4

    def __init__(self, inplanes, planes, stride=1,downsample=None, groups=1,
                 base_with = 64, dilation = 1,norm_layer = None, *, reduction = 16):
        super(SEBottleneck, self).__init__()
        self.conv1 = nn.Conv2d(inplanes, planes, kernel_size = 1, bias = False)
        self.bn1 = nn.BatchNorm2d(planes)
        self.conv2 = nn.Conv2d(planes, planes, kernel_size=3, stride=stride,
                               padding = 1, bias=False)
        self.bn2 = nn.BatchNorm2d(planes)
        self.conv3 = nn.Conv2d(planes, planes * 4, kernel_size = 1, bias = False)
        self.bn3 = nn.BatchNorm2d(planes * 4)
        self.relu = nn.ReLU(inplace = True)
        self.se = SELayer(planes * 4,reduction)
        self.downsample = downsample
        self.stride = stride

    def forward(self, x):
        residual = x

        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv1(out)
        out = self.bn2(out)
        out = self.relu(out)

        out = self.conv3(out)
        out = self.bn3(out)
        out = self.se(out)

        if self.downsample is not None:
            residual = self.downsample(x)

        out += residual
        out = self.relu(out)

        return out
    def se_resnet18(num_class=1_000):
        """Constructs a ResNet-18 model.
           Args:
               pretrained (bool): If True, returns a model pre-trained on ImageNet
        """
        model = ResNet(SEBasicBlock, [2, 2, 2, 2], num_classes = num_classes)
        model.avgpool = nn.AdaptiveAvgPool2d(1)
        return model

    def se_resnet34(num_classes=1_000):
        """Constructs a ResNet-34 model.
            Args:
                pretrained (bool): If True, returns a model pre-trained on ImageNet
        """
        model = ResNet(SEBasicBlock, [3, 4, 6, 3], num_classes)
        model.avgpool = nn.AdaptiveAvgPool2d(1)
        return model

    def se_resnet50(num_classes=1_000, pretrained=False):
        """Constructs a ResNet-50 model.
        Args:
            pretrained (bool): If True, returns a model pre-trained on ImageNet
        """
        model = ResNet(SEBottleneck, [3, 4, 6, 3], num_classes=num_classes)
        model.avgpool = nn.AdaptiveAvgPool2d(1)
        if pretrained:
            model.load_state_dict(load_state_dict_from_url(
                "https://github.com/moskomule/senet.pytorch/releases/download/archive/seresnet50-60a8950a85b2b.pkl"))
        return model

    def se_resnet101(num_classes=1_000):
        """Constructs a ResNet-101 model.
        Args:
            pretrained (bool): If True, returns a model pre-trained on ImageNet
        """
        model = ResNet(SEBottleneck, [3, 4, 23, 3], num_classes=num_classes)
        model.avgpool = nn.AdaptiveAvgPool2d(1)
        return model

    def se_resnet152(num_classes=1_000):
        """Constructs a ResNet-152 model.
        Args:
            pretrained (bool): If True, returns a model pre-trained on ImageNet
        """
        model = ResNet(SEBottleneck, [3, 8, 36, 3], num_classes=num_classes)
        model.avgpool = nn.AdaptiveAvgPool2d(1)
        return model






