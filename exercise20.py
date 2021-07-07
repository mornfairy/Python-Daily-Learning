# 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

# height = float(input("请输入原始高度："))
# i = int(input("请输入是第几次："))
# h = []
#
# for j in range(2, i+1):
#     height = float(height / 2)
#     h.append(height)
# print('第10次反弹%s米高' % (min(h)/2))
# print('第10次落地时共经过：%.2f米' % (sum(h)*2+100))

tour = []
height = []

hei = 100.0  # 起始高度
tim = 10  # 次数

for i in range(1, tim + 1):
    # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2 * hei)
    hei /= 2
    height.append(hei)

print('总高度：tour = {0}'.format(sum(tour)))
print('第10次反弹高度：height = {0}'.format(height[-1]))
