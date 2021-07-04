# 题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示
# score = int(input("请输入分数："))
#
# if score >= 90:
#     grade = 'A'
# elif score >= 60:
#     grade = 'B'
# else:
#     grade = 'C'
#
# print("成绩%d对应的等级为：%s"%(score,grade))


# 高赞答案

# score = int(input('输入分数:\n'))
# print(['C','C','B','A'][int(score/30)])  #此种输出方法没见过

print(['A','B','C'][1])  #重点记下
