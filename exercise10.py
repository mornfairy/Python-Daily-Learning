# 题目：暂停一秒输出，并格式化当前时间。

import time,datetime
time.sleep(1)
time_now = datetime.datetime.now()
print(time_now.strftime("%Y.%m.%d %H-%M-%S"))