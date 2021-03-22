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


#example

str1 = 'hello, world!'
print(len(str1))  #通过内置函数len计算字符串长度

print(str1.capitalize())  #将字符串首字母大写后输出

print(str1.title())    #将字符串的每个单词首字母大写之后输出

print(str1.upper())    #将字符串变成大写之后输出

print(str1.find('or')) #查找子串在字符串中的位置
print(str1.find('shit'))  #找不到不会引发异常

print(str1.index('or')) #与find作用类似，但找不到会引发异常
#print(str1.index('shit'))  #找不到，引发异常

print(str1.startswith('He'))  #检查字符串是否以指定的字符开始，返回值为布尔类型
print(str1.startswith('hel'))

print(str1.endswith('!'))    #检查字符串是否以指定的字符结尾

print(str1.center(50,'*'))   #将字符串以指定的宽度剧中并在两侧填充指定字符
print(str1.rjust(50,' '))    #将字符串以指定的宽度靠右放置并在左侧填充指定字符

str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True
str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())


















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
