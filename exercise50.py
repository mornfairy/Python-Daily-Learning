# pytorch教程

import torch
import torchvision
import torch.nn as nn
import numpy as np
import torchvision.transforms as transforms

# # create tensor
# x = torch.tensor(1., requires_grad = True)
# #print(x.shape)
# w = torch.tensor(2., requires_grad = True)
# b = torch.tensor(3., requires_grad = True)
#
# # build computational graph
# y = w * x + b
#
# # compute gradients
# y.backward()
#
# # print out the gradients
# print(x.grad)
# print(w.grad)
# print(b.grad)

# create tensors of shape(10, 3) and (10, 2)
x = torch.randn(10, 3)
print(x)
y = torch.randn(10, 2)
print(y)

# build a fully connected layer
linear = nn.Linear(3, 2)
print('w', linear.weight)
print('b', linear.bias)

# build loss function and optimizer
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(linear.parameters(), lr = 0.01)

# forward pass
pred = linear(x)
#pred = linear(y)  # 写这个就报维度不匹配的错误了，因为x是10×3，linear的第一维是3刚好匹配
print(pred)

# compute loss
loss = criterion(pred, y)
print(loss)

# backward pass
loss.backward()

# print out the gradients
print('dL/dW: ', linear.weight.grad)
print('dL/db: ', linear.bias.grad)

# 1-step gradient descent
optimizer.step()

# print out the loss after 1-step gradient descent
pred = linear(x)
loss = criterion(pred, y)
print('loss after 1 step optimization: ', loss.item())