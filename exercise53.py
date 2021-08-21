#  构建线性回归

import torch
import matplotlib.pyplot as plt

lr = 0.5

#创建训练数据
x = torch.rand(20, 1) * 10
#print(x)
y = 2 * x + (5 + torch.randn(20, 1))

w = torch.randn((1), requires_grad = True)
b = torch.zeros((1), requires_grad = True)

for iteration in range(1000):

    # 前向传播
    wx = torch.mul(w, x)
    y_pred = torch.add(wx, b)

    # 计算MSE loss
    loss = (0.5 * (y - y_pred) ** 2).mean()

    # 反向传播
    loss.backward()

    # 更新参数
    b.data.sub_(lr * b.grad)
    w.data.sub_(lr * w.grad)

    # 每次更新参数之后，都要清零张量的梯度
    w.grad.zero_()
    b.grad.zero_()

    # 绘图，每个20次重新绘制直线
    if iteration % 20 == 0:

        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), y_pred.data.numpy(), 'r-', lw = 5)
        plt.text(2, 20, 'Loss = %.4f' % loss.data.numpy(), fontdict={'size': 20, 'color': 'red'})
        plt.xlim(1.5, 10)
        plt.ylim(8, 28)
        plt.title("Iteration :{}\nw: {} b: {}".format(iteration, w.data.numpy(), b.data.numpy()))
        plt.pause(0.5)

        # 如果MSE小于1，则停止训练
        if loss.data.numpy() < 1:
            break
