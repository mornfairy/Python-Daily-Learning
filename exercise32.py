# 题目：按相反的顺序输出列表的值。

# list = ['home', 'go', 'to', 'want', 'I']
# list.reverse()
#
# for i in list:
#     print(i,' ', end = "")   # 使用end = ""可以避免主动换行操作

list = ['home', 'go', 'to', 'want', 'I']
for i in list[::-1]:  #使用列表的反向输出方法
    print(i, ' ', end = "")