# # 计算图
#
# import torch
# w = torch.tensor([1.], requires_grad = True)
# x = torch.tensor([2.], requires_grad = True)
# #print(w.shape)
# #print(x.shape)
#
# a = torch.add(w, x)
# b = torch.add(w, 1)
# y =torch.mul(a, b)
#
# y.backward(retain_graph = True)
# print(w.grad)
#
# y.backward()  #pytorch默认不保存计算图，因此第一次计算梯度之后再进行第二次梯度计算时，计算图已经被清空。
# # 第一次设置retrain_graph = True之后，第二次的反向传播就可以计算了



# pytorch实现逻辑回归

import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np
torch.manual_seed(10)

sample_nums = 100
mean_value = 1.7
bias = 1
n_data = torch.ones(sample_nums, 2)

x0 = torch.normal(mean_value * n_data, 1) + bias
y0 = torch.zeros(sample_nums)

x1 = torch.normal(-mean_value * n_data, 1) + bias
y1 = torch.ones(sample_nums)

train_x = torch.cat((x0, x1), 0)
train_y = torch.cat((y0, y1), 0)

class LR(nn.Module):
    def __init__(self):
        super(LR, self).__init__()
        self.features = nn.Linear(2, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.features(x)
        x = self.sigmoid(x)
        return x

lr_net = LR()

loss_fn = nn.BCELoss()

lr = 0.01
optimizer = torch.optim.SGD(lr_net.parameters(), lr = lr, momentum = 0.9)


for iteration in range(1000):
    # 前向传播
    y_pred = lr_net(train_x)
    # 计算loss
    loss = loss_fn(y_pred.squeeze(), train_y)
    # 反向传播
    loss.backward()
    # 更新参数
    optimizer.step()
    # 清空梯度
    optimizer.zero_grad()
    # 绘图
    if iteration % 20 == 0:
        mask = y_pred.ge(0.5).float().squeeze()
        correct = (mask == train_y).sum()
        acc = correct.item() / train_y.size(0)

        plt.scatter(x0.data.numpy()[:, 0], x0.data.numpy()[:, 1], c = 'r', label = 'class 0')
        plt.scatter(x1.data.numpy()[:, 0], x1.data.numpy()[:, 1], c = 'r', label = 'class 1')

        w0, w1 = lr_net.features.weight[0]
        w0, w1 = float(w0.item()), float(w1.item())
        plot_b = float(lr_net.features.bias[0].item())
        plot_x = np.arange(-6, 6, 0.1)
        plot_y = (-w0 * plot_x - plot_b) / w1

        plt.xlim(-5, 7)
        plt.ylim(-7, 7)
        plt.plot(plot_x, plot_y)

        plt.text(-5, 5, 'Loss=%.4f' % loss.data.numpy(), fontdict={'size': 20, 'color': 'red'})
        plt.title("Iteration: {}\nw0:{:.2f} w1:{:.2f} b: {:.2f} accuracy:{:.2%}".format(iteration, w0, w1, plot_b, acc))
        plt.legend()
        # plt.savefig(str(iteration / 20)+".png")
        plt.show()
        plt.pause(0.5)
        # 如果准确率大于 99%，则停止训练
        if acc > 0.99:
            break