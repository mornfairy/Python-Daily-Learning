import torch
import numpy as np

t = torch.ones((2, 3))
t_0 = torch.cat([t, t], dim = 0)
t_1 = torch.cat([t, t], dim = 1)
print("t_0:{} shape:{}\n t_1:{} shape:{}".format(t_0, t_0.shape, t_1, t_1.shape))


t = torch.ones((2, 3))
t_stack = torch.stack([t, t, t], dim = 2)
print("\n t_stack.shape:{}".format(t_stack.shape))

t_stack = torch.stack([t, t, t], dim = 0)
print("\n t_stack.shape:{}".format(t_stack.shape))