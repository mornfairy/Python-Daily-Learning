# 判断101-200之间有多少个素数，并输出所有素数。

# 判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。

l = []
for i in range(101, 201):
    for j in range(2, i-1):
        if i%j == 0:
            break
    else:#注意else语句的位置，否则输出的列表中的元素数量可能会有差别
        l.append(i)
print(l)
print("素数个数为：%d"%len(l))

