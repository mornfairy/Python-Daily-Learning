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

#完美数

import math

for i in range(1,1000):
    result = 0
    for num in range(1,int(math.sqrt(i)) + 1):   # 这一步比较难想出来，math.sqrt(i) + 1为啥要用这种？？？
        if i % num == 0:
            result += num
            if num > 1 and i // num != num:
                result += i // num
    if result == i:
        print(i)



















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
