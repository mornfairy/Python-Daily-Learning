# 题目：输入某年某月某日，判断这一天是这一年的第几天？
# 思考：需要区分是否为闰年，需要判断是几月份以及那一天。输入变量为：年，月，日
year = int(input("请输入年"))
month = int(input("请输入月份"))
day = int(input("请输入那一天"))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 272, 304, 334)
if 0 < month <= 12:
    sum = months[month - 1]
else:
    print('dara error')
sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 == 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
print('The day is th %d th day' %sum)



