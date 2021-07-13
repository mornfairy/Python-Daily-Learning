# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
#
# # 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。
#
# list1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#
# letter = input("请输入星期几的第一个字母：")
# if letter == 'M' or letter == 'm':
#     print(list1[0])
# elif letter == 'W' or letter == 'w':
#     print(list1[2])
# elif letter == 'F' or letter == 'f':
#     print(list1[4])
# else:
#     if letter == 'T' or letter == 't':
#         letter1 = input("请输入第二个字母：")
#         if letter1 == 'u' or letter == 'U':
#             print(list1[1])
#         else:
#             print(list1[3])
#     else:
#         letter2 = input("请输入第二个字母：")
#         if letter2 == 'a' or letter == 'A':
#             print(list1[5])
#         else:
#             print(list1[6])

# 高赞解答（字典方法）

weeklist = {'M': 'Monday','T': {'u': 'Tuesday','h':'Thursday'}, 'W': 'Wednesday', 'F':'Friday','S':{'a':'Saturday','u':'Sunday'}}
sLetter1 = input("请输入首字母：")
sLetter1 = sLetter1.upper()

if (sLetter1 in ['T','S']):
    sLetter2 = input("请输入第二个字母：")
    print(weeklist[sLetter1][sLetter2])
else:
    print(weeklist[sLetter1])
